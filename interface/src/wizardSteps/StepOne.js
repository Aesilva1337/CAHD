import React, { Component } from 'react';

class StepOne extends Component {
  render() {
    return (
      <div>
        <h1>Isso é um teste para criação da wizard</h1>
        <h3>StepOne</h3>
        <p>
          <button onClick={this.props.previousStep}>Previous Step</button>
        </p>
        <p>
          <button onClick={this.props.nextStep}>Next Step</button>
        </p>
      </div>
    );
  }
}

export default StepOne;
