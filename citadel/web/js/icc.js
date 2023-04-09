function iccrespond(){
  let textArea = document.getElementById("interactive-inputs")
  

  let icc_result = eel.get_icc_respond(textArea.value)();

  icc_result.then(a=>{
      replaceOutputs(a)
  })
}

function replaceOutputs(a){
  let outputArea = document.getElementById("interactive-outputs")
  outputArea.innerText = a;
  
}