import { useState } from "react";
import { Bot, BrainCircuit, Database, FileText } from "lucide-react";

import CompanySearch from "../components/CompanySearch";
import ChatBox from "../components/ChatBox";

function Home() {
  const [ticker, setTicker] = useState("");
  const [isIndexed, setIsIndexed] = useState(true);

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-black">
      <div className="mx-auto flex max-w-6xl flex-col items-center px-6 py-16">

        {/* Hero */}

        <div className="mb-10 flex items-center gap-5">

          <div className="rounded-2xl bg-blue-600 p-4 shadow-lg">
            <Bot
              size={42}
              className="text-white"
            />
          </div>

          <div>
            <h1 className="text-5xl font-bold tracking-tight">
              EquiMind AI
            </h1>

            <p className="mt-2 text-lg text-slate-400">
              AI-Powered Equity Research Assistant
            </p>
          </div>

        </div>

        <p className="max-w-3xl text-center text-lg leading-8 text-slate-400">
          Analyze SEC filings using Retrieval-Augmented Generation (RAG),
          semantic search, and Gemini AI to instantly answer questions
          about any public company.
        </p>

        {/* Feature Cards */}

        <div className="mt-14 grid w-full grid-cols-1 gap-6 md:grid-cols-3">

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

            <FileText
              className="mb-4 text-blue-400"
              size={32}
            />

            <h3 className="mb-2 text-lg font-semibold">
              SEC Filings
            </h3>

            <p className="text-slate-400">
              Download and process the latest SEC 10-K filings directly from EDGAR.
            </p>

          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

            <Database
              className="mb-4 text-green-400"
              size={32}
            />

            <h3 className="mb-2 text-lg font-semibold">
              Vector Search
            </h3>

            <p className="text-slate-400">
              Retrieve the most relevant filing sections using Qdrant semantic search.
            </p>

          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

            <BrainCircuit
              className="mb-4 text-purple-400"
              size={32}
            />

            <h3 className="mb-2 text-lg font-semibold">
              AI Analysis
            </h3>

            <p className="text-slate-400">
              Generate concise answers grounded in SEC filings using Gemini 3.6 Flash.
            </p>

          </div>

        </div>

        <CompanySearch
          ticker={ticker}
          setTicker={setTicker}
          setIsIndexed={setIsIndexed}
        />

        <ChatBox
          ticker={ticker}
          isIndexed={isIndexed}
        />

        <footer className="mt-20 text-center text-sm text-slate-500">
          Built with React • FastAPI • Qdrant • Gemini 3.6 Flash
        </footer>

      </div>
    </main>
  );
}

export default Home;