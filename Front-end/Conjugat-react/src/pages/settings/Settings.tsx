import { Outlet, useNavigate } from "react-router-dom"
import SettingsLinks from "../../components/settings/SettingsLinks"
import SettingsNavbar from "../../components/settings/SettingsNavbar"
import '../../sass/pages/settings/Settings.scss'
import { useEffect } from "react"
import Authorization from "../../functions/Authorization"

function Settings() {
    Authorization.AuthRequired()
    const navigate = useNavigate()
    const base = 'http://localhost:5000/'
    useEffect(() => {
        if (window.location.href == base + 'settings/' || window.location.href == base + 'settings') {
        navigate('change-email/'), []
        }
    })
    
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