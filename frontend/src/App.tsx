import { useEffect, useState} from 'react'
import axios from 'axios'

type Todo = {
  id: number
  title: string
  description: string
  completed: boolean
}

function App() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  useEffect(() => {
    fetchTodos();
  }, [])

  const fetchTodos = async () => {
    const res = await axios.get("http://localhost:8000/todos");
    setTodos(res.data);
  };

  const addTodo = async (e: React.FormEvent) => {
    e.preventDefault();
    const newTodo = { title, description, completed: false };
    await axios.post("http://localhost:8000/todos", newTodo);
    setTitle('');
    setDescription('');
    fetchTodos();
  };

  const toggleCompleted = async (todo: Todo) => {
    const updated = { ...todo, completed: !todo.completed };
    await axios.put(`http://localhost:8000/todos/${todo.id}`, updated);
    fetchTodos();
  };

  const deleteTodo = async (id: number) => {
    await axios.delete(`http://localhost:8000/todos/${id}`);
    fetchTodos();
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Todo List</h1>

      <form onSubmit={addTodo} style={{ marginBottom: "1rem" }}>
        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" required/>
        <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description"/>
        <button type="submit">Add</button>
      </form>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <strong
              style={{
                textDecoration: todo.completed ? "line-through" : "none",
                cursor: "pointer",
              }}
              onClick={() => toggleCompleted(todo)}
            >
              {todo.title}
            </strong>{" "}
             - {todo.description}{" "}
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App
