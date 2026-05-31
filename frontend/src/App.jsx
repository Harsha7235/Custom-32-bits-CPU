import { useState, useEffect, useRef } from "react"
import axios from "axios"


import CodeEditor from "./components/Editor"
import Registers from "./components/Registers"
import Memory from "./components/Memory"
import Stats from "./components/Stats"
import Controls from "./components/Controls"
import Loading from "./components/Loading"
import ModeSelector from "./components/ModeSelector"

import VMEditor from "./components/VMEditor"
import BinaryViewer from "./components/BinaryViewer"
import StackView from "./components/StackView"
import Pipeline from "./components/Pipeline"
import FlowGraph from "./components/FlowGraph"
import ISAReference from "./components/ISAReference"
import Guidelines from "./components/Guidelines"

import {
  loadProgram,
  stepProgram,
  resetCPU
} from "./api/cpuApi"


export default function App(){

// ---------------- BOOT ----------------

const [booting,setBooting] = useState(true)

// ---------------- MODE ----------------

const [mode,setMode] = useState("developer")

useEffect(()=>{
axios.get("http://127.0.0.1:8000/mode")
.then(res=>setMode(res.data.mode))
},[])


// ---------------- TABS ----------------

const [tab,setTab] = useState("cpu")

// ---------------- CODE ----------------

const [code,setCode] = useState("")

// ---------------- CPU STATE ----------------

const [state,setState] = useState({
registers:[],
memory:[],
pc:0,
sp:0,
binary:[]
})

// ---------------- SPEED ----------------

const [speed,setSpeed] = useState(1)

const intervalRef = useRef(null)


// ---------------- LOAD ----------------

async function load(){

const res = await loadProgram(code)

console.log("Binary:", res.data.binary)

setState(prev => ({
...prev,
registers: res.data.registers,
memory: res.data.memory,
pc: res.data.pc,
sp: res.data.sp,
binary: res.data.binary || []
}))

}


// ---------------- STEP ----------------

async function step(){

const res = await stepProgram()

setState(prev => ({
...prev,
...res.data,
binary: prev.binary
}))

}


// ---------------- RUN ----------------

function run(){

if(intervalRef.current) return

intervalRef.current = setInterval(async()=>{

const res = await stepProgram()

setState(prev => ({
...prev,
...res.data,
binary: prev.binary
}))

if(!res.data.running){
clearInterval(intervalRef.current)
intervalRef.current = null
}

},600/speed)

}


// ---------------- PAUSE ----------------

function pause(){
clearInterval(intervalRef.current)
intervalRef.current = null
}


// ---------------- RESET ----------------

async function reset(){

pause()

const res = await resetCPU()

setState(prev => ({
...prev,
...res.data,
binary: prev.binary
}))

}

// ---------------- LOADING SCREEN ----------------

if(booting){
return <Loading onFinish={()=>setBooting(false)} />
}


// ---------------- UI ----------------

return(

<div className="bg-gray-100 min-h-screen p-4">

{/* TITLE + MODE */}

<div style={{display:"flex",justifyContent:"space-between",marginBottom:"10px"}}>
<h2 className="text-xl font-bold text-green-700">
Custom CPU Simulator
</h2>
<ModeSelector/>
</div>


{/* -------- TABS -------- */}

<div className="flex gap-4 mb-4">

<button
onClick={()=>setTab("cpu")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="cpu" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
CPU
</button>

{mode==="developer" && (
<>
<button
onClick={()=>setTab("vm")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="vm" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
VM
</button>

<button
onClick={()=>setTab("binary")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="binary" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
Binary
</button>

<button
onClick={()=>setTab("pipeline")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="pipeline" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
Pipeline
</button>

<button
onClick={()=>setTab("flow")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="flow" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
Flow
</button>

<button
onClick={()=>setTab("isa")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="isa" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
ISA
</button>
</>
)}

<button
onClick={()=>setTab("guide")}
className={`px-4 py-2 rounded transition transform hover:scale-110 ${
tab==="guide" ? "bg-green-500 text-white shadow-lg" : "bg-gray-200"
}`}
>
Guide
</button>

</div>


{/* -------- VM -------- */}

{mode==="developer" && tab==="vm" && (
<div className="bg-white p-4 shadow rounded">
<VMEditor/>
</div>
)}


{/* -------- GUIDE -------- */}

{tab==="guide" && (
<div className="bg-white p-4 shadow rounded">
<Guidelines code={code}/>
</div>
)}


{/* -------- BINARY -------- */}

{mode==="developer" && tab==="binary" && (
<div className="bg-white p-4 shadow rounded">
<BinaryViewer key={state.binary?.length} binary={state.binary || []}/>
</div>
)}


{/* -------- PIPELINE -------- */}

{mode==="developer" && tab==="pipeline" && (
<div className="bg-white p-4 shadow rounded">
<Pipeline stage={state.stage}/>
</div>
)}


{/* -------- FLOW -------- */}

{mode==="developer" && tab==="flow" && (
<div className="bg-white p-4 shadow rounded">
<FlowGraph trace={state.trace}/>
</div>
)}


{/* -------- ISA -------- */}

{mode==="developer" && tab==="isa" && (
<div className="bg-white p-4 shadow rounded">
<ISAReference/>
</div>
)}


{/* -------- CPU DASHBOARD -------- */}

{tab==="cpu" && (

<div className={mode==="developer" ? "grid grid-cols-2 gap-4" : "grid grid-cols-1 gap-4"}>

{/* PROGRAM */}

<div className="bg-white shadow rounded p-4 flex flex-col">

<h2 className="font-bold mb-2 text-green-700">
Program
</h2>

<div className="h-48 overflow-auto border rounded">

<CodeEditor
code={code}
setCode={setCode}
pc={state.pc}
/>

</div>

<div className="mt-3">

<Controls
load={load}
run={run}
step={step}
reset={reset}
pause={pause}
speed={speed}
setSpeed={setSpeed}
/>

</div>

</div>


{/* REGISTERS */}

<div className="bg-white shadow rounded p-4">

<h2 className="font-bold mb-2 text-green-700">
Registers
</h2>

<Registers
registers={state.registers || []}
lastWrite={state.last_write}
/>

</div>


{/* RAM */}

{mode==="developer" && (

<div className="bg-white shadow rounded p-4">

<h2 className="font-bold mb-2 text-green-700">
RAM
</h2>

<Memory
memory={state.memory || []}
active={state.mem_access}
/>

</div>

)}


{/* STACK */}

{mode==="developer" && (

<div className="bg-white shadow rounded p-4">

<h2 className="font-bold mb-2 text-green-700">
Stack
</h2>

<StackView
memory={state.memory || []}
sp={state.sp}
/>

</div>

)}


{/* STATS */}

{mode==="developer" && (

<div className="bg-white shadow rounded p-4">

<h2 className="font-bold mb-2 text-green-700">
Stats
</h2>

<Stats stats={state.stats}/>

</div>

)}

</div>

)}

</div>

)

}