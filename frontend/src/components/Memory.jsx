export default function Memory({memory = [], active}){

return(

<div className="grid grid-cols-4 gap-2">

{memory.map((m,i)=>{

const highlight = i === active

return(

<div
key={i}
className={`border p-1 text-sm rounded
${highlight ? "bg-yellow-300 font-bold" : ""}
`}
>

{i}: {Array.isArray(m) ? m.join(" ") : m}

</div>

)

})}

</div>

)

}