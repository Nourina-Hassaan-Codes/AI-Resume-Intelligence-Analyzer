function JobDescription({ value, setValue }) {
  return (
    <div className="card">
      <h2>2. Target Job</h2>

      <p>
        Paste the job description you want to target.
      </p>

      <textarea
        value={value}
        onChange={(event) =>
          setValue(event.target.value)
        }
        placeholder="Paste the complete job description here..."
        rows="12"
      />
    </div>
  );
}

export default JobDescription;
