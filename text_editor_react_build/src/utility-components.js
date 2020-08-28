import React from "react";

export function NavBar(props) {
  
  return (
    <nav className="navigation-bar">
      <p className="navigation-bar-left">Welcome, {props.user.name}!&nbsp;&nbsp;|&nbsp;&nbsp;</p>
      <a href={props.links.logout} className="navigation-bar-right"> Logout</a>
    </nav>
  );
  
}