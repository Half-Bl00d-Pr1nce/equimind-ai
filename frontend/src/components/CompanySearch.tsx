import { useState } from "react";
import api from "../services/api";
import axios from "axios";

type CompanySearchProps = {
  ticker: string;
  setTicker: React.Dispatch<React.SetStateAction<string>>;
  setIsIndexed: React.Dispatch<React.SetStateAction<boolean>>;
};

function CompanySearch({
  ticker,
  setTicker,
  setIsIndexed,
}: CompanySearchProps) {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  async function handleLoadFiling() {
    if (!ticker.trim()) return;

    try {
      setLoading(true);
      setMessage("");

      const response = await api.post(
        `/vector/index/${ticker.toUpperCase()}`
      );

      setIsIndexed(true);

      setMessage(
        `🟢 ${response.data.ticker} • ${response.data.status}`
      );

    } catch (error: unknown) {
          let message = "Failed to load company filing.";

    if (axios.isAxiosError(error)) {
      message =
        error.response?.data?.detail ??
        error.message;
    }

    setMessage(`❌ ${message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mt-12 w-full max-w-2xl rounded-xl border border-slate-800 bg-slate-900 p-6 shadow-lg">

      <h2 className="mb-2 text-2xl font-bold">
        Load Company Filing
      </h2>

      <p className="mb-6 text-slate-400">
        Download and index the latest SEC 10-K filing.
      </p>

      <div className="flex gap-4">
        <input
          type="text"
          placeholder="Enter ticker (AAPL)"
          value={ticker}
          onChange={(e) => {
            setTicker(e.target.value);
            setIsIndexed(false);
            setMessage("");
          }}
          className="flex-1 rounded-lg border border-slate-700 bg-slate-950 px-4 py-3 text-white outline-none transition focus:border-blue-500"
        />

        <button
          onClick={handleLoadFiling}
          disabled={loading}
          className="rounded-lg bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? "Loading Filing..." : "Load Filing"}
        </button>
      </div>

      {message && (
        <div className="mt-5 rounded-lg border border-slate-700 bg-slate-950 p-3 text-sm text-slate-300">
          {message}
        </div>
      )}

    </div>
  );
}

export default CompanySearch;