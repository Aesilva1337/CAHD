import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import StepOne from './wizardSteps/StepOne';
import StepTwo from './wizardSteps/StepTwo';
import StepWizard from 'react-step-wizard';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons'

library.add(faArrowLeft, faArrowRight)
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
