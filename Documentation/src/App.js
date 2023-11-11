import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import Get from "./reactfiles/Get"
import Set from "./reactfiles/Set"
import Delete from "./reactfiles/Delete"

function App() {
  const notes = [
    { id: 1, title: "Get", content: "This is how to GET information" },
    { id: 2, title: "Set", content: "This is how to SET information" },
    { id: 3, title: "Delete", content: "This is how to DELETE information" }
  ];
  
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/"></Route>
          <Route path="/info" element={<div className="no-note-selected">Click menu icon for info instructions</div>}></Route>
          <Route path="/info/get" element={<Get />}></Route>
          <Route path="/info/set" element={<Set />}></Route>
          <Route path="/info/delete" element={<Delete />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;