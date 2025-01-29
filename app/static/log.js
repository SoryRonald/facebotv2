socket = io()

const bago = ({ message, label }) => {
  if (typeof message == "string"){
    let $hasLabel = label?.text ? `<span style="color: ${label?.color ?? "#6167e9"}"><b>${label.text} ⟩⟩ </b></span>` : ''
    $('#logline').append($("<li>").html(`${$hasLabel}${message}`))
  }else{
    if (message?.user){
      const { name, uid, threadId, command } = message.user;
      $("#logline").append($("<li>").addClass("user").html(`
        <div class="head bg-dark">${name}</div>
        <div class="body">
          <span><b>UserID: </b>${uid}</span><br>
          <span><b>ThreadID: </b>${threadId}</span><br>
          <span class="command"><b>Command: </b>${command}</span>
        </div>
      `))
    }
  }
  console.log("Haha")
  const ul = document.getElementById('logline');
  ul.scrollTop = ul.scrollHeight;
}

// get the new log
socket.on("log", (data) => {
  bago(data)
})

// get all logs
async function logs(session){
  try{
    const response = await fetch(`/api/logs/${session}`);
    const data = await response.json();
    bago({
      message: `Session <i>${session}</i>`,
      label: {
        text: "FLASK",
        color: "#FF9D3D"
      }
    })
    data.forEach(log => bago(log))
  }catch(error){
    bago({
      message: error,
      label: {
        text: "ERROR",
        color: "red"
      }
    })
  }
}

// clear log
$(document).ready(function(){
  $("#clear").click(function(){
    $("#logline").html("")
    socket.emit('clearLog', {})
  })
  
  $("#test").click(() => {
    
  })
})