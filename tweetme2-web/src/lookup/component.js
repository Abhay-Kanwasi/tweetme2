function lookup(method, endpoint, callback, data) {
  let jsonData;
  if (data) {
    jsonData = JSON.stringify(data)
  }
  const xhr = new XMLHttpRequest();
    const url = `http://localhost:8000/api${endpoint}/` // Changing this url so our react app can have some sort of connection with django server
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
  
    xhr.send(jsonData); // triger this request
  }

// A function to sending the tweet
export function createTweet(newTweet, callback) {
  lookup("POST", "/tweets/create/", callback, {content: newTweet})
}  
export function loadTweets(callback) {
    lookup("GET","/tweets/",callback)
  }
  