import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './app/App';
import data from "./data.json"

let {group, album, released, studio, songs}= data

 

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App group={group} album={album} released={released} studio={studio} songs={songs}/>
  </React.StrictMode>
);


