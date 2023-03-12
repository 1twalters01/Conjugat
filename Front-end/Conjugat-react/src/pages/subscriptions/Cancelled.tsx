import { Link } from "react-router-dom"
import Authorization from '../../components/functions/Authorization'

function Cancelled() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Cancelled</h1>
      
      <p>There was a problem processing your payment. <Link to="../process">Try again</Link></p>
    </div>
  )
}

export default Cancelled