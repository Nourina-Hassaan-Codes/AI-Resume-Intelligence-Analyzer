function ResumeUpload({ resume, setResume }) {
  return (
    <div className="card">
      <h2>1. Upload Resume</h2>

      <p>
        Upload your PDF, DOCX, or TXT resume.
      </p>

      <input
        type="file"
        accept=".pdf,.docx,.txt"
        onChange={(event) =>
          setResume(event.target.files[0])
        }
      />

      {resume && (
        <p className="file-name">
          Selected: {resume.name}
        </p>
      )}
    </div>
  );
}

export default ResumeUpload;
