// src/pages/ai.jsx
import React, { useState, useRef, useEffect } from "react";
import "../styles/ai.css"; // see CSS below (create this file)

export default function AiWidget() {
  const [messages, setMessages] = useState([
    { id: 1, who: "system", text: "Welcome to Etherea AI Widget — try asking something!" },
  ]);
  const [input, setInput] = useState("");
  const listRef = useRef(null);

  // scroll to bottom on new messages
  useEffect(() => {
    if (listRef.current) listRef.current.scrollTop = listRef.current.scrollHeight;
  }, [messages]);

  const sendMessage = () => {
    const trimmed = input.trim();
    if (!trimmed) return;
    const userMsg = { id: Date.now(), who: "you", text: trimmed };
    setMessages((m) => [...m, userMsg]);
    setInput("");

    // fake AI response (replace later with API call)
    setTimeout(() => {
      const botMsg = {
        id: Date.now() + 1,
        who: "ai",
        text: `AI Response (demo): I received "${trimmed}".`,
      };
      setMessages((m) => [...m, botMsg]);
    }, 700); // small delay to simulate thinking
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="ai-page">
      <h1 className="ai-title">AI Widget</h1>

      <div className="ai-chat" ref={listRef}>
        {messages.map((m) => (
          <div key={m.id} className={`ai-bubble ${m.who === "you" ? "you" : m.who === "ai" ? "ai" : "sys"}`}>
            <div className="ai-text">{m.text}</div>
          </div>
        ))}
      </div>

      <div className="ai-input-row">
        <textarea
          className="ai-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your question... (Enter to send)"
          rows={2}
        />
        <button className="ai-send" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}
