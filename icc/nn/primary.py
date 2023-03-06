import torch
import torch.nn as nn
import torch.nn.functional as F


class FCLayer(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_features, out_features),
            nn.LayerNorm([out_features]),
            nn.ReLU()
        )

    def forward(self, input):
        return self.net(input)

class FCBlock(nn.Module):
    def __init__(self,
                 hidden_ch,
                 num_hidden_layers,
                 in_features,
                 out_features,
                 outermost_linear=False):
        super().__init__()

        self.net = []
        self.net.append(FCLayer(in_features=in_features, out_features=hidden_ch))

        for i in range(num_hidden_layers):
            self.net.append(FCLayer(in_features=hidden_ch, out_features=hidden_ch))

        if outermost_linear:
            self.net.append(nn.Linear(in_features=hidden_ch, out_features=out_features))
        else:
            self.net.append(FCLayer(in_features=hidden_ch, out_features=out_features))

        self.net = nn.Sequential(*self.net)

    def __getitem__(self,item):
        return self.net[item]

    def forward(self, input):
        return self.net(input)


class VAE(torch.nn.Module):

    # For simplicity we assume encoder and decoder share same hyperparameters
    def __init__(self, in_features, num_hidden_layers=2, hidden_ch=128,
                                                 latent_features=5, beta=10):
        super().__init__()

        self.beta = beta

        self.encoder = FCBlock(in_features=in_features,
                               hidden_ch = hidden_ch,
                               num_hidden_layers=num_hidden_layers,
                               out_features=2*latent_features,
                               outermost_linear=True)

        self.decoder = FCBlock(in_features = latent_features,
                               hidden_ch = hidden_ch,
                               num_hidden_layers=num_hidden_layers,
                               out_features=in_features,
                               outermost_linear=True)

    # Returns reconstruction, reconstruction loss, and KL loss
    def forward(self, x):
        """
        return: recon, recon_loss, self.beta * kld_loss
        """

        # Split encoding into mu/logvar, reparameterize, and decode

        mu, log_var = self.encoder(x).chunk(2,dim=1)

        std    = torch.exp(0.5*log_var)
        eps    = torch.randn_like(std)
        sample = mu + (eps * std)

        recon  = self.decoder(sample)

        # Compute reconstruction and kld losses

        recon_loss = torch.linalg.norm(recon-x,dim=1)
        kld_loss   = -0.5 * (1 + log_var - mu.pow(2) - log_var.exp())

        return recon, recon_loss, self.beta*kld_loss


class Attention(nn.Module):
    """Attention layer"""
        
    def __init__(self, dim, use_weight=False, hidden_size=512):
        super(Attention, self).__init__()
        self.use_weight = use_weight
        self.hidden_size = hidden_size
        if use_weight:
            print('| using weighted attention layer')
            self.attn_weight = nn.Linear(hidden_size, hidden_size, bias=False)
        self.linear_out = nn.Linear(2*dim, dim)

    def forward(self, output, context):
        """
        - args
        output : Tensor
            decoder output, dim (batch_size, output_size, hidden_size)
        context : Tensor
            context vector from encoder, dim (batch_size, input_size, hidden_size)
        - returns
        output : Tensor
            attention layer output, dim (batch_size, output_size, hidden_size)
        attn : Tensor
            attention map, dim (batch_size, output_size, input_size)
        """
        batch_size = output.size(0)
        hidden_size = output.size(2)
        input_size = context.size(1)

        if self.use_weight:
            output = self.attn_weight(output.contiguous().view(-1, hidden_size)).view(batch_size, -1, hidden_size)

        attn = torch.bmm(output, context.transpose(1, 2))
        attn = F.softmax(attn.view(-1, input_size), dim=1).view(batch_size, -1, input_size) # (batch_size, output_size, input_size)

        mix = torch.bmm(attn, context) # (batch_size, output_size, hidden_size)
        comb = torch.cat((mix, output), dim=2) # (batch_size, output_size, 2*hidden_size)
        output = torch.tanh(self.linear_out(comb.view(-1, 2*hidden_size)).view(batch_size, -1, hidden_size)) # (batch_size, output_size, hidden_size)

        return output, attn
