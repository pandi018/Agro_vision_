var form = document.getElementById("signup-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // send a request to the server to sign up the user
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/signup", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                alert("Sign up successful! Welcome, " + response.name + "!");
            } else {
                alert(response.error);
            }
        }
    };
    var data = JSON.stringify({
        email: email,
        password: password
    });
    xhr.send(data);
});