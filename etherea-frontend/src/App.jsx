import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/dashboard.jsx";
import AiWidget from "./pages/ai.jsx"; 
// Add more pages later

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/ai" element={<AiWidget />} />
        {/* Add more routes here */}
      </Routes>
    </BrowserRouter>
  );
}
