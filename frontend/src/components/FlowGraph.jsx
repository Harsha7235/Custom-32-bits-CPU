export default function FlowGraph({trace}){

if(!trace || trace.length===0){
return <div>No execution trace yet</div>
}

return(

<div className="space-y-2">

{trace.map((t,i)=>(

<div
key={i}
className="border p-2 rounded bg-gray-50"
>

{t}

</div>

))}

</div>

)

}