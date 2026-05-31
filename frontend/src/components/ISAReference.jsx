export default function ISAReference(){

const instructions = [

{
name:"ADD",
format:"ADD r1 r2",
binary:"00000001",
desc:"Add register r2 to r1"
},

{
name:"SUB",
format:"SUB r1 r2",
binary:"00000010",
desc:"Subtract r2 from r1"
},

{
name:"MUL",
format:"MUL r1 r2",
binary:"00000011",
desc:"Multiply registers"
},

{
name:"DIV",
format:"DIV r1 r2",
binary:"00000100",
desc:"Divide registers"
},

{
name:"MOV",
format:"MOV r1 r2",
binary:"00000101",
desc:"Copy register value"
},

{
name:"MOVI",
format:"MOVI r value",
binary:"00000110",
desc:"Load immediate value"
},

{
name:"PUSH",
format:"PUSH r",
binary:"00000111",
desc:"Push register to stack"
},

{
name:"POP",
format:"POP r",
binary:"00001000",
desc:"Pop stack to register"
},

{
name:"LOADG",
format:"LOADG r addr",
binary:"00001001",
desc:"Load global memory"
},

{
name:"STOREG",
format:"STOREG r addr",
binary:"00001010",
desc:"Store to memory"
},

{
name:"JMP",
format:"JMP label",
binary:"00001011",
desc:"Jump to label"
},

{
name:"JZ",
format:"JZ r label",
binary:"00001100",
desc:"Jump if register zero"
},

{
name:"CALL",
format:"CALL label",
binary:"00001101",
desc:"Call function"
},

{
name:"RET",
format:"RET",
binary:"00001110",
desc:"Return from function"
},

{
name:"HALT",
format:"HALT",
binary:"11111111",
desc:"Stop CPU execution"
}

]

return(

<div className="grid grid-cols-3 gap-4">

{instructions.map((i,index)=>(

<div
key={index}
className="border rounded p-4 bg-white shadow"
>

<h2 className="font-bold text-green-700">
{i.name}
</h2>

<p className="text-sm mt-2">
<b>Format:</b> {i.format}
</p>

<p className="text-sm">
{i.desc}
</p>

<p className="text-xs font-mono mt-2 text-blue-600">
Opcode: {i.binary}
</p>

</div>

))}

</div>

)

}