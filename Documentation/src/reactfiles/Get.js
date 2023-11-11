import React from "react";

export default function Get() {

  return (
    <div id="Note">
      <div className="note-info">
        <div className="title-date">
          <h2>How to GET information:</h2>
          <small>In order to retrieve info, you need to initialize a connection object. Do this by calling connection.get and the argument is a key, which is the key of the table</small>
        </div>
      </div>
    </div>
  );
}