import { Link } from 'react-router-dom'
import { getTranslation } from "../../../functions/getTranslation"
import { PasswordChangeTokenDoneTranslations } from "../../../content/account/PasswordResetToken"
import '../../../sass/Components/account/Password reset token/PasswordResetTokenDone.scss'

function PasswordResetTokenDone({language}: {language:string}){
    return(
        <div className="PasswordResetTokenDone-response">
            <p className="para text">{getTranslation(PasswordChangeTokenDoneTranslations, language, 'Text')}</p>
            <Link to="../login"><div className="login-btn strong-gold-btn">{getTranslation(PasswordChangeTokenDoneTranslations, language, 'Login')}</div></Link>
        </div>
    )
}

export default PasswordResetTokenDone