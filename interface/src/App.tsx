import * as React from "react";
import "./App.css";

import logo from "./logo.svg";
import GetExampleComponent from './example/components/getExample/getExampleComponent';

class App extends React.Component {
  public render() {    
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Arquitetura Liga</h1>
        </header>
        <GetExampleComponent />
      </div>
    );
  }
}

export default App;
