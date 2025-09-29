import React, { useState } from "react";
import { predictSpam } from "./api";

const Predict = () => {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const prediction = await predictSpam(email);
    setResult(prediction?.label || "Error predicting");
  };

  return (
    <div>
      <h2>Spam Mail Detection</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Paste your email here"
          rows="6"
          cols="50"
        />
        <br />
        <button type="submit">Predict</button>
      </form>
      {result && <h3>Result: {result}</h3>}
    </div>
  );
};

export default Predict;
