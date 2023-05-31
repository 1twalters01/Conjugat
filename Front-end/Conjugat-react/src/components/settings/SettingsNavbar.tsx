import { Link } from "react-router-dom"
import { getTranslation } from "../../functions/getTranslation"
import { NewsletterResponseTranslation, SettingsNavbarTranslation } from '../../content/newsletter/Subscribe'
import '../../sass/Components/settings/SettingsNavbar.scss'

function SettingsNavbar({language}: {language:string}) {
    return (
        <div className="Settings-navbar">
            <div className="logo">
                <h2><Link to='/home/' className='text'>{getTranslation(SettingsNavbarTranslation, language, 'Conjugat')}</Link></h2>
            </div>

            <div className="settings">
                <Link to='/test/' className="text-gold-link">{getTranslation(SettingsNavbarTranslation, language, 'Test')}</Link>
            </div>
            
            <div className="newsletter">
                <Link to='/newsletter/' className="text-gold-link">{getTranslation(SettingsNavbarTranslation, language, 'Newsletter')}</Link>
            </div>

            <div className="settings">
                <Link to='/settings/change-email/' className="text-gold-link">{getTranslation(SettingsNavbarTranslation, language, 'Settings')}</Link>
            </div>

            <div className="Logout">
                <Link to='/account/logout/' className="text-gold-link">{getTranslation(SettingsNavbarTranslation, language, 'Logout')}</Link>
            </div>
        </div>
    )
}

export default SettingsNavbar