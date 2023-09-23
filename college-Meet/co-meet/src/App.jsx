import React from 'react'
import ReactDOM from 'react-dom/client'
import {BrowserRouter as Router, Routes, Route, BrowserRouter} from "react-router-dom";
import { useState } from 'react'
import HomePage  from './pages/HomePage'
import RegisterPage from './pages/RegisterPage'
function App() {
  return (
    <div>
      <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<HomePage />}/>
        <Route path="/register" element={<RegisterPage />}/>
      </Routes>
      </BrowserRouter>
    </div>
  ) 
}

export default App
