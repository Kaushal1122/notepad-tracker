const editor = document.getElementById("editor");
const filePath = document.getElementById("file-path");
const saveStatus = document.getElementById("save-status");
const newButton = document.getElementById("new-btn");

editor.addEventListener("input", () => {
    saveStatus.textContent = "Unsaved changes";
});

newButton.addEventListener("click", () => {
    editor.value = "";
    filePath.value = "";
    saveStatus.textContent = "New file";
    editor.focus();
});
