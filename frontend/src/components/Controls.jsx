export default function Controls({
load,run,step,reset,pause,speed,setSpeed
}){

return(

<div className="mt-4">

<div className="flex gap-3 mb-3">

<button onClick={load} className="px-4 py-2 bg-green-500 text-white rounded">
LOAD
</button>

<button onClick={run} className="px-4 py-2 bg-blue-500 text-white rounded">
RUN
</button>

<button onClick={step} className="px-4 py-2 bg-yellow-500 text-white rounded">
STEP
</button>

<button onClick={pause} className="px-4 py-2 bg-purple-500 text-white rounded">
PAUSE
</button>

<button onClick={reset} className="px-4 py-2 bg-red-500 text-white rounded">
RESET
</button>

</div>

<div className="flex items-center gap-3">

<label className="text-gray-700">
Speed
</label>

<input
type="range"
min="1"
max="10"
value={speed}
onChange={(e)=>setSpeed(Number(e.target.value))}
/>

<span className="text-gray-700">
{speed}x
</span>

</div>

</div>

)

}