import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import '../../sass/pages/home/FAQ.scss'

function Faq() {
    return (
        <div className="FAQ-container container">
            <div className="Header-spacer">
                <Header />
            </div>

            <div className="navbar">
                <MiscNavbar/>
            </div>

            <h1>FAQ</h1>
        </div> 
    )
  }

export default Faq