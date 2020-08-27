import React, { useState, useEffect, Fragment } from "react";
import { NavBar } from "./utility-components.js";
import { CreatePosts, PostHistory } from "./editor-wrappers.js";

function EditorApp(props) {
  
  // state variable of post history, link info, and user info
  const [postHistory, setPostHistory] = useState(null);
  const [linkInfo, setLinkInfo] = useState(null);
  const [userInfo, setUserInfo] = useState(null);
  
  // get initial data from server
  useEffect(() => {
    let infoRequest = new XMLHttpRequest(); 
    infoRequest.onreadystatechange = function () { 
      if (this.readyState === 4 && this.status === 200) { 
        let data = JSON.parse(this.responseText);
        setUserInfo(data.user);
        setLinkInfo(data.links);
        setPostHistory(data.postHistory);
      } 
    };
    
    infoRequest.open('GET', '/editor/get-posts/');
    infoRequest.send();
  }, []);
  
  if (postHistory === null)
  {
    return <h1>Loading... Please wait.</h1>;
  }
  else
  {
    console.log(postHistory);
    console.log(linkInfo);
    console.log(userInfo);
    return (
    <Fragment>
      <NavBar user={userInfo} links={linkInfo} />
      <CreatePosts links={linkInfo} setPostHistory={setPostHistory} />
      <hr />
      <PostHistory postHistory={postHistory} />
    </Fragment>
    );
  }
  
}

export default EditorApp;