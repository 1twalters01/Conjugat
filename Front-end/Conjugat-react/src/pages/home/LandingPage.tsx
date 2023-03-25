import { Link } from "react-router-dom"
import BottomContainer from "../../components/home/Landing page/BottomContainer"
import Navbar from "../../components/home/Landing page/Navbar"
import TopContainer from "../../components/home/Landing page/TopContainer"
import Authorization from "../../functions/Authorization"

function Index() {
    Authorization.NotAuthRequired()
    return (
      <div className="Landing-page-container">        
          <Navbar />

          <TopContainer />

          <BottomContainer />
      </div>
    )
}

export default Index