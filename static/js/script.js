document.addEventListener("DOMContentLoaded", () => {
  const yearTarget = document.getElementById("currentYear");
  if (yearTarget) {
    yearTarget.textContent = new Date().getFullYear();
  }
});