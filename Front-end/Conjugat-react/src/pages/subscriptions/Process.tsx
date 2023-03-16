import Authorization from '../../functions/Authorization'
import RetrieveStatus from "../../components/subscriptions/Process/RetrieveStatus"

function Process() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Process</h1>

      <RetrieveStatus />
    </div>
  )
}

export default Process