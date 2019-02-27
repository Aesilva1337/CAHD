import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import StepOne from './wizardSteps/StepOne';
import StepTwo from './wizardSteps/StepTwo';
import StepWizard from 'react-step-wizard';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <StepWizard initialStep={1}>
            <StepOne />
            <StepTwo />
          </StepWizard>
        </header>
      </div>
    );
  }
}

export default App;
