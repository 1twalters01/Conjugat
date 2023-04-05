import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"

function Home() {
    Authorization.AuthRequired()
    return (
      <div>
        <h1>Home</h1>
        <Link to='../account/logout/' className="text-blue-link">Log out</Link>

        <br />
        
        <Link to='../settings/change-email/' className="text-blue-link">Settings</Link>
        
        <br />
        
        <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
        
        <br />
        
        <Link to='../Newsletter/subscribe/' className="text-blue-link">Newsletter</Link>
      </div>
      
    )
  }

export default Home