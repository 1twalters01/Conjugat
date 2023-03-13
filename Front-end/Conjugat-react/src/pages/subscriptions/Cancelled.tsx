import Authorization from '../../components/functions/Authorization'
import CancelledText from "../../components/subscriptions/CancelledText"

function Cancelled() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Cancelled</h1>
      
      <CancelledText />
    </div>
  )
}

export default Cancelled