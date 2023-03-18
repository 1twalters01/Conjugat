import { ChangeEvent, FormEvent, useState} from "react"
import PasswordField from "../../Input fields/PasswordField"
import TotpField from "../../Input fields/TotpField"
import SubmitBtn from "../../Input fields/SubmitBtn"
import AxiosInstance from "../../../functions/AxiosInstance"
import { useDispatch } from "react-redux"
import { onConfirmedChange } from "../../../redux/slices/loginSlice"

function QrForm({setDone}: {setDone:Function}) {
    const dispatch = useDispatch()
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/two-factor-auth/', {
        password: password,
        totp: totp,
      })
      .then(res=>{
        setDone(true)
        console.log(res.data.confirmed, res.data.success)
        dispatch(onConfirmedChange(res.data.confirmed))
      })
      .catch(err => {
        console.log(err.response.data.error)
      })
    }
  
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handleTotp(e:ChangeEvent<HTMLInputElement>) {
        if (isNaN(+e.target.value) == false){
          setTotp(e.target.value)
        }
    }
  
    return(
      <form onSubmit={(e) => submit(e)}>
          <PasswordField
            id="password"
            password={password}
            handlePassword={(e:ChangeEvent<HTMLInputElement>) => handlePassword(e)}
            labelText="Password"
          />
  
          <TotpField
          totp={totp}
          handleTotp={(e:ChangeEvent<HTMLInputElement>) => handleTotp(e)}
          labelText="Totp"
          />
  
          <SubmitBtn
            value="Submit"
          />
      </form>
    )
}

export default QrForm