import React, { useState } from "react";
import axios from "axios";
import { FiMail, FiShield, FiAlertTriangle, FiCheckCircle } from "react-icons/fi";

function Home() {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/predict", {
        message: email
      });
      setResult(response.data);
    } catch (error) {
      console.error(error.response?.data || error.message);
      setResult({ error: "Something went wrong. Please try again." });
    } finally {
      setIsLoading(false);
    }
  };

  const clearResults = () => {
    setResult(null);
    setEmail("");
  };

  return (
    <div className="home-container">
      <div className="hero-section">
        <div className="hero-content">
          <h1 className="hero-title">
            <FiShield className="hero-icon" />
            Spam Mail Detection
          </h1>
          <p className="hero-subtitle">
            Protect yourself from phishing scams and spam emails with our advanced AI-powered detection system
          </p>
        </div>
      </div>

      <div className="detection-section">
        <div className="card main-form-card">
          <div className="card-header">
            <h2>
              <FiMail className="card-icon" />
              Email Analyzer
            </h2>
            <p className="card-subtitle">Paste your email content below to detect spam</p>
          </div>

          <form onSubmit={handleSubmit} className="email-form">
            <div className="textarea-container">
              <textarea
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Paste your email content here...&#10;&#10;Example: &#10;Subject: You've won $1000!&#10;Click here to claim your prize immediately..."
                className="email-textarea"
                rows="8"
                required
              />
              <div className="char-count">{email.length} characters</div>
            </div>

            <div className="form-actions">
              <button 
                type="submit" 
                className="btn btn-primary"
                disabled={isLoading || !email.trim()}
              >
                {isLoading ? (
                  <>
                    <div className="spinner"></div>
                    Analyzing...
                  </>
                ) : (
                  <>
                    <FiAlertTriangle className="btn-icon" />
                    Check for Spam
                  </>
                )}
              </button>
              
              {(result || email) && (
                <button 
                  type="button" 
                  onClick={clearResults}
                  className="btn btn-secondary"
                >
                  Clear
                </button>
              )}
            </div>
          </form>

          {result && (
            <div className={`result-container ${result.label === 'Spam' ? 'spam'.toLowerCase() : result.label?.toLowerCase()}`}>
              <div className="result-header">
                <div className="result-icon">
                  {result.label === 'Ham' ? (
                    <FiCheckCircle className="success-icon" />
                  ) : result.label === 'Spam' ? (
                    <FiAlertTriangle className="danger-icon" />
                  ) : (
                    <FiAlertTriangle className="error-icon" />
                  )}
                </div>
                <div className="result-text">
                  <h3 className="result-title">
                    {result.error ? 'Error' : result.label === 'Ham' ? 'Safe Email' : 'Spam Detected'}
                  </h3>
                  <p className="result-subtitle">
                    {result.error ? result.error : result.confidence}
                  </p>
                </div>
              </div>
              
              {result.spam_type && (
                <div className="spam-details">
                  <strong>Spam Type:</strong> {result.spam_type}
                </div>
              )}
            </div>
          )}
        </div>

        <div className="info-cards">
          <div className="card info-card">
            <FiShield className="info-icon" />
            <h3>AI-Powered Detection</h3>
            <p>Advanced machine learning algorithms analyze email patterns and content</p>
          </div>
          
          <div className="card info-card">
            <FiAlertTriangle className="info-icon" />
            <h3>Real-time Analysis</h3>
            <p>Get instant results to protect yourself from harmful emails</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;