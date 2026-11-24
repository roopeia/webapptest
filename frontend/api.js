async function testBackend() {
  //asettaa napin muuttujaan
  const responseElement = document.getElementById("response");
  responseElement.textContent = "Contacting backend...";

  try {
    const response = await fetch("/api/hello");
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    const data = await response.json();
    responseElement.textContent = data.message;
  } catch (error) {
    responseElement.textContent = `Could not reach the backend: ${error.message}`;
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("api-button")
    .addEventListener("click", testBackend);
});
