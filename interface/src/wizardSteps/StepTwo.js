import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

class StepTwo extends Component {
  render() {
    return (
      <div>
        <h1>Isso é um teste para criação da wizard</h1>
        <h3>StepTwo</h3>        
        <p> 
        <a onClick={this.props.previousStep}><FontAwesomeIcon icon="arrow-left" size="5x"/></a>
        </p>
        <p>
          <a onClick={this.props.nextStep}><FontAwesomeIcon icon="arrow-right" size="5x"/></a>
        </p>
      </div>
    );
  }
}

export default StepTwo; 
