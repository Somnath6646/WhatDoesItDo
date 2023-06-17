document.addEventListener("DOMContentLoaded", () => {
  const inputUrl = document.getElementById("inputUrl");
  const submitButton = document.getElementById("submitButton");
  const descriptionContainer = document.getElementById("descriptionContainer");
  const darkModeToggle = document.getElementById("darkModeToggle");

  submitButton.addEventListener("click", () => {
    fetchDescription(inputUrl.value);
  });

  darkModeToggle.addEventListener("click", () => {
    toggleDarkMode();
  });
});

async function fetchDescription(url) {
  try {
    const response = await fetch("http://127.0.0.1:5000/get_response", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "url": url }),
    });

    if (response.ok) {
      const data = await response.json();
      descriptionContainer.textContent = data.description;
    } else {
      descriptionContainer.textContent = "Error fetching description.";
    }
  } catch (error) {
    descriptionContainer.textContent = "Error fetching description.";
  }
}

function toggleDarkMode() {
  document.body.classList.toggle("dark");
}