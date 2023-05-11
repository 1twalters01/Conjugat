import { ChangeEvent, FormEvent, useState } from "react"
import { useDispatch } from "react-redux";
import { toast } from "react-toastify";
import { onConfirmedChange, onUsernameChange } from "../../../redux/slices/loginSlice";
import AxiosInstance from '../../../functions/AxiosInstance'
import handleText from "../../../functions/handlers/handleText";
import TextField from '../../Input fields/TextField'
import SubmitBtn from "../../Buttons/SubmitBtn";
import { getTranslation } from "../../../functions/getTranslation"
import { LabelTextTranslation } from "../../../content/account/Login"
import '../../../sass/Components/account/Login/UsernameForm.scss'


function UsernameForm({ language, onPageChange, }: { language:string, onPageChange:Function }) {
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
              <div className="username-spacer">
                  <TextField
                    id="username"
                    value={ username }
                    handleText={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setUsername)}
                    labelText = {getTranslation(LabelTextTranslation, language, 'Label')}
                    required={true}
                  />
              </div>

              <SubmitBtn
                value={getTranslation(LabelTextTranslation, language, 'Label')}
                style= 'strong-gold-btn'
              />
          </form>
      </div>
    )
}

export default UsernameForm