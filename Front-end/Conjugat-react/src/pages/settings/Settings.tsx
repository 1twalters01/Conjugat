import { Outlet, useNavigate } from "react-router-dom"
import SettingsLinks from "../../components/settings/SettingsLinks"
import SettingsNavbar from "../../components/settings/SettingsNavbar"
import { useEffect } from "react"
import Authorization from "../../functions/Authorization"
import '../../sass/pages/settings/Settings.scss'
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"

function Settings() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const navigate = useNavigate()
    const base = import.meta.env.VITE_CLIENT_URL as string
    useEffect(() => {
        if (window.location.href == base + 'settings/' || window.location.href == base + 'settings') {
        navigate('change-email/'), []
        }
    })
    
    return (
        <div className="Settings-container">
            <div className="Settings-navbar-container container">
                <SettingsNavbar language={language} />
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