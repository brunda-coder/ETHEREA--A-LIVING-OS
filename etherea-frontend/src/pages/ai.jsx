import React, { useState } from "react";

export default function AiWidget() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  function handleSend() {
    if (!input.trim()) return;
    setResponse("✨ AI response coming soon...");
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Widget 🤖</h1>

      <input
        type="text"
        placeholder="Ask something..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ padding: "10px", width: "60%" }}
      />

      <button
        onClick={handleSend}
        style={{ padding: "10px 20px", marginLeft: "10px" }}
      >
        Send
      </button>

      <p style={{ marginTop: "20px" }}>{response}</p>
    </div>
  );
}

