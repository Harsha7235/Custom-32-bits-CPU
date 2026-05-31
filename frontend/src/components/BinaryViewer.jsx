export default function BinaryViewer({ binary }) {

if(!binary || binary.length === 0){
return <div>No binary generated yet</div>
}

return (

<div className="font-mono text-sm">

{/* HEADER */}

<div className="grid grid-cols-4 gap-2 mb-2 font-bold text-gray-700">
<div>OPCODE (8)</div>
<div>R1 (4)</div>
<div>R2 (4)</div>
<div>IMM / ADDR (16)</div>
</div>

{binary.map((b,i)=>{

const opcode = b.slice(0,8)
const r1 = b.slice(8,12)
const r2 = b.slice(12,16)
const imm = b.slice(16,32)

return(

<div
key={i}
className="grid grid-cols-4 gap-2 border p-2 mb-1 bg-white rounded shadow"
>

<div className="text-red-600">{opcode}</div>

<div className="text-blue-600">{r1}</div>

<div className="text-green-600">{r2}</div>

<div className="text-purple-600">{imm}</div>

</div>

)

})}

</div>

)

}