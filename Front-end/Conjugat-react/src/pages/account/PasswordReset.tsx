import { useState } from "react"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import PasswordResetDone from "../../components/account/Password reset/PasswordResetDone"
import PasswordResetForm from "../../components/account/Password reset/PasswordResetForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import '../../sass/pages/account/PasswordReset.scss'

function PasswordReset() {
    Authorization.NotAuthRequired()
    const [done, setDone] = useState(false)

    // if (done == false) {
    //     return (
    //         <div className="PasswordReset-container container">
    //             <div className="Header-spacer">
    //                 <Header />
    //             </div>
    //             

    //             <RegisterLinks />
    //             <div className="RegisterLinks-spacer"></div>
                
    //             <div className="form-width">
    //                 <PasswordResetForm onDoneChange={setDone} />
    //             </div>
    //             <div className="PasswordResetForm-spacer"></div>
    //         </div>
    //     )
    // }
    // else {
        return(
            <div className="PasswordReset-container container">
                <div className="Header-spacer">
                    <Header />
                </div>
                
                <PasswordResetDone />
            </div>
        )
    // }
}

export default PasswordReset