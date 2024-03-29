import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { TweetsComponent } from './tweets';

document.addEventListener('DOMContentLoaded', function() {
  const appEl = document.getElementById('root');
  if (appEl) {
    createRoot(appEl).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );
  }

  const tweetsEl = document.getElementById('tweetme-2');
  if (tweetsEl) {
    createRoot(tweetsEl).render(
      <React.StrictMode>
        <TweetsComponent />
      </React.StrictMode>
    );
  }
});

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();




