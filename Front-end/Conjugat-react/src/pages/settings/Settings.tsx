import { Outlet } from "react-router-dom"
import SettingsLinks from "../../components/settings/SettingsLinks"
import SettingsNavbar from "../../components/settings/SettingsNavbar"
import '../../sass/pages/settings/Settings.scss'

function Settings() {
    return (
        <div className="Settings-container">
            <div className="Settings-navbar-container container">
                <SettingsNavbar />
            </div>
            
            <div className="Settings-main-container">
                <div className="lhs container">
                    <SettingsLinks />
                </div>
                
                <Outlet />
                
            </div>
        </div>
    )
}

export default Settings