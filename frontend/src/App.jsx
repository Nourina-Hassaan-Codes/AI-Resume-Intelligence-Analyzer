import { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import JobDescription from "./components/JobDescription";
import AnalysisResult from "./components/AnalysisResult";
import { analyzeResume } from "./services/api";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleAnalyze() {
    if (!resume) {
      setError("Please upload a resume.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }

    setError("");
    setLoading(true);
    setResult(null);

    try {
      const data = await analyzeResume(
        resume,
        jobDescription
      );

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="app">
      <section className="hero">
        <p className="eyebrow">AI-POWERED CAREER INTELLIGENCE</p>

        <h1>
          AI Resume
          <span> Intelligence Analyzer</span>
        </h1>

        <p className="subtitle">
          Compare your resume with a target job and discover
          your real skill gaps.
        </p>
      </section>

      <section className="workspace">
        <ResumeUpload
          resume={resume}
          setResume={setResume}
        />

        <JobDescription
          value={jobDescription}
          setValue={setJobDescription}
        />

        <button
          className="analyze-button"
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {error && (
          <div className="error">
            {error}
          </div>
        )}
      </section>

      {result && (
        <AnalysisResult result={result} />
      )}
    </main>
  );
}

export default App;
