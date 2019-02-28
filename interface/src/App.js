import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import "./wizardSteps/Steps.css";
import StepOne from './wizardSteps/StepOne';
import StepTwo from './wizardSteps/StepTwo';
import StepThree from './wizardSteps/StepThree';
import StepWizard from 'react-step-wizard';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons'

library.add(faArrowLeft, faArrowRight)
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="App-body">
        <StepWizard initialStep={1}>
            <StepOne />
            <StepTwo />
            <StepThree />
          </StepWizard>
          </div>
      </div>
    );
  }
}

export default App;
