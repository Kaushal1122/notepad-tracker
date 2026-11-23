const editor = document.getElementById("editor");
const filePath = document.getElementById("file-path");
const saveStatus = document.getElementById("save-status");

const newButton = document.getElementById("new-btn");
const openButton = document.getElementById("open-btn");
const saveButton = document.getElementById("save-btn");


async function createFile() {
    const path = prompt("Enter the complete path for the new file:");

    if (!path) {
        return;
    }

    try {
        const response = await fetch("/api/files", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ path })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        filePath.value = data.path;
        editor.value = "";
        saveStatus.textContent = "New file created";
        editor.focus();

    } catch (error) {
        alert(error.message);
    }
}


async function openFile() {
    const path = filePath.value.trim();

    if (!path) {
        alert("Please enter a file path.");
        return;
    }

    try {
        const params = new URLSearchParams({ path });

        const response = await fetch(`/api/files?${params}`);

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        editor.value = data.content;
        filePath.value = data.path;
        saveStatus.textContent = "File opened";

    } catch (error) {
        alert(error.message);
    }
}


async function saveFile() {
    const path = filePath.value.trim();

    if (!path) {
        alert("Please create or open a file first.");
        return;
    }

    saveStatus.textContent = "Saving...";

    try {
        const response = await fetch("/api/files", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                path,
                content: editor.value
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        saveStatus.textContent = "Saved";

    } catch (error) {
        saveStatus.textContent = "Save failed";
        alert(error.message);
    }
}


editor.addEventListener("input", () => {
    saveStatus.textContent = "Unsaved changes";
});

newButton.addEventListener("click", createFile);
openButton.addEventListener("click", openFile);
saveButton.addEventListener("click", saveFile);
