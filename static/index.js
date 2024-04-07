document.getElementById("submitButton").addEventListener("click", function() {
    var loadingSpinner = document.createElement("span");
    loadingSpinner.className = "loading loading-spinner loading-sm";
    this.appendChild(loadingSpinner);
  });