import React, { Component } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class StepOne extends Component {
  render() {
    return (
      <div>
        <div className="Wizard-content">
          <h1>Isso é um teste para criação da wizard</h1>
          <h3>StepOne</h3>
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

export default StepOne;
