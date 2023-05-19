import { Link } from "react-router-dom"
import '../../sass/Components/settings/SettingsLinks.scss'

function SettingsLinks() {
    return (
        <div className="settings-links">
            <h1 className="text"><Link to='/settings/change-email/' className="text-gold-link">Settings</Link></h1>
            <div className="profile">
                <p className="profile-text header">Profile</p>
                <Link to='/settings/change-email/' className="text-blue-link">Change email</Link>
                <Link to='/settings/change-password/' className="text-blue-link">Change password</Link>
                <Link to='/settings/change-username/' className="text-blue-link">Change username</Link>
            </div>

            <div className="application">
                <p className="profile-text header">Application</p>
                <Link to='/settings/language/' className="text-blue-link">Language</Link>
                <Link to='/settings/font/' className="text-blue-link">Font</Link>
            </div>

            <div className="options">
                <p className="options-text header">Options</p>
                <Link to='/settings/premium' className="text-blue-link">Premium</Link>
                <Link to='/settings/themes' className="text-blue-link">Themes</Link>
                <Link to='/settings/two-factor-auth' className="text-blue-link">2FA</Link>
            </div>
        
            <div className="account">
                <p className="account-text header">Account</p>
                <Link to='/settings/logout-all/' className="text-blue-link">Logout all</Link>
                <Link to='/settings/reset-account' className="text-blue-link">Reset account</Link>
                <Link to='/settings/close-account' className="text-blue-link">Close account</Link>
            </div>
        </div>
    )
}

export default SettingsLinks