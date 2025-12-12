import React, { useState } from "react";
import "./AI.css";

function AI() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = () => {
    if (!input.trim()) return;

    const newMessage = { sender: "user", text: input };
    setMessages([...messages, newMessage]);
    setInput("");

    // Temporary AI reply (you can replace later)
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        { sender: "ai", text: "This is Etherea AI responding!" },
      ]);
    }, 600);
  };

  return (
    <div className="ai-container">
      <h1>Etherea AI</h1>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <p key={i} className={msg.sender === "user" ? "user-msg" : "ai-msg"}>
            {msg.text}
          </p>
        ))}
      </div>

      <div className="input-row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default AI;
