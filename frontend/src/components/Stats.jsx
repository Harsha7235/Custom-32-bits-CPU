export default function Stats({stats}){

if(!stats) return null

return(

<div className="border p-4 border-green-500">

<h2 className="text-xl">CPU Stats</h2>

<div>Instructions: {stats.instructions}</div>
<div>Cycles: {stats.cycles}</div>
<div>Memory Reads: {stats.reads}</div>
<div>Memory Writes: {stats.writes}</div>
<div>Peak Stack: {stats.peak_stack}</div>

</div>

)

}