import {useState,useEffect} from "react"
import axios from "axios"

export default function Guidelines({code}){

const [analysis,setAnalysis] = useState(null)

useEffect(()=>{

async function analyze(){

const res = await axios.post(
"http://127.0.0.1:8000/analyze",
{code}
)

setAnalysis(res.data)

}

analyze()

},[code])


if(!analysis) return null


if(analysis.status==="good"){

return(

<div className="p-3 bg-green-100 border border-green-400">

✅ Code looks correct

</div>

)

}


return(

<div className="p-3 bg-yellow-100 border border-yellow-400">

{analysis.issues.map((i,idx)=>(
<div key={idx}>⚠ {i}</div>
))}

</div>

)

}