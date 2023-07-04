import React from "react";
import ProcessMap from "./process-map";
import Toolbox from "./toolbox";
import "./App.css";

function App() {
  return (
    <div className="App" data-theme="light">
      <div className="drawer drawer-open">
        <input id="drawer-toggle" type="checkbox" className="drawer-toggle" />
        <div className="drawer-content">
          <ProcessMap />
        </div>
        <div className="drawer-side">
          <Toolbox />
        </div>
      </div>
    </div>
  );
}

export default App;
