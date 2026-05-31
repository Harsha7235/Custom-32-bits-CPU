export default function Registers({registers = [], lastWrite}){

return(

<div className="grid grid-cols-4 gap-2">

{registers.length === 0 && (
<div className="text-gray-400">Registers empty</div>
)}

{registers.map((r,i)=>{

const active = i === lastWrite

return(

<div
key={i}
className={`border p-2 rounded text-center
${active ? "bg-green-300" : ""}
`}
>

R{i}: {r}

</div>

)

})}

</div>

)

}