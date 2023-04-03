import SettingsLinks from "../../components/settings/SettingsLinks"
import '../../sass/pages/settings/ResetAccount.scss'

function ResetAccount() {
    return (
        <div className="Reset-account-container">
            <div className="lhs container">
                <SettingsLinks />
            </div>
            
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">Reset account</h1>
                </div>
                
                <div className="form-spacer">
                    
                </div>
            </div>
        </div>
    )
}

export default ResetAccount