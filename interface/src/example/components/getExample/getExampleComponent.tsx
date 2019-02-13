import * as React from 'react';
import { Props } from './props';
import { State } from './state';
import ExampleService from 'src/example/service/exampleService';

class GetExampleComponent extends React.Component<Props, State> {
    constructor(props: Props) {
      super(props);
      this.state = {
          Example:[],
          TxtEmail:""        
      }  
    }
    LoadExampleList = () => {

      ExampleService.getListExample({
        email: this.state.TxtEmail
      }).then(e => {
        this.setState({
          Example: e.data.examples
        })
      })
    }
    handleChange(e: React.FormEvent<HTMLInputElement>) {
      this.setState({
        TxtEmail: e.currentTarget.value
      });
    }
  
    render() {    
      return (
        <div>
          <h1>Example Component</h1>
          {this.state.Example.map(function (example, i) {
            return (
              <ul key={example.idExample}>
                <li>ID: {example.idExample}</li>
                <li>Name: {example.name}</li>
                <li>Email: {example.email}</li>
              </ul>
            );
          })}
          <br></br>
          <input id="lblEmail" placeholder="Type your email" value={ this.state.TxtEmail } onChange={ e => this.handleChange(e) }/>
          <button className="btn btn-block btn-danger" onClick={this.LoadExampleList}>Load Example</button>
        </div>
      );
    }
  }
  
  export default GetExampleComponent;