import { Link } from "react-router-dom"

function Home() {
    return (
      <div>
        <h1>Home</h1>
        <Link to='../account/logout/' >Log out</Link>
      </div>
      
    )
  }

export default Home