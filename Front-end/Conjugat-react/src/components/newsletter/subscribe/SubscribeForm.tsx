import { ChangeEvent, FormEvent, useState} from "react"
import EmailField from "../../Input fields/EmailField"
import TextField from "../../Input fields/TextField";
import AxiosInstance from "../../../functions/AxiosInstance"
import SubmitBtn from "../../Input fields/SubmitBtn";

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
        console.log(err.response.data.error)
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
      <div>
        <form onSubmit={(e) => submit(e)}>
              <EmailField
                id='email'
                email={email}
                labelText="Email"
                handleEmail={(e:ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
              />
              
              <TextField
                id={"firstName"}
                labelText="First name"
                required={false}
                handleText={(e:ChangeEvent<HTMLInputElement>) => setFirstName(e.target.value)}
                value={firstName}
              />
  
              <TextField
                id={"lastName"}
                labelText="Last name"
                required={false}
                handleText={(e:ChangeEvent<HTMLInputElement>) => setLastName(e.target.value)}
                value={lastName}
              />
              
              <div>
                <label htmlFor="languages">Languages</label>
                <select name="languages" id="languages" value={languages || []} onChange={(e) => changeLanguage(e)} multiple={true}>
                  <option value="English">English</option>
                  <option value="French">French</option>
                  <option value="Italian">Italian</option>
                  <option value="Portuguese">Portuguese</option>
                  <option value="Spanish">Spanish</option>
                </select>
              </div>

              <SubmitBtn
                value="Submit"
              />
          </form>
      </div>
    )
}

export default SubscribeForm