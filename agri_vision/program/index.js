let form = document.querySelector('form');
form.addEventListener('submit', function(event) 
{
  event.preventDefault();
  let username = document.querySelector('#username').value;
  let password = document.querySelector('#password').value;
  if(username=="user" && password=="pass")
  {
    window.location.replace("farmer.html");
  }
  else{
    alert("failed please check your username and password")
  }
});