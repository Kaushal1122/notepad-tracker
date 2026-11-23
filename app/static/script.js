const editor = document.getElementById("editor");
const filePath = document.getElementById("file-path");
const saveStatus = document.getElementById("save-status");

const newButton = document.getElementById("new-btn");
const openButton = document.getElementById("open-btn");
const saveButton = document.getElementById("save-btn");

const autosaveDelay = Number(editor.dataset.autosaveDelay);

let autosaveTimer = null;
let isSaving = false;
let saveAgain = false;


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

        clearTimeout(autosaveTimer);

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

        clearTimeout(autosaveTimer);

        filePath.value = data.path;
        editor.value = data.content;
        saveStatus.textContent = "File opened";

    } catch (error) {
        alert(error.message);
    }
}


async function saveFile(showError = true) {
    const path = filePath.value.trim();

    if (!path) {
        saveStatus.textContent = "Create or open a file first";
        return;
    }

    if (isSaving) {
        saveAgain = true;
        return;
    }

    isSaving = true;

    const content = editor.value;

    saveStatus.textContent = "Saving...";

    try {
        const response = await fetch("/api/files", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                path,
                content
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        if (
            editor.value === content &&
            filePath.value.trim() === path
        ) {
            saveStatus.textContent = data.committed
                ? "Saved and committed"
                : "Saved - no changes";
        } else {
            saveStatus.textContent = "Unsaved changes";
        }

    } catch (error) {
        saveStatus.textContent = "Save failed";

        if (showError) {
            alert(error.message);
        }

    } finally {
        isSaving = false;

        if (saveAgain) {
            saveAgain = false;

            if (editor.value !== content || filePath.value.trim() !== path) {
                saveFile(false);
            }
        }
    }
}


function scheduleAutosave() {
    clearTimeout(autosaveTimer);

    saveStatus.textContent = "Unsaved changes";

    autosaveTimer = setTimeout(() => {
        saveFile(false);
    }, autosaveDelay);
}


editor.addEventListener("input", scheduleAutosave);

newButton.addEventListener("click", createFile);
openButton.addEventListener("click", openFile);
saveButton.addEventListener("click", () => saveFile(true));
