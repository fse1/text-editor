import React from "react";

export function NavBar(props) {
  
  return (
    <nav>
      <p>Welcome, {props.user.name}</p>
      <a href={props.links.logout}>Logout</a>
    </nav>
  );
  
}