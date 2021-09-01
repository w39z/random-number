var id = window.setInterval(function(){randomNumber();},5000);

function randomNumber()
{
  var rand = Math.floor(Math.random()*101 | 0);
  $('#holder').html(rand);
}

