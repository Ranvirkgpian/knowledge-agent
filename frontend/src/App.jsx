import { useState } from "react";
import axios from "axios";
import "./App.css";

export default function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        question,
      });

      setAnswer(res.data.answer);
      setSources(res.data.sources);
    } catch (err) {
      alert("Backend not running.");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Meraki SD-WAN Knowledge Agent</h1>

      <textarea
        rows="5"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askQuestion} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {answer && (
        <>
          <h2>Answer</h2>

          <div className="answer">
            {answer}
          </div>

          <h2>Sources</h2>

          {sources.map((s, i) => (
            <div className="source" key={i}>
              {s}
            </div>
          ))}
        </>
      )}
    </div>
  );
}