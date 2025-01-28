socket = io()

const bago = ({ message, label }) => {
  $('#logline').append($("<li>").html(`
    <span style="color: ${label?.color ?? "#6167e9"}"><b>${label.text} ⟩⟩</b></span> ${message}
  `))
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