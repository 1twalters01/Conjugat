import Authorization from '../../functions/Authorization'
import RetrieveSuccessStatus from "../../components/subscriptions/success/RetrieveSuccessStatus"

function Success() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Success</h1>

      <RetrieveSuccessStatus />
    </div>
  )
}

export default Success