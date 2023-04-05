import Authorization from '../../functions/Authorization'
import RetrievePremiumStatus from "../../components/settings/premium/RetrievePremiumStatus"

function Premium() {
    Authorization.AuthRequired()
    return (
        <div className="rhs container">
            <div className="Header-spacer">
                <h1 className="text">Premium</h1>
            </div>

            <div className="form-spacer">
                <RetrievePremiumStatus />
            </div>
        </div>
    )
}



export default Premium