function previewFile() {
    var preview = document.getElementById("namo");
    var file  = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
     preview.src = reader.result;
    }
    if (file) {
     reader.readAsDataURL(file);
    } else {
     preview.src = "";
    }
}

function deletePost(id){
    let elementId = "article-container-" + id
    let element = document.getElementById(elementId)
    element.remove()
}

function lovePost(id){
    let heart = document.getElementById("heart-image" + id)
    if (heart.src.indexOf("active") == -1){
        heart.src = "tweeter active"
    }
    else{
        heart.src = "tweeter"
    }
}

function checkCharacterCount(textArea){
    let counter  = document.getElementById("input-characters")
    let container = document.getElementById("form-container")
    if (textArea.value.length > 140){
        textArea.value = textArea.value.substr(0,140)
        container.classList.add("is-error")
    }else{
        container.classList.remove("is-error")
    }
    counter.innerText = textArea.value.length
}

function submitPost() {
    let textArea = document.getElementById("input-textarea")
    let counter = document.getElementById("input-characters")
    let contentToPost = textArea.value;
    
    if(contentToPost.length === 0) {
        return false;
    }
    if (contentToPost == "view calendar") {
        createPostHTML(`To view the calender of the Citadel, clcik this <a href="fullcalendar.html">calender</a> for further details`);
    }
    
    if (contentToPost == "view dashboard") {
        createPostHTML(`To view the calender of the Citadel, clcik this <a href="dash.html">calender</a> for further details`);
    }

    if (contentToPost == "view stats") {
        createPostHTML(`To view the stats of the Citadel click this <a href="stats.html">stats</a> for further details.`)
    } else {
        createPostHTML(contentToPost)
    
        let res1 = eel.get_respond(textArea.value)();
    
        res1.then(a=>{
            createRespondHTML(a)
        })
    }
    textArea.value = "";
    counter.innerText = 0;
    return false;

}

let currentPostId = 1;
function createPostHTML(postContent) {
    let now = new Date()
    let time = now.toLocaleTimeString()
    let date = now.toLocaleString()
    let name = "Arthas"
    let username = "ysun697@gatech.edu"
    
    currentPostId = currentPostId + 1
    
    /**
    postContent = postContent.replace(/</g, "&lt;")
    postContent = postContent.replace(/\n/g, "<br />")
    postContent = postContent.replace(/(https?:\/\/[^\s]+)/g, "<a href=\"$1\" target=\"_blank\">$1</a>")
    **/
    let template = `
        <article id="article-container-${currentPostId}">
            <header>
                <button class="close" onclick="deletePost(${currentPostId})">
                    <img src="src/close.png" height="15" width="15"/>
                </button>
                <div class="avatar">
                <img src = "src/lck.png" height="40" width="40"/>
                </div>
                <h1>${name}</h1>
                <h2>@${username}</h2>
            </header>
            <blockquote>
                ${postContent}
            </blockquote>
            <hr/>
            <footer>
                <p class="date-posted">Posted
                    <time>${date}</time>
                </p>

            </footer>
        </article>`
    document.getElementById("form-container").insertAdjacentHTML("afterend", template)
}

function createRespondHTML(postContent) {
    let now = new Date()
    let time = now.toLocaleTimeString()
    let date = now.toLocaleString()
    let name = "The LichKing"
    let username = "zongjingli@gmail.com"
    
    currentPostId = currentPostId + 1
    
    postContent = postContent.replace(/</g, "&lt;")
    postContent = postContent.replace(/\n/g, "<br />")
    postContent = postContent.replace(/(https?:\/\/[^\s]+)/g, "<a href=\"$1\" target=\"_blank\">$1</a>")
    
    let template = `
        <article id="article-container-${currentPostId}">
            <header>
                <button class="close" onclick="deletePost(${currentPostId})">
                    <img src="src/close.png" height="15" width="15"/>
                </button>
                <div class="avatar">
                <img src = "src/arthas.png" height="40" width="40"/>
                </div>
                <h1>${name}</h1>
                <h2>@${username}</h2>
            </header>
            <blockquote>
                ${postContent}
            </blockquote>
            <hr/>
            <footer>
                <p class="date-posted">Posted
                    <time>${date}</time>
                </p>

            </footer>
        </article>`
    document.getElementById("form-container").insertAdjacentHTML("afterend", template)
}

function test_string_from_python(){
    
    let res1 = eel.test_str()()
    /*document.getElementById("test-name").innerText = template*/
    res1.then(a=>{

		let test_element = document.getElementById("test-name")
		test_element.innerText = a
	
	})
}

function test_network_from_torch(){
    let textArea = document.getElementById("input-textarea")

    let res1 = eel.test_network(textArea.value)();
    textArea.value = "";

    res1.then(a=>{
        let test_element = document.getElementById("test-name")
		test_element.innerText = a
	})
}

function test_network_from_torch2(){
    let textArea = document.getElementById("input-textarea")
    let counter = document.getElementById("input-characters")

    let res1 = eel.get_respond(textArea.value)();

    res1.then(a=>{
        createRespondHTML(a)
        return false;
	})
}
function previewFile() {
    var preview = document.getElementById('preview-img');
    var file  = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
     preview.src = reader.result;
    }
    if (file) {
     reader.readAsDataURL(file);
    } else {
     preview.src = "";
    }
}

