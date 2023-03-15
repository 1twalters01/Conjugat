import { ChangeEvent, FormEvent, useState } from "react"

import AxiosInstance from '../../../functions/AxiosInstance'
import TextField from '../../Input fields/TextField'
import SubmitBtn from "../../Input fields/SubmitBtn";

import '../../../sass/Components/account/Login/UsernameForm.scss'
import { useDispatch } from "react-redux";
import { onConfirmedChange, onIdChange, onUsernameChange } from "../../../redux/slices/loginSlice";

function UsernameForm({ onPageChange, }: { onPageChange:Function }) {
    const [username, setUsername] = useState('')
    const dispatch = useDispatch();

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/login/username/', {
          username: username
        })
        .then(res=>{
            dispatch(onUsernameChange(res.data.username))
            dispatch(onConfirmedChange(res.data.confirmed))
            dispatch(onIdChange(res.data.id))
            onPageChange('password')
        })
        .catch(err=>{
            console.log(err.response.data.error)
        })
    }
    
    function handleUsername(e:ChangeEvent<HTMLInputElement>) {
      setUsername(e.target.value)
    }
  
    return (
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
          <TextField
              id="username"
              value={ username }
              handleText={(e:ChangeEvent<HTMLInputElement>) => handleUsername(e)}
              labelText = "Email or Username"
              required={true}
          />
          <div className="username-spacer"></div>
  
          <SubmitBtn
            value="Continue"
          />
        </form>
      </div>
    )
}

export default UsernameForm