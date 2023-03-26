import { ChangeEvent, FormEvent } from "react"
import { toast } from "react-toastify"
import EmailField from "../../Input fields/EmailField"
import AxiosInstance from "../../../functions/AxiosInstance"
import SubmitBtn from "../../Buttons/SubmitBtn"


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
        toast.error(err.response.data.error)
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

        <SubmitBtn
          value="Unsubscribe"
        />
        </form>
      </div>
    )
}

export default UnsubscribeForm