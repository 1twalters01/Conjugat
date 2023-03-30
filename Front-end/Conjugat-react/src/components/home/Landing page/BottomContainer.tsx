import { Link } from "react-router-dom"
import '../../../sass/Components/home/Landing page/BottomContainer.scss'

function BottomContainer() {
    return (
        <div className="Landing-page-bottom-container">
            <div className="section">
                <div className="Text">
                    <h1 className="subheader">Ready to begin your journey?</h1>
                    <p className="text">Let us help you on your path by joining conjugat for free, or get one week of Conjugat premium on us!</p>
                </div>
                <Link to='account/register' className=""><p className="link-btn strong-green-btn">Join now</p></Link>
            </div>

            <div className="section">
                <div className="Text">
                    <h1 className="subheader">Coming soon to android and ios</h1>
                    <p className="text">The engineer is working as quickly as possible to bring the conjugat experience to your android and ios devices.</p>
                </div>
            </div>

            <div className="section">
                <div className="Text">
                    <h1 className="subheader">Or join our free newsletter</h1>
                    <p className="text">Receive our weekly tips that will help you go on your language learning adventure as efficiently as possible.</p>
                </div>
                <Link to='newsletter/subscribe' className="link"><p className="link-btn weak-gold-btn">Sign up</p></Link>
            </div>
        </div>
    )
}

export default BottomContainer