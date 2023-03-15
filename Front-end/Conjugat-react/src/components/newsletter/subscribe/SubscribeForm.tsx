import { ChangeEvent, FormEvent, useState} from "react"
import EmailField from "../../Input fields/EmailField"
import TextField from "../../Input fields/TextField";
import AxiosInstance from "../../../functions/AxiosInstance"

function SubscribeForm({setDone, email, setEmail}: {setDone:Function, email:string, setEmail:Function}) {
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [languages, setLanguage] = useState<string[]>([]);
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Unauthorised
      .post('/newsletter/subscribe/', {
        email: email,
        first_name: firstName,
        last_name: lastName,
        languages: languages,
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
    function handleFirstName(e:ChangeEvent<HTMLInputElement>) {
      setFirstName(e.target.value)
    }
    function handleLastName(e:ChangeEvent<HTMLInputElement>) {
      setLastName(e.target.value)
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
                handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleEmail(e)}
              />
              
              <TextField
                id={"firstName"}
                labelText="First name"
                required={false}
                handleText={(e:ChangeEvent<HTMLInputElement>) => handleFirstName(e)}
                value={firstName}
              />
  
              <TextField
                id={"lastName"}
                labelText="Last name"
                required={false}
                handleText={(e:ChangeEvent<HTMLInputElement>) => handleLastName(e)}
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
              <button>Submit</button>
          </form>
      </div>
    )
}

export default SubscribeForm