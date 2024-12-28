const apiBase = "https://todoapifunction.azurewebsites.net/api/ToDoFunction?code=w0fv9msxegHVOGCY4Rddi0v7xsQqu1t9G9dBxLE3iekvAzFuAHJ5Eg%3D%3D"

// Fetch all to-do items
async function fetchTodos() {
    const response = await fetch(apiBase);
    const todos = await response.json();
    const todoList = document.getElementById("todo-list");
    todoList.innerHTML = ""; // Clear the list
    todos.forEach(todo => {
        const div = document.createElement("div");
        div.className = "todo-item";
        div.innerHTML = `
            <span>${todo.task} (${todo.completed ? "Completed" : "Pending"})</span>
            <button class="button" onclick="deleteTodo(${todo.id})">Delete</button>
            <button class="button" onclick="markComplete(${todo.id})">Mark Complete</button>
        `;
        todoList.appendChild(div);
    });
}

// Add a new to-do
async function addTodo() {
    const task = document.getElementById("task").value;
    if (!task) return alert("Task cannot be empty");
    await fetch(apiBase, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: Date.now(), task, completed: false })
    });
    document.getElementById("task").value = ""; // Clear input
    fetchTodos(); // Refresh the list
}

// Delete a to-do
async function deleteTodo(id) {
    await fetch(apiBase, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id })
    });
    fetchTodos(); // Refresh the list
}

// Mark a to-do as complete
async function markComplete(id) {
    const response = await fetch(apiBase);
    const todos = await response.json();
    const todo = todos.find(t => t.id === id);
    if (!todo) return alert("To-Do not found");

    await fetch(apiBase, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...todo, completed: true })
    });
    fetchTodos(); // Refresh the list
}

// Initial fetch
fetchTodos();
