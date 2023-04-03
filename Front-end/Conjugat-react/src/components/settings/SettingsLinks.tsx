import { Link } from "react-router-dom"
import '../../sass/Components/settings/SettingsLinks.scss'

function SettingsLinks() {
    return (
        <div className="settings-links">
            <h1 className="text">Settings</h1>
            <div className="profile">
                <p className="profile-text header">Profile</p>
                <Link to='../change-email/' className="text-blue-link">Change email</Link>
                <Link to='../change-password/' className="text-blue-link">Change password</Link>
                <Link to='../change-username/' className="text-blue-link">Change username</Link>
            </div>

            <div className="options">
                <p className="options-text header">Options</p>
                <Link to='../premium' className="text-blue-link">Premium</Link>
                <Link to='../themes' className="text-blue-link">Themes</Link>
                <Link to='../two-factor-auth' className="text-blue-link">2FA</Link>
            </div>
        
            <div className="account">
                <p className="account-text header">Account</p>
                <Link to='../logout-all/' className="text-blue-link">Logout all</Link>
                <Link to='../reset-account' className="text-blue-link">Reset account</Link>
                <Link to='../close-account' className="text-blue-link">Close account</Link>
            </div>
        </div>
    )
}

export default SettingsLinks