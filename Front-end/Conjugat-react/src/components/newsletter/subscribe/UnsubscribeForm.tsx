import { ChangeEvent, FormEvent } from "react"
import EmailField from "../../Input fields/EmailField"
import AxiosInstance from "../../../functions/AxiosInstance"

function UnsubscribeForm({setDone, email, setEmail}: {setDone:Function, email:string, setEmail:Function}) {
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Unauthorised
      .post('/newsletter/unsubscribe/', {
        email: email,
      })
      .then(res=>{
        setDone(true)
        console.log(res.data)
      })
      .catch(err=>{
        console.log(err.response.data.error)
      })
    }
    
    function handleEmail(e:ChangeEvent<HTMLInputElement>) {
      setEmail(e.target.value)
    }
  
    return (
      <div>
        <form onSubmit={(e) => submit(e)}>
            <EmailField
              id='email'
              email={email}
              labelText="Email"
              handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleEmail(e)}
            />
        </form>
        <button>Submit</button>
      </div>
    )
}

export default UnsubscribeForm