const API_URL = "http://127.0.0.1:8000/api";

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

  const response = await fetch(
    `${API_URL}/analyze`,
    {
      method: "POST",
      body: formData,
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail || "Analysis failed."
    );
  }

  return data;
}
