import { FormEvent, useCallback } from "react"

import AxiosInstance from '../../functions/AxiosInstance'
import UsernameField from '../../Input fields/UsernameField'

function UsernameForm({username, onPageChange, onUsernameChange, onIdChange, onConfirmedChange}: {username:string, onPageChange:Function, onUsernameChange:Function, onIdChange:Function, onConfirmedChange:Function}) {
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/login/username/', {
          username: username
        })
        .then(res=>{
              onPageChange('password')
              onConfirmedChange(res.data.confirmed)
              onIdChange(res.data.id)
        })
        .catch(err=>{
          console.log(err.response.data.error)
        })
    }
  
    const handleUsername = useCallback((e: { target: { value: string } }) => {
        onUsernameChange(e.target.value)
    }, [onUsernameChange])
  
    return(
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
          <UsernameField
              username = {username}
              handleUsername = {handleUsername}
          />
  
          <div className="submit">
              <input type="submit" className="strong-btn" value="Continue" />
          </div>
        </form>
      </div>
    )
}

export default UsernameForm