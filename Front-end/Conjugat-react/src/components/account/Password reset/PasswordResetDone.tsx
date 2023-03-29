import { Link } from 'react-router-dom'
import '../../../sass/Components/account/Password reset/PasswordResetDone.scss'

function PasswordResetDone() {
    return(
        <div className='Password-reset-done-container'>
            <div className='paragraphs'>
                <p className='text'>We've emailed you instructions for setting your password.</p>
                <p className='text'>If you don't receive an email, please make sure you've entered the address you registered with.</p>
            </div>
            <Link to="../login"><div className='login-btn strong-gold-btn'>Login</div></Link>
        </div>

    )
}

export default PasswordResetDone