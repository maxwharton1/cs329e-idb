
function searchBar(){

  console.log("function called")
  let str = document.getElementById("searchInput").value;
  console.log(str)
  let http = "http://127.0.0.1:5000/search/" + str;
  console.log(http)

  if (str != ''){
    console.log('accessed');
    window.location.replace(http);

    window.location.reload();

  }
}
