import { useEffect, useState } from "react"

export default function Loading({ onFinish }){

const [progress,setProgress] = useState(0)

useEffect(()=>{

let p = 0

const interval = setInterval(()=>{

p += Math.random()*15

if(p >= 100){
p = 100
clearInterval(interval)

setTimeout(()=>{
onFinish()
},500)
}

setProgress(p)

},120)

},[])

return(

<div className="relative w-screen h-screen overflow-hidden bg-black">

{/* Full screen background image */}

<img
src="/cpu.png"
className="absolute inset-0 w-full h-full object-cover opacity-40"
/>

{/* dark overlay */}

<div className="absolute inset-0 bg-black/50"/>

{/* loading content */}

<div className="relative z-10 flex flex-col items-center justify-center h-full text-green-400 font-mono">

<h1 className="text-4xl mb-6 tracking-widest">
CPU32 INITIALIZING
</h1>

<div className="w-96 h-3 bg-gray-800 rounded overflow-hidden">

<div
className="h-full bg-green-400 transition-all duration-200"
style={{width:progress+"%"}}
/>

</div>

<p className="mt-4 text-lg">
Booting system... {Math.floor(progress)}%
</p>

</div>

</div>

)

}