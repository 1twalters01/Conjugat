import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from "../../functions/Authorization"
import BottomContainer from "../../components/home/Landing page/BottomContainer"
import Navbar from "../../components/home/Landing page/Navbar"
import TopContainer from "../../components/home/Landing page/TopContainer"
import LPFooter from "../../components/home/Landing page/LPFooter"
import '../../sass/pages/home/LandingPage.scss'

function Index() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
      <div className="Landing-page-container container">
          <div className="Navbar-spacer">
              <Navbar language={language} />
          </div>

          <div className="TopContainer-spacer">
              <TopContainer language={language} />
          </div>
          
          <div className="BottomContainer-spacer">
              <BottomContainer language={language} />
          </div>

          <div className="Footer">
                <LPFooter />
          </div>
      </div>
    )
}

export default Index