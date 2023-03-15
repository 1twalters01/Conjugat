import { FormEvent } from "react"
import AxiosInstance from "../../../functions/AxiosInstance";

function ThemeFunctionality() {
    function submitDark(e:FormEvent<HTMLDivElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/themes/', {
        choice: 'Dark'
      })
      .then(res=>{
        // location.reload()
        console.log(res.data)
      })
      .catch(err=>{
        console.log(err.response.data)
      })
    }
    
    function submitLight(e:FormEvent<HTMLDivElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/themes/', {
        choice: 'Light'
      })
      .then(res=>{
        // location.reload()
        console.log(res.data)
      })
      .catch(err=>{
        console.log(err.response.data)
      })
    }
  
    return(
      <div>
        <div onClick={(e) => submitDark(e)} style={{height: '200px', width: '200px', background: 'black'}}>
        
        </div>
        <div onClick={(e) => submitLight(e)} style={{height: '200px', width: '200px', background: 'yellow'}}>
        
        </div>
      </div>
    )
}

export default ThemeFunctionality