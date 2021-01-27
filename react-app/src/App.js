import React from "react";
import ReactDOM from "react-dom";
import PropTypes from "prop-types";
import { DashApp } from "dash-embedded-component";

window.React = React;
window.ReactDOM = ReactDOM;
window.PropTypes = PropTypes;
// Note: Dash requires PropTypes in the global scope even if it isn't
// used in the project, as described in /Docs/embedded-middleware/usage


function App() {
  return [
    <div style={{ padding: "50px", backgroundColor: "#f0f0f0" }}>
      <h1>React Host Application</h1>
      <div
        style={{
          padding: "50px",
          backgroundColor: "white",
          border: "1px solid lightgray",
        }}
      >
        <h1>Embedded Dash Application</h1>
        <DashApp
          config={{
            url_base_pathname: "https://core-dev.plotly.host/vz-embedded-react",
          }}
        />
      </div>
    </div>,
  ];
}

export default App;
