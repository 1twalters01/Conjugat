import { useState } from "react"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"

import RegisterDone from "../../components/account/Register/RegisterDone"
import RegisterForm from "../../components/account/Register/RegisterForm"

function Register() {
  Authorization.NotAuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <Header />
        <h1>Register</h1>
        
        <RegisterForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else{
    return (
      <div>
        <Header />
        <h1>Register</h1>
        
        <RegisterDone />
      </div>
    )
  }
}

export default Register