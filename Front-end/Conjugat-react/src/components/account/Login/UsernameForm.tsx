import { ChangeEvent, FormEvent, useState } from "react"
import { useDispatch } from "react-redux";
import { onConfirmedChange, onUsernameChange } from "../../../redux/slices/loginSlice";
import AxiosInstance from '../../../functions/AxiosInstance'
import handleText from "../../../functions/handlers/handleText";
import TextField from '../../Input fields/TextField'
import SubmitBtn from "../../Input fields/SubmitBtn";
import '../../../sass/Components/account/Login/UsernameForm.scss'
import { toast } from "react-toastify";


function UsernameForm({ onPageChange, }: { onPageChange:Function }) {
    const dispatch = useDispatch()
    const [username, setUsername] = useState('')

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/login/username/', {
            username: username
        })
        .then(res=>{
            dispatch(onConfirmedChange(res.data.confirmed))
            dispatch(onUsernameChange(res.data.username))
            onPageChange('password')
        })
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }
  
    return (
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
          <TextField
            id="username"
            value={ username }
            handleText={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setUsername)}
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