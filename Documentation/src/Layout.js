import React, { useEffect, useState } from "react";
import { Outlet, useNavigate, useParams } from "react-router-dom";
// import Get from "./reactfiles/Get";
// import Set from "./reactfiles/Set";
// import Delete from "./reactfiles/Delete";
// import { v4 as uuidv4 } from "uuid";

function Layout() {
  const navigate = useNavigate();
  const LOCAL_STORAGE_KEY = "notesApp.notes";
  const params = useParams();
  const [notes, setNotes] = useState(() => {
    const store = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
    if (store === null) {
      return [];
    } else {
      return store;
    }
  });

  const [sidebar, setSidebar] = useState(false);
  const showSidebar = () => setSidebar(!sidebar);

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(notes));
  }, [notes]);

  return (
    <>
      <div id="title">
        <h1>SustainDBility</h1>
        <p>Code the Change 2023: Hackathon</p>
      </div>
      <label id="sidebar" onClick={showSidebar}>
        &#9776;
      </label>
      <nav className={sidebar ? "nav-menu active" : "nav-menu"}>
        <div id="head">
          <h2>Info</h2>
          <button type="button" onClick={showSidebar} class="closebtn">
            <b>X</b>
          </button>
        </div>
        <button className="nav-menu-items" onClick={(()=>{navigate("info/get")})}>
          <h2>Get</h2>
        </button>
        <button className="nav-menu-items" onClick={(()=>{navigate("info/gettable")})}>
          <h2>GetTable</h2>
        </button>
        <button className="nav-menu-items" onClick={(()=>{navigate("info/set")})}>
          <h2>Set</h2>
        </button>
        <button className="nav-menu-items" onClick={(()=>{navigate("info/delete")})}>
          <h2>Delete</h2>
        </button>
      </nav>
      <div className={sidebar ? "content menuActive" : "content"}>
        <Outlet context={[notes, setNotes]} />
      </div>
    </>
  );
}

export default Layout;