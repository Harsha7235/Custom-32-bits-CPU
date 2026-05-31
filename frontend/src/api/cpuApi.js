import axios from "axios"

const API = "http://127.0.0.1:8000"

// ---------------- CPU ----------------

export const loadProgram = (code)=>{
return axios.post(`${API}/load`,{code})
}

export const runProgram = ()=>{
return axios.post(`${API}/run`)
}

export const stepProgram = ()=>{
return axios.post(`${API}/step`)
}

export const resetCPU = ()=>{
return axios.post(`${API}/reset`)
}

// ---------------- VM ----------------

export const translateVM = (code)=>{
return axios.post(`${API}/vm`,{code})
}

// ---------------- PERFORMANCE ----------------

export const getStats = ()=>{
return axios.get(`${API}/stats`)
}