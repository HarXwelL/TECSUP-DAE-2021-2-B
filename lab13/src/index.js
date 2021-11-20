import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import {Route,Link,BrowserRouter,Routes} from 'react-router-dom'

import App from './App';
import Users from './users';
import Contact from './contact';
import Notfound  from './notfound';

const routing = (
  <div>
    <BrowserRouter>
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">Home</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <Link className="nav-link" to="/usuarios">Users</Link>
            </li>
            <li class="nav-item">
              <Link className="nav-link" to="/contacto">Contact</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  

      <Routes>
        <Route exact path="/" element={<App />} />
        <Route path="/usuarios" element={<Users />} />
        <Route path="/usuarios/:id" element={<Users />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="*" element = {<Notfound />} />
      </Routes>
    </BrowserRouter>
  </div>
)

ReactDOM.render(
  routing,
  document.getElementById('root')
);

