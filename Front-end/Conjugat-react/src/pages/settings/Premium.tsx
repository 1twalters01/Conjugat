import Authorization from '../../functions/Authorization'
import RetrievePremiumStatus from "../../components/settings/premium/RetrievePremiumStatus"

function Premium() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Premium</h1>

      <RetrievePremiumStatus />
    </div>
  )
}



export default Premium