import { FormEvent } from "react"

import AxiosInstance from '../../../functions/AxiosInstance'
import UsernameField from '../../Input fields/UsernameField'
import SubmitBtn from "../../Input fields/SubmitBtn";

import '../../../sass/Components/account/Login/UsernameForm.scss'
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "../../../redux/store";
import { onConfirmedChange, onIdChange } from "../../../redux/slices/loginSlice";

function UsernameForm({ onPageChange, }: { onPageChange:Function }) {
    const{ username } = useSelector((state: RootState) => state.login)
    const dispatch = useDispatch();

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/login/username/', {
          username: username
        })
        .then(res=>{
              onPageChange('password')
              dispatch(onConfirmedChange(res.data.confirmed))
              dispatch(onIdChange(res.data.id))
              console.log(res.data)
        })
        .catch(err=>{
          console.log(err.response.data.error)
        })
    }
  
    return(
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
          <UsernameField
              labelText = "Email or Username"
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