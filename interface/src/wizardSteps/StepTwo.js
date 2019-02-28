import React, { Component } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class StepTwo extends Component {
  render() {
    return (
      <div className="col-md-12">
        <div className="Arrow-left">
          <a onClick={this.props.previousStep}>
            <FontAwesomeIcon icon="arrow-left" size="5x" />
          </a>
        </div>
        <div className="Wizard-content">
          <h1>Isso é um teste para criação da wizard</h1>
          <h3>StepTwo</h3>
        </div>
        <div className="Arrow-right">
          <a onClick={this.props.nextStep}>
            <FontAwesomeIcon icon="arrow-right" size="5x" />
          </a>
        </div>
      </div>
    );
  }
}

export default StepTwo;
