export default function Result({ result }) {
    return (
      <div className="mt-6 p-6 bg-white shadow-lg rounded-lg w-96">
        <h2 className="text-xl font-semibold">
          Result: {result.result === 1 ? "True ✅" : "False ❌"}
        </h2>
        <h3 className="mt-4 text-lg font-medium">Evidence:</h3>
        <p className="text-gray-700 mt-2">{result.evidence}</p>
      </div>
    );
  }
  