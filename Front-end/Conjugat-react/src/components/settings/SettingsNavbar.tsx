import { Link } from "react-router-dom"
import '../../sass/Components/settings/SettingsNavbar.scss'

function SettingsNavbar() {
    return (
        <div className="Settings-navbar">
            <div className="logo">
                <h2><Link to='/home/' className='text'>Conjugat</Link></h2>
            </div>

            <div className="settings">
                <Link to='/verbs/test' className="text-gold-link">Test</Link>
            </div>
            
            <div className="newsletter">
                <Link to='/newsletter/' className="text-gold-link">Newsletter</Link>
            </div>

            <div className="settings">
                <Link to='/settings/' className="text-gold-link">Settings</Link>
            </div>

            <div className="Logout">
                <Link to='/account/logout/' className="text-gold-link">Logout</Link>
            </div>
        </div>
    )
}

export default SettingsNavbar