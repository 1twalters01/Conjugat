import { useState } from "react"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import RegisterDone from "../../components/account/Register/RegisterDone"
import RegisterForm from "../../components/account/Register/RegisterForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import '../../sass/pages/account/Register.scss'

function Register() {
    Authorization.NotAuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
          <div className="Register-container">
            <div className="Header-spacer-top"></div>
            <Header />
            <div className="Header-spacer-bottom"></div>

            <RegisterLinks />
            <div className="RegisterLinks-spacer"></div>
            
            <RegisterForm
              onDoneChange={setDone}
            />
            <div className="RegisterForm-spacer"></div>
          </div>
        )
    }
    else {
        return (
          <div className="Register-done-container">
            <div className="Header-spacer-top"></div>
            <Header />
            <div className="Header-spacer-bottom"></div>

            <h1>Register</h1>
            
            <RegisterDone />
          </div>
        )
    }
}

export default Register