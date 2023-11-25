const apiButton = document.querySelector('.apiButton');
const apiCodeInput = document.getElementById('api_code');

const apiUrl = "http://localhost:105"

apiButton.addEventListener('click', function() {
    //let yourForm = document.getElementById("myform");
    const apiCodeValue = apiCodeInput.value;
    //const jwtToken = getCookie('jwt');

    // Fetch API call
    if (apiCodeValue == "hello"){
      fetch(`${apiUrl}/${apiCodeValue}`, {method: 'GET'})
      .then(response => response.json())
      .then(data => {
        console.log(data);
        alert(JSON.stringify(data.message));
      })
      .catch(error => {
        console.log("Fetch error! (hello)");
      });
    } else if (apiCodeValue == "test"){
      fetch(`${apiUrl}/${apiCodeValue}`, {method: 'POST'})
      .catch(error => {
        console.log("Fetch error! (test)");
      });
    }
});

function getCookie(name) {
    const cookieString = document.cookie;
    const cookies = cookieString.split(';');
  
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + '=')) {
        return cookie.substring(name.length + 1);
      }
    }
  
    return null;
  }