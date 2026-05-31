import { useState } from "react"
import Editor from "@monaco-editor/react"
import { translateVM } from "../api/cpuApi"

export default function VMEditor(){

const [vm,setVM] = useState("")
const [asm,setASM] = useState([])

async function translate(){

const res = await translateVM(vm)

setASM(res.data.assembly)

}

return(

<div className="space-y-3">

<h2 className="font-bold text-green-600">VM Code</h2>

<Editor
height="220px"
theme="light"
value={vm}
onChange={(v)=>setVM(v)}
options={{
fontSize:14,
minimap:{enabled:false},
placeholder:"Write VM code here..."
}}
/>

<button
onClick={translate}
className="bg-blue-500 text-white px-4 py-2 rounded"
>
Translate
</button>

<div className="border rounded p-2 bg-gray-50">

<h3 className="font-semibold mb-2">
Generated ASM
</h3>

<pre>
{asm.join("\n")}
</pre>

</div>

</div>

)

}