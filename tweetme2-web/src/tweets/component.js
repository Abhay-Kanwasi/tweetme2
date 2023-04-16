import React, { useEffect, useState } from "react";

import {loadTweets} from "../lookup"

export function TweetsList(props) {
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    // do my lookup
    const myCallback = (response, status) => {
      if (status === 200) {
        setTweets(response); //tweetItems is nothing but response
      } else {
        alert("There was an error"); // This will get us a pop-up message (localhost: 3000 says (whaterver inside of alert)) in our reacr app
      }
    };
    loadTweets(myCallback);
  }, []);

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
  const className = props.className
    ? props.className
    : "btn btn-primary btn-sm";
  return action.type === "like" ? (
    <button className={className}>{tweet.likes} Likes</button>
  ) : null;
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
        <ActionBtn tweet={tweet} action={{ type: "like" }} />
        <ActionBtn tweet={tweet} action={{ type: "unlike" }} />
      </div>
    </div>
  );
}
