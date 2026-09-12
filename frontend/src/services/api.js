// const API_URL = "http://127.0.0.1:8000/api";
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function analyzeResume(
  resume,
  jobDescription
) {
  const formData = new FormData();

  formData.append("resume", resume);
  formData.append(
    "job_description",
    jobDescription
  );


// Example fetch call
const response = await fetch(`${API_BASE_URL}/api/analyze`, {
  method: "POST",
  body: formData,
});


  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail || "Analysis failed."
    );
  }

  return data;
}
