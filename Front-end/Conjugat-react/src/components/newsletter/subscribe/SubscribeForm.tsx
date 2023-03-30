import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify";
import EmailField from "../../Input fields/EmailField"
import TextField from "../../Input fields/TextField";
import SelectField from "../../Input fields/SelectField";
import AxiosInstance from "../../../functions/AxiosInstance"
import SubmitBtn from "../../Buttons/SubmitBtn";
import '../../../sass/Components/newsletter/subscribe/SubscribeForm.scss'

function SubscribeForm({setDone, email, setEmail}: {setDone:Function, email:string, setEmail:Function}) {
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [languages, setLanguage] = useState<string[]>([]);
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Unauthorised
      .post('/newsletter/unsubscribe/', {
        email: email,
        first_name: firstName,
        last_name: lastName,
        languages: languages,
      })
      .then(res=>{
        setDone(true)
      })
      .catch(err=>{
        toast.error(err.response.data.error)
      })
    }
  
    function changeLanguage(e:ChangeEvent<HTMLSelectElement>) {
      if (languages.includes(e.target.value)) {
        setLanguage(languages.filter(languages => languages !== e.target.value ))
      }
      else {
        setLanguage([...languages, e.target.value])
      }
    }
  
    return (
      <div className="Subscribe-form">
        <form onSubmit={(e) => submit(e)}>
            <div className="text-spacer">
                <EmailField
                  id='email'
                  email={email}
                  labelText="Email"
                  handleEmail={(e:ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
                  required={true}
                />
            </div>
                
            <div className="text-spacer">
                <TextField
                  id={"firstName"}
                  labelText="First name"
                  required={true}
                  handleText={(e:ChangeEvent<HTMLInputElement>) => setFirstName(e.target.value)}
                  value={firstName}
                />
            </div>
    
            <div className="text-spacer">
                <TextField
                  id={"lastName"}
                  labelText="Last name (optional)"
                  required={false}
                  handleText={(e:ChangeEvent<HTMLInputElement>) => setLastName(e.target.value)}
                  value={lastName}
                />
            </div>
                
            <div className="select-spacer">
                <SelectField
                languages={languages}
                changeLanguage={changeLanguage}
                />
            </div>
                

              <SubmitBtn
                value="Submit"
                style="strong-gold-btn"
              />
          </form>
      </div>
    )
}

export default SubscribeForm