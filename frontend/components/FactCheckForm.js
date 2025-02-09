import { useState } from "react";

export default function FactCheckForm({ setResult }) {
  const [claim, setClaim] = useState("");
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
    <div className="flex flex-col items-center">
      <input
        type="text"
        value={claim}
        onChange={(e) => setClaim(e.target.value)}
        placeholder="Enter a claim..."
        className="px-4 py-2 border border-gray-300 rounded-lg w-80 mb-4"
      />
      
      <button 
        onClick={checkFact} 
        className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-400 transition"
      >
        {loading ? "Checking..." : "Check Fact"}
      </button>
    </div>
  );
}
