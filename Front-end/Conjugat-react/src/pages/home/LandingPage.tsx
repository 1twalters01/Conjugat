import Authorization from "../../functions/Authorization"
import BottomContainer from "../../components/home/Landing page/BottomContainer"
import Navbar from "../../components/home/Landing page/Navbar"
import TopContainer from "../../components/home/Landing page/TopContainer"
import '../../sass/pages/home/LandingPage.scss'
import LPFooter from "../../components/home/Landing page/LPFooter"

function Index() {
    Authorization.NotAuthRequired()
    return (
      <div className="Landing-page-container container">
          <div className="Navbar-spacer">
              <Navbar />
          </div>

          <div className="TopContainer-spacer">
              <TopContainer />
          </div>
          
          <div className="BottomContainer-spacer">
              <BottomContainer />
          </div>

          <div className="Footer">
                <LPFooter />
          </div>
      </div>
    )
}

export default Index