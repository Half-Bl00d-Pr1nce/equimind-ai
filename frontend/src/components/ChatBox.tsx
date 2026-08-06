import { useState } from "react";
import ReactMarkdown from "react-markdown";
import api from "../services/api";

type ChatBoxProps = {
  ticker: string;
  isIndexed: boolean;
};

function ChatBox({
  ticker,
  isIndexed,
}: ChatBoxProps) {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState(0);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  async function handleAsk() {

    if (!ticker.trim()) {
      setAnswer("Please load a company first.");
      return;
    }

    if (!question.trim()) {
      setAnswer("Please enter a question.");
      return;
    }

    try {

      setLoading(true);
      setStatus("Searching SEC filing...");

      const response = await api.get(
        `/chat/${ticker.toUpperCase()}`,
        {
          params: {
            question,
          },
        }
      );

      setStatus("Generating answer...");

      setAnswer(response.data.answer);
      setSources(response.data.sources_used);

      setStatus("");

    } catch (error) {

      console.error(error);

      setStatus("");
      setAnswer("Failed to retrieve an answer.");

    } finally {

      setLoading(false);

    }
  }

  return (
    <div className="mt-8 w-full max-w-4xl rounded-xl border border-slate-800 bg-slate-900 p-6 shadow-lg">

      <h2 className="mb-2 text-2xl font-bold">
        Ask EquiMind AI
      </h2>

      <p className="mb-6 text-slate-400">
        Ask natural language questions about the selected company.
      </p>

      <div className="mb-5 flex items-center gap-3">
        <span className="text-slate-400">
          Selected Company
        </span>

        <span className="rounded-full bg-blue-600 px-4 py-1 font-semibold text-white">
          {ticker || "None"}
        </span>
      </div>

      <textarea
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something about the company..."
        disabled={!ticker.trim() || !isIndexed}
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3 text-white outline-none transition focus:border-blue-500 disabled:cursor-not-allowed disabled:opacity-50"
      />

      <button
        onClick={handleAsk}
        disabled={loading || !isIndexed || !ticker.trim()}
        className="mt-4 rounded-lg bg-green-600 px-6 py-3 font-semibold transition hover:bg-green-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading
          ? "Thinking..."
          : !ticker.trim()
          ? "Enter a Ticker"
          : !isIndexed
          ? "Load Company First"
          : "Ask AI"}
      </button>

      {loading && (
        <div className="mt-6 rounded-lg border border-blue-800 bg-blue-950 p-4 text-blue-300">
          {status}
        </div>
      )}

      {answer && (
        <div className="mt-8 rounded-xl border border-slate-700 bg-slate-950 p-6 shadow-lg">

          <h3 className="mb-5 text-xl font-semibold">
            🤖 Answer
          </h3>

          <ReactMarkdown
            components={{
              p: ({ children }) => (
                <p className="mb-4 leading-7 text-slate-300">
                  {children}
                </p>
              ),

              ul: ({ children }) => (
                <ul className="mb-4 list-disc pl-6 text-slate-300">
                  {children}
                </ul>
              ),

              ol: ({ children }) => (
                <ol className="mb-4 list-decimal pl-6 text-slate-300">
                  {children}
                </ol>
              ),

              li: ({ children }) => (
                <li className="mb-2">
                  {children}
                </li>
              ),

              strong: ({ children }) => (
                <strong className="font-semibold text-white">
                  {children}
                </strong>
              ),
            }}
          >
            {answer}
          </ReactMarkdown>

          <div className="mt-6 flex items-center justify-between border-t border-slate-800 pt-4 text-sm text-slate-500">

            <span>
              Generated using Gemini 3.6 Flash
            </span>

            <span>
              {sources} source chunks
            </span>

          </div>

        </div>
      )}

    </div>
  );
}

export default ChatBox;