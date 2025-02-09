import { useState } from "react";

export default function Home() {
  const [claim, setClaim] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkFact = async () => {
    setLoading(true);
    const response = await fetch("/api/fact-check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: claim }),
    });

    const data = await response.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Fact Checker</h1>
      <input
        type="text"
        value={claim}
        onChange={(e) => setClaim(e.target.value)}
        placeholder="Enter a claim..."
      />
      <button onClick={checkFact}>Check Fact</button>
      {loading && <p>Checking...</p>}
      {result && (
        <div className="result">
          <h2>Result: {result.result === 1 ? "True ✅" : "False ❌"}</h2>
          <p><strong>Evidence:</strong> {result.evidence}</p>
        </div>
      )}
      <style jsx>{`
        .container { text-align: center; padding: 20px; }
        input { width: 50%; padding: 10px; }
        button { margin-top: 10px; padding: 10px; }
        .result { margin-top: 20px; background: #f9f9f9; padding: 20px; border-radius: 5px; }
      `}</style>
    </div>
  );
}
