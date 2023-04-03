import Authorization from '../../functions/Authorization'
import RetrievePremiumStatus from "../../components/settings/premium/RetrievePremiumStatus"
import SettingsLinks from '../../components/settings/SettingsLinks'
import '../../sass/pages/settings/Premium.scss'

function Premium() {
  Authorization.AuthRequired()
  return (
      <div className="Theme-container">
          <div className="lhs container">
              <SettingsLinks />
          </div>
          
          <div className="rhs container">
              <div className="Header-spacer">
                  <h1 className="text">Premium</h1>
              </div>
              
              <div className="form-spacer">
              <RetrievePremiumStatus />
              </div>
          </div>
      </div>
  )
}



export default Premium