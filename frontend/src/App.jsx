import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // New state to store previous predictions
  const [history, setHistory] = useState([]);

  const handlePredict = async () => {
    setError("");
    setResult(null);

    if (!message.trim()) {
      setError("Please enter a CRM request first.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      if (!response.ok) {
        throw new Error("Backend request failed.");
      }

      const data = await response.json();

      // Show latest prediction result
      setResult(data);

      // Add latest prediction to history
      setHistory((previousHistory) => [
        {
          message: message,
          intent: data.intent,
          confidence: data.confidence,
          route: data.route,
        },
        ...previousHistory,
      ]);
    } catch (err) {
      setError("Could not connect to backend. Make sure FastAPI is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h1>Tiny CRM Agent Router</h1>

        <p className="subtitle">
          Enter a CRM-related user request. The trained SLM will predict the
          intent and route it to the correct agent.
        </p>

        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Example: Summarize this customer conversation"
        />

        <button onClick={handlePredict} disabled={loading}>
          {loading ? "Predicting..." : "Predict Intent"}
        </button>

        {error && <p className="error">{error}</p>}

        {result && (
          <div className="result-box">
            <h2>Prediction Result</h2>
            <p>
              <strong>Intent:</strong> {result.intent}
            </p>
            <p>
              <strong>Confidence:</strong>{" "}
              {(result.confidence * 100).toFixed(2)}%
            </p>
            <p>
              <strong>Route:</strong> {result.route}
            </p>
          </div>
        )}

        {history.length > 0 && (
          <div className="history-box">
            <h2>Prediction History</h2>

            {history.map((item, index) => (
              <div className="history-item" key={index}>
                <p>
                  <strong>Message:</strong> {item.message}
                </p>
                <p>
                  <strong>Intent:</strong> {item.intent}
                </p>
                <p>
                  <strong>Confidence:</strong>{" "}
                  {(item.confidence * 100).toFixed(2)}%
                </p>
                <p>
                  <strong>Route:</strong> {item.route}
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;