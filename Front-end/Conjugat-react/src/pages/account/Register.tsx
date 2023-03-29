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
            <div className="Login-body body">
                <div className="Register-container container">
                    <div className="Header-spacer">
                        <Header />
                    </div>

                    
                    <div className="RegisterLinks-spacer">
                        <RegisterLinks />
                    </div>
                    
                    <div className="form-width">
                        <RegisterForm
                        onDoneChange={setDone}
                        />
                    </div>
                    
                    <div className="RegisterForm-spacer"></div>
                </div>
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