import React, { useState } from "react";
import axios from "axios";

function MailForm() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/predict", { message });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error connecting to backend");
    }
  };

  return (
    <div className="card">
      <form onSubmit={handleSubmit}>
        <textarea
          rows="6"
          cols="60"
          placeholder="Enter your email message here..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          required
        />
        <br />
        <button type="submit">Check Spam</button>
      </form>

      {result && (
        <div className="result">
          <h4>Result</h4>
          <p><b>Prediction:</b> {result.prediction}</p>
          {result.spam_type && <p><b>Spam Type:</b> {result.spam_type}</p>}
        </div>
      )}
    </div>
  );
}

export default MailForm;
