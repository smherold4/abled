import React from "react";
import ReactDOM from "react-dom";
import CandidatesTable from "./components/CandidatesTable";

function renderReactComponents() {
  
  const components_by_id = {
    "CandidatesTable": <CandidatesTable/>
  }

  for (let compId in components_by_id) {
    let rootEl = document.getElementById(compId);
    if (rootEl) {
      let props = rootEl.dataset;
      let componentWithProps = React.cloneElement(components_by_id[compId], props);
      ReactDOM.render(componentWithProps, rootEl);
    }
  }
  
  const components_by_klass = {}

  for (let compKlass in components_by_klass) {
    let els = document.getElementsByClassName(compKlass);

    if (els.length > 0) {
      for (let i = 0; i < els.length; i++) {
        let el = els[i];
        let props = el.dataset;
        let componentWithProps = React.cloneElement(components_by_klass[compKlass], props);
        ReactDOM.render(componentWithProps, el);
      }
    }
  }

}

document.addEventListener('DOMContentLoaded',() => {
  renderReactComponents()
});