export default function StackView({memory=[],sp=0}){

return(

<div className="grid grid-cols-1 gap-1">

{memory.slice(0,20).map((v,i)=>{

const isSP = i === sp

return(

<div
key={i}
className={`border p-1 rounded text-sm
${isSP ? "bg-red-300 font-bold" : ""}
`}
>

{i}: {v} {isSP ? "<-- SP" : ""}

</div>

)

})}

</div>

)

}