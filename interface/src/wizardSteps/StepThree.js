import React, { Component } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class StepOne extends Component {
  render() {
    return (
      <div>
        <div className="Arrow-left">
          <a onClick={this.props.previousStep}>
            <FontAwesomeIcon icon="arrow-left" size="5x" />
          </a>
        </div>
        <div className="Wizard-content">
          <h1>Isso é um teste para criação da wizard</h1>
          <h3>StepThree</h3>
        </div>
      </div>
    );
  }
}

export default StepOne;
