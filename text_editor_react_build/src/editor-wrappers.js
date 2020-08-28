import React, { useState, Fragment } from "react";
import SlateEditor from "./slate-editor.tsx";

export function CreatePosts(props) {
  
  const [editorState, setEditorState] = useState(initialValue);
  
  function PostSubmit(props) {
    
    function handleSubmit(event, submitLink, setPostHistory) {
      event.preventDefault();
      let data = new FormData(event.currentTarget);
      
      let createPostRequest = new XMLHttpRequest(); 
      createPostRequest.onreadystatechange = function () { 
        if (this.readyState === 4 && this.status === 200) { 
          let postData = JSON.parse(this.responseText);
          setPostHistory((postHistory) => {let new_array = []; new_array.push(postData); return new_array.concat(postHistory) });
        } 
      };
      
      createPostRequest.open('POST', submitLink);
      createPostRequest.send(data);
    }
    
    return (
    <Fragment>
      <form className="create-post-form" action={props.links.createPost} method="post" encType="multipart/form-data" onSubmit={(e) => handleSubmit(e, props.links.createPost, props.setPostHistory)}>
        <input type="hidden" name="post-content" value={JSON.stringify(props.editorState)} />
        <input type="submit" value="Create Post" />
      </form>
    </Fragment>
    );
  }
  
  return (
  <div className="create-post-area">
    <h1>Create New Post</h1>
    <div className="slate-editor"><SlateEditor editable={true} valueCallback={setEditorState} initialValue={initialValue} /></div><br />
    <PostSubmit editorState={editorState} links={props.links} setPostHistory={props.setPostHistory} /><br />
  </div>
  );
  
}

export function PostHistory(props) {
  
  return (
  <div className="post-history-area">
    <h1>Post History (Newest to Oldest)</h1>
    <br />
    {props.postHistory.map((post) => 
      <Fragment key={post.id}>
        <div>
          <h3>Post Creation Date: {post.initialCreationDate}</h3>
          <div className="slate-editor"><SlateEditor editable={false} initialValue={post.content} /></div>
        </div>
        <br />
      </Fragment>
    )}
  </div>
  );
}

const initialValue = [
  {
    type: 'paragraph',
    children: [
      { text: '' },
    ],
  },
]