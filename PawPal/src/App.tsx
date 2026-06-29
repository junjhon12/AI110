import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="min-h-screen bg-slate-100 flex items-center justify-center p-6">
      <div className="bg-white p-8 rounded-2xl shadow-xl max-w-sm text-center border border-slate-200">
        <h1 className="text-3xl font-bold text-indigo-600 mb-2">PawPal+</h1>
        <p className="text-slate-600 font-medium">Tailwind & TSX Integration Successful! 🐾</p>
      </div>
    </div>
    </>
  )
}

export default App
