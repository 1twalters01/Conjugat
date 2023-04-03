import Dropdowns from "../../components/home/FAQs/Dropdowns"
import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import '../../sass/pages/home/FAQ.scss'

function Faq() {
    return (
        <div className="FAQ-container container">
            <div className="Header-spacer">
                <Header />
            </div>

            <div className="navbar-spacer">
                <MiscNavbar />
            </div>
            
            <div className="para">
                <h1 className="text">FAQ</h1>
            </div>

            <div className="dropdown-spacer">
                <Dropdowns />
            </div>
        </div>
    )
  }

export default Faq