import React, { Component } from "react";
import key from 'weak-key';
class CandidatesTable extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      candidates: [],
      loaded: false
    }
  }
	
  componentDidMount() {
    fetch("/api/candidates")
    .then(response => {
      if (response.status !== 200) {
        return this.setState({ placeholder: "Something went wrong" });
      }
      return response.json();
    })
    .then(data => this.setState({ data: data, loaded: true }));
  }
  
  render() {
    
    if (!this.state.loaded) {
      return (
        <p>Loading...</p>
      )
    } else {
      return (
        <div className="column">
          <h2 className="subtitle">
            Showing <strong>{this.state.data.length} items</strong>
          </h2>
          <table className="table is-striped">
            <thead>
              <tr>
                {Object.entries(this.state.data[0]).map(el => <th key={key(el)}>{el[0]}</th>)}
              </tr>
            </thead>
            <tbody>
              {this.state.data.map(el => (
                <tr key={el.id}>
                  {Object.entries(el).map(el => <td key={key(el)}>{el[1]}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )
    }
  }
}
export default CandidatesTable;