import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import Get from "./reactfiles/Get"
import GetTable from "./reactfiles/GetTable"
import Set from "./reactfiles/Set"
import Delete from "./reactfiles/Delete"

function App() {
  const notes = [
    { id: 1, title: "Get", content: "This is how to GET information" },
    { id: 2, title: "GetTable", content: "This is how to GET TABLE information" },
    { id: 3, title: "Set", content: "This is how to SET information" },
    { id: 4, title: "Delete", content: "This is how to DELETE information" }
  ];
  
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/"></Route>
          <Route path="/info" element={<div className="no-note-selected">Welcome to the future of data storage – introducing SustainDBility, where efficiency meets environmental responsibility. Imagine a world where computing resources are consolidated on a massive scale, eliminating idle servers and minimizing energy waste. Our revolutionary server virtualization ensures optimal resource utilization, dynamically scaling to meet demand and conserving energy during downtime. sustainDBility is not just about storing data; it's about storing it responsibly. Join us in shaping a greener, more efficient future. Embrace the sustainDBility – where sustainability meets performance.</div>}></Route>
          <Route path="/info/get" element={<Get />}></Route>
          <Route path="/info/get" element={<GetTable />}></Route>
          <Route path="/info/set" element={<Set />}></Route>
          <Route path="/info/delete" element={<Delete />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;