// Upload photo
// document.querySelector('.custom-file-input').addEventListener('change',function(e){
//   var fileName = document.getElementById("myInput").files[0].name;
//   var nextSibling = e.target.nextElementSibling
//   nextSibling.innerText = fileName
// })

// Get current date
function getDate() {
  let dateSubStr = Date().substring(4,15)
  document.getElementById('date').value = dateSubStr;
}