import { Link } from "react-router-dom"

function Index() {
    return (
      <div>
        <h1>Index</h1>
        <Link to='../account/login/' >Log in</Link>
      </div>
      
    )
  }

export default Index