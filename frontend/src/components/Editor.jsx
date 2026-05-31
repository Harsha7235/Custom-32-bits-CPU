import Editor from "@monaco-editor/react"
import { useRef, useEffect } from "react"

export default function CodeEditor({ code, setCode, pc }) {

const editorRef = useRef(null)
const decorationsRef = useRef([])   // <-- THIS FIXES YOUR ERROR

function handleMount(editor) {
editorRef.current = editor
}

useEffect(() => {

if (!editorRef.current) return
if (pc === undefined || pc < 0) return

const model = editorRef.current.getModel()

if (!model) return

const lineCount = model.getLineCount()

if (pc + 1 > lineCount) return

decorationsRef.current =
editorRef.current.deltaDecorations(
decorationsRef.current,
[
{
range:{
startLineNumber: pc + 1,
startColumn:1,
endLineNumber: pc + 1,
endColumn:1
},
options:{
isWholeLine:true,
className:"currentInstruction"
}
}
]
)

}, [pc])

return (

<div className="border border-gray-400 bg-white rounded p-2">

<div className="font-semibold text-gray-700 mb-2">
Program Code
</div>

<Editor
height="220px"
theme="light"
value={code}
onChange={(v)=>setCode(v)}
onMount={handleMount}

options={{
fontSize:14,
lineNumbers:"on",
minimap:{enabled:false},
automaticLayout:true,
scrollBeyondLastLine:false,
placeholder:"Write ASM code here...."
}}
/>

</div>

)

}