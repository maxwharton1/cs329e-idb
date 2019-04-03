
function sharks(books){

  for (var l in books.results){
    url = toURL(l.name)
    document.getElementById('list').innerHTML += '<a href = shark/' + url + ' class = "list-group-item list-group-item-action active">'+ l.name + '</a>';
  }
}

function deals(books){

  for (var l in books.results){
    url = toURL(l.name)
    document.getElementById('list').innerHTML += '<a href = company/' + url + ' class = "list-group-item list-group-item-action active">'+ l.name + '</a>';
  }
}

function thisShark(deals, shark){
  shark = shark[0] //only one shark was passed in

  document.getElementById('info').innerHTML += "<img src= " + shark.picture + "alt='picture' class='img-thumbnail'><br></br>";
  for (var key in shark){
    if (key == "investments"){continue}
    document.getElementById('info').innerHTML += key + ": "+ shark[key] + "<br></br>"; //displays every element in the dict
  }

  for (var l in deals){
    url = toURL(l.name)
    document.getElementById('list').innerHTML += '<a href = ../company/' + url + ' class = "list-group-item list-group-item-action active">'+ l.name + '</a>';
  }
}

function thisComp(deals){

  deal = deals[0]
  document.getElementById('info').innerHTML += "<img src= " + deal.picture + "alt='picture' class='img-thumbnail'><br></br>";
  for (var key in deal){
    if (key == "sharks"){continue}
    document.getElementById('info').innerHTML += key + ": "+ deal[key] + "<br></br>"; //displays every element in the dict
  }

  for (var l in deal.sharks){
    url = toURL(l)
    document.getElementById('list').innerHTML += '<a href = ../company/' + url + ' class = "list-group-item list-group-item-action active">'+ l+ '</a>';
  }
}


function toURL(str){
    str = str.replace(/'/g, "");
    return str.replace(/ /g, "_");
}
