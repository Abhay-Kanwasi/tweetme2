// useEffect will be run our http request
import React, { useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';

// function loadTweets is imported(copied) form home.html
function loadTweets(callback) {
  // initial setup
  const xhr = new XMLHttpRequest()
  const method = 'GET' //"POST"
  const url = " http://localhost:8000/api/tweets/" // Changing this url so our react app can have some sort of connection with django server
  const responseType = "json"

  // perform the request
  xhr.responseType = responseType  //set it's own response type to initial response type
  xhr.open(method, url) //Open up the request with this method and this url
  //now handle this whenever it's loded
  xhr.onload = function(){
    callback(xhr.response, xhr.status)
  } // return xhr response and it's status
  xhr.onerror = function (e) {
    console.log(e)
    callback({"message" : "Request was the error"}, 400)
  }
  xhr.send() // triger this request
}
  
function App() {
  const [tweets, setTweets] = useState([{ content: 123 }]) //with this we can use these inside of my component using curly brackets({})
  

  useEffect(() => {
    // do my lookup
    const myCallback = (response, status) => {
      console.log(response, status)
      if (status === 200) {
        setTweets(response) //tweetItems is nothing but response
      }
      else {
        alert("There was an error") // This will get us a pop-up message (localhost: 3000 says (whaterver inside of alert)) in our reacr app 
      }
    }
    loadTweets(myCallback)
    
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {tweets.map((tweets, index) => {
            return <li>{tweets.content}</li>
          })}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
