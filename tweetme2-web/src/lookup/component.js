export function loadTweets(callback) {
    // initial setup
    const xhr = new XMLHttpRequest();
    const method = "GET"; //"POST"
    const url = " http://localhost:8000/api/tweets/"; // Changing this url so our react app can have some sort of connection with django server
    const responseType = "json";
  
    // perform the request
    xhr.responseType = responseType; //set it's own response type to initial response type
    xhr.open(method, url); //Open up the request with this method and this url
    //now handle this whenever it's loded
    xhr.onload = function () {
      callback(xhr.response, xhr.status);
    }; // return xhr response and it's status
    xhr.onerror = function (e) {
      console.log(e);
      callback({ message: "Request was the error" }, 400);
    };
    xhr.send(); // triger this request
  }
  