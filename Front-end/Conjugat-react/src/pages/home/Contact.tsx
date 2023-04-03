import { Link } from "react-router-dom"
import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import '../../sass/pages/home/Contact.scss'

function Contact() {
    return (
        <div className="Contact-container container">
            <div className="Header-spacer">
                <Header />
            </div>

            <div className="navbar">
                <MiscNavbar/>
            </div>

            <div className="para">
                <h1 className="text">Contact us</h1>
                <p className="text">
                    Have any troubles or suggestions? Email us at:
                    <span className="blue-text"> Conjugat465@gmail.com</span>
                </p>
                <p className="text">
                    Want to raise an issue on github? Find it here:
                    <Link to='https://github.com/1twalters01/Conjugat' className="text-gold-link"> https://github.com/1twalters01/Conjugat</Link>
                </p>
            </div>
        </div> 
    )
  }

export default Contact