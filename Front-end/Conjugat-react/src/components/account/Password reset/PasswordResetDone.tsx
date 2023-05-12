import { Link } from 'react-router-dom'
import { getTranslation } from "../../../functions/getTranslation"
import { PasswordResetDoneTranslations } from '../../../content/account/PasswordReset'
import '../../../sass/Components/account/Password reset/PasswordResetDone.scss'

function PasswordResetDone({language}: {language:string}) {
    return(
        <div className='Password-reset-done-container'>
            <div className='paragraphs'>
                <p className='text'>{getTranslation(PasswordResetDoneTranslations, language, 'Text1')}</p>
                <p className='text'>{getTranslation(PasswordResetDoneTranslations, language, 'Text2')}</p>
            </div>
            <Link to="../login"><div className='login-btn strong-gold-btn'>Login</div></Link>
        </div>

    )
}

export default PasswordResetDone