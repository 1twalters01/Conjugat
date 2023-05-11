import { useState } from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import RegisterDoneFalse from "../../components/account/Register/RegisterDoneFalse"
import RegisterDoneTrue from "../../components/account/Register/RegisterDoneTrue"
import RegisterForm from "../../components/account/Register/RegisterForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import '../../sass/pages/account/Register.scss'

function Register() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)

    const [done, setDone] = useState(false)
    const [returnedEmail, setReturnedEmail] = useState(null)

    if (done == false) {
        return (
            <div className="Register-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>

                
                <div className="RegisterLinks-spacer">
                    <RegisterLinks />
                </div>
                
                <div className="form-width">
                    <RegisterForm
                    onDoneChange={setDone}
                    setReturnedEmail={setReturnedEmail}
                    />
                </div>
                
                <div className="RegisterForm-spacer"></div>
            </div>

        )
    }
    else {
        if (returnedEmail == true){
            return (
                <div className="Register-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>

                    <div className="Register-done-spacer">
                        <RegisterDoneTrue />
                    </div>
                </div>
              )
        }
        else {
            return (
                <div className="Register-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>
                    
                    <div className="Register-done-spacer">
                         <RegisterDoneFalse />
                    </div>
                  
                </div>
              )
        }
        
    }
}

export default Register