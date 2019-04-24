
function searchBar(){

  console.log('anything');
  console.log('saldjf');

  let str = document.getElementById("searchInput").value;
  let http = "http://127.0.0.1:5000/search/" + str;


  if (str != ''){

    //window.location.href = http;
    console.log(http);
  }
}

function tester(){
  console.log('test compmlete');
}
