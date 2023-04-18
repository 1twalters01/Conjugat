import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"
import AxiosInstance from "../../functions/AxiosInstance"
import { useEffect } from "react"

function Home() {
    Authorization.AuthRequired()
    async function retrieveData() {
      const res = await(
        AxiosInstance.Authorised
        .get('/home')
      )
      console.log(res)
    }

    useEffect(() => {
      retrieveData(), []
    })

    return (
        <div>
            <h1>Home</h1>
            <Link to='../account/logout/' className="text-blue-link">Log out</Link>

            <br />
            
            <Link to='../settings/change-email/' className="text-blue-link">Settings</Link>
            
            <br />
            
            <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
            
            <br />
            
            <Link to='../newsletter/' className="text-blue-link">Newsletter</Link>

            <br />
            
            <Link to='../verbs/test' className="text-blue-link">verb test</Link>
        </div>
    )
}

export default Home