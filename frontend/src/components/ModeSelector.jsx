import axios from "axios"

const API = "http://127.0.0.1:8000"

export default function ModeSelector(){

async function setUser(){

await axios.post(`${API}/mode`,{mode:"user"})
window.location.reload()

}

async function setDev(){

await axios.post(`${API}/mode`,{mode:"developer"})
window.location.reload()

}

return(

<div style={{display:"flex",gap:"10px"}}>

<button
style={{background:"#3b82f6",color:"white",padding:"6px 12px"}}
onClick={setUser}
>
User Mode
</button>

<button
style={{background:"#10b981",color:"white",padding:"6px 12px"}}
onClick={setDev}
>
Developer Mode
</button>

</div>

)

}