function test_network_from_torch2(){
  let textArea = document.getElementById("interactive-inputs")
  let outputArea = document.getElementById("interactive-outputs")

  let icc_result = eel.get_icc_respond(textArea.value)();

  res1.then(a=>{
      outputArea.innerText = icc_result;
      return false;
  })
}