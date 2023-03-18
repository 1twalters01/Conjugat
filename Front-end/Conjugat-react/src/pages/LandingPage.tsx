import { Link } from "react-router-dom"
import Authorization from "../functions/Authorization"

function Index() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Index</h1>
        <Link to='../account/login/' >Log in</Link>
      </div>
      
    )
}

export default Index