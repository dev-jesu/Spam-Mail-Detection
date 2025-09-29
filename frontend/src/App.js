import React from "react";
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from "react-router-dom";
import { FiShield, FiBarChart2 } from "react-icons/fi";
import Home from "./pages/Home";
import About from "./pages/About";
import "./App.css";

function Navigation() {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <FiShield className="brand-icon" />
        <h2>Spam Detection System</h2>
      </div>
      <div className="navbar-links">
        <Link 
          to="/" 
          className={location.pathname === "/" ? "active" : ""}
        >
          <FiShield className="nav-icon" />
          Home
        </Link>
        <Link 
          to="/about" 
          className={location.pathname === "/about" ? "active" : ""}
        >
          <FiBarChart2 className="nav-icon" />
          Analytics
        </Link>
      </div>
    </nav>
  );
}

function App() {
  return (
    <Router>
      <Navigation />
      
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
