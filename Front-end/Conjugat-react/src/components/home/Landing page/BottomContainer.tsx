import { Link } from "react-router-dom"

function BottomContainer() {
    return (
        <div className="bottom-container">
            <div className="first">
                <div className="Text">
                    <h1>Or join our free newsletter</h1>
                    <p>Receive our weekly tips that will help you go on your language learning adventure as efficiently as possible.</p>
                </div>
                <Link to='newsletter/subscribe'><p className="get-started">Get started</p></Link>
            </div>

            <div className="second">
                <div className="Text">
                    <h1>Coming soon to android and ios</h1>
                    <p>The engineer is working as quickly as possible to bring you the conjugat experience on your android and ios devices.</p>
                </div>
            </div>

            <div className="third">
                <div className="Text">
                    <h1>Ready to begin your journey?</h1>
                    <p>Let us help you on your path by joining conjugat for free, or get one week of Conjugat premium on us!</p>
                </div>
                <Link to='account/register'><p className="join-now">Join now</p></Link>
            </div>
        </div>
    )
}

export default BottomContainer