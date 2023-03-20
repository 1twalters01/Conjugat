import { Link } from "react-router-dom"
import Authorization from "../functions/Authorization"

function Home() {
    Authorization.AuthRequired()
    return (
      <div>
        <h1>Home</h1>
        <Link to='../account/logout/' >Log out</Link>

        <br />
        
        <Link to='../settings/' >Settings</Link>
        
        <br />
        
        <Link to='../subscriptions/' >Subscribe</Link>
        
        <br />
        
        <Link to='../Newsletter/' >Newsletter</Link>
      </div>
      
    )
  }

export default Home