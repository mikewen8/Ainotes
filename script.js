/*
const notesContainer = document.querySelector(".notes-container");
const createBtn = document.querySelector(".btn");
let notes = document.querySelectorAll(".input-box");

createBtn.addEventListener("click", ()=>{
    let inputBox = document.createElement("p");
    let img = document.createElement("img");
    inputBox.className = "input-box";
    inputBox.setAttribute("contenteditable", "true");
    img.src = "images/delete.png";
    notesContainer.appendChild(inputBox).appendChild(img);
    let noteContent = inputBox.textContent.trim();
    
    let formData = new FormData();
    formData.append('content', noteContent);
    fetch('/add_note', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert('Note saved successfully');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

} )
*/

const notesContainer = document.querySelector(".notes-container");
const createBtn = document.querySelector(".btn");

createBtn.addEventListener("click", () => {
    let inputBox = document.createElement("div");
    let contentBox = document.createElement("p");
    let img = document.createElement("img");

    inputBox.className = "note";
    contentBox.className = "input-box";
    contentBox.setAttribute("contenteditable", "true");
    img.src = "images/delete.png";

    // Append the content and delete icon to the note
    inputBox.appendChild(contentBox);
    inputBox.appendChild(img);
    notesContainer.appendChild(inputBox);

    // Add event listener to delete the note
    img.addEventListener("click", () => {
        notesContainer.removeChild(inputBox);
    });

    // Save the note content on input change
    contentBox.addEventListener("input", () => {
        let noteContent = contentBox.textContent.trim();

        // Skip empty notes
        if (noteContent === "") {
            return;
        }

        let formData = new FormData();
        formData.append('content', noteContent);

        fetch('/add_note', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert('Note saved successfully');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});


