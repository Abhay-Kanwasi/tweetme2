import React, { useEffect, useState } from "react";

import {loadTweets} from "../lookup"

// a component that hold our tweets and have an ability to add new tweets

export function TweetsComponent(props) {
  const textAreaRef = React.createRef()
  const [newTweets, setNewTweets] = useState([])
  const handleSubmit = (event) => {
    event.preventDefault()
    const newVal = textAreaRef.current.value
    let tempNewTweets = [...newTweets] // Copied the newTweet list
    //push will send our element into tempNewTweets list
    //but push will put it into last but we need in the very beginning so we use unshift
    tempNewTweets.unshift({
      content: newVal,
      likes: 0,
      id:1243
    })
    setNewTweets(tempNewTweets)
    textAreaRef.current.value = ''
  }
  return <div className={props.className}>
    <div className="col-12 mb-3">
      <form onSubmit={handleSubmit}>
        <textarea ref={textAreaRef} required={true}  className="form-control" name="tweet"> 

      </textarea>
      <button type="submit" className="btn btn-primary my-3">Tweet</button>
      </form>
    </div>
    <TweetsList newTweets={newTweets} />
    </div>
}

// Add this property monitor prop changes and if they do change then we will combine it with another array that has a state (Simply putting we can now tweet through our tweet react app)
export function TweetsList(props) {
  const [tweetsInit, setTweetsInit] = useState([]);
  const [tweets, setTweets] = useState([])
  const [tweetsDidSet, setTweetsDidSet] = useState(false)
  // setTweetsInit([...props.newTweets].concat(tweetsInit)) //But it will cause a infinite loop
  useEffect(() => {
    const final = [...props.newTweets].concat(tweetsInit) // concat(tweetsInit) is after props.newTweets to maintain order how tweets will appear
    if (final.length !== tweets.length) {
      setTweets(final)
    }
  }, [props.newTweets,tweets, tweetsInit])
  useEffect(() => {
    if (tweetsDidSet === false) {
        // do my lookup
        const myCallback = (response, status) => {
          if (status === 200) {
            setTweetsInit(response); //tweetItems is nothing but response
            setTweetsDidSet(true)
          } else {
            alert("There was an error"); // This will get us a pop-up message (localhost: 3000 says (whaterver inside of alert)) in our reacr app
          }
        };
        loadTweets(myCallback);
    } 
  }, [tweetsInit,tweetsDidSet,setTweetsDidSet]);

  return (
    <div>
      {tweets.map((tweet, index) => (
        <Tweet
          tweet={tweet}
          className="my-5 py-5 border bg-white text-dark"
          key={`${index}-${tweet.id}`}
        />
      ))}
    </div>
  );
}

export function ActionBtn(props) {
  const { tweet, action } = props;
  const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0) // useState hook allow changes how this will work
  const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false)
  const className = props.className ? props.className: "btn btn-primary btn-sm";
  const actionDisplay = action.display ? action.display : 'Action'
  
  // Dynamic way to ensure our action(Incase we don't give a type to our action btn so this will show action btn instead)
  const handleClick = (event) => {
    event.preventDefault()
    if (action.type === 'like') {
      if (userLike === true) {
        // Unlike it
        setLikes(likes - 1)
        setUserLike(false)
      }
      else {
        // like it
        setLikes(likes + 1)
        setUserLike(true)
      }  
    }
  }
  const display = action.type === 'like' ? `${likes}${actionDisplay}` : actionDisplay 
  return <button className={className} onClick = {handleClick}>{display}</button>
}

// New way to render our tweet
export function Tweet(props) {
  // using props you can add various elements like tweet className
  const { tweet } = props;
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6"; // Here '?' indicating if it exists and ':' indicating else default
  return (
    <div className={className}>
      <p>
        {tweet.id} - {tweet.content}
      </p>
      <div className="btn btn-group">
      {/* This will display the like unlike and retweet button in our app */}
        <ActionBtn tweet={tweet} action={{ type: "like", display:"Likes" }} />
        <ActionBtn tweet={tweet} action={{ type: "unlike", display: "Unlike" }} />
        <ActionBtn tweet={tweet} action={{ type: "retweet", display: "Retweet" }} />
      </div>
    </div>
  );
}
