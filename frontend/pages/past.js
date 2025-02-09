import { useEffect, useState } from "react";

export default function PastFactChecks() {
  const [pastChecks, setPastChecks] = useState([]);

  useEffect(() => {
    const fetchPastChecks = async () => {
      const response = await fetch("/api/past-checks");
      const data = await response.json();
      setPastChecks(data.claims);
    };

    fetchPastChecks();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold text-center mb-6 text-blue-600">Past Fact Checks</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {pastChecks.map((claim, index) => (
          <div key={index} className="p-6 bg-white shadow-lg rounded-lg">
            <h2 className="text-lg font-semibold">Claim: {claim}</h2>
            <p className="text-gray-700 mt-2">Evidence: [Stored evidence]</p>
          </div>
        ))}
      </div>
    </div>
  );
}
