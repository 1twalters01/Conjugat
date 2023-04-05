import SettingsLinks from '../../components/settings/SettingsLinks'
import ThemeFunctionality from '../../components/settings/Theme/ThemeFunctionality'
import Authorization from '../../functions/Authorization'

function Themes() {
    Authorization.AuthRequired()
    return (
        <div className="rhs container">
            <div className="Header-spacer">
                <h1 className="text">Theme</h1>
            </div>
            
            <div className="form-spacer">
                <ThemeFunctionality />
            </div>
        </div>
    )
}


export default Themes