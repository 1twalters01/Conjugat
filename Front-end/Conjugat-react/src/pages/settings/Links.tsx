import { Link } from "react-router-dom"

function SettingsLinks() {
    return (
        <div className="settings-links">
            <div className="options">
                <p className="options-text text">Options</p>
                <Link to='../premium'></Link>
                <Link to='../themes'></Link>
                <Link to='../two-factor-auth'></Link>
            </div>

            <div className="profile">
                <p className="profile-text text">Profile</p>
                <Link to='../change-email/'></Link>
                <Link to='../change-password/'></Link>
                <Link to='../change-username/'></Link>
            </div>
        
            <div className="account-text text">
                <p className="account-text text">Account</p>
                <Link to='../logout-all/'></Link>
                <Link to='../reset-account'></Link>
                <Link to='../close-account'></Link>
            </div>
        </div>
    )
}

export default SettingsLinks