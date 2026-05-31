export default function Pipeline({stage}){

const stages=["FETCH","DECODE","EXECUTE","MEMORY","WRITEBACK"]

return(

<div>

<h2>Pipeline</h2>

{stages.map(s=>(
<span
style={{
color: stage===s?"red":"black",
marginRight:"10px"
}}
>
{s}
</span>
))}

</div>

)

}