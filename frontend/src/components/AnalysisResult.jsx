function AnalysisResult({ result }) {
  return (
    <section className="results">
      <div className="result-header">
        <p className="eyebrow">AI ANALYSIS</p>
        <h2>Your Resume Intelligence Report</h2>
      </div>

      <div className="score">
        <strong>{result.match_score}%</strong>
        <span>Match Score</span>
      </div>

      <div className="result-grid">

        <div className="result-card">
          <h3>Matching Skills</h3>

          {result.matching_skills?.length ? (
            <ul>
              {result.matching_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>
          ) : (
            <p>No matching skills detected.</p>
          )}
        </div>

        <div className="result-card">
          <h3>Missing Skills</h3>

          {result.missing_skills?.length ? (
            <ul>
              {result.missing_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>
          ) : (
            <p>No major missing skills detected.</p>
          )}
        </div>

        <div className="result-card">
          <h3>Recommendations</h3>

          <ul>
            {result.recommendations?.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>

      </div>

      <div className="summary">
        <h3>AI Summary</h3>
        <p>{result.summary}</p>
      </div>
    </section>
  );
}

export default AnalysisResult;
