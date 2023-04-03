import { useEffect, useState } from "react"
import { Link } from "react-router-dom";
import Header from "../../components/account/Header";
import NewsletterLinks from "../../components/newsletter/NewsletterLinks";
import NewsletterResponse from "../../components/newsletter/NewsletterResponse";
import LoadUnsubscribeForm from "../../components/newsletter/unsubscribe/LoadUnsubscribeform"
import '../../sass/pages/newsletter/Unsubscribe.scss';

function Unsubscribe() {
    const [loading, setLoading] = useState(true);
    const [done, setDone] = useState(false)

    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        const userToken = localStorage.getItem('token');
        if (!userToken) {
            setIsLoggedIn(false);
        }
        else{
            setIsLoggedIn(true);
        }
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);

    if (isLoggedIn == false) {
        if (done == false) {
            return (
                <div className="Newsletter-unauth-unsubscribe-container container">
                    <div className="Header-spacer">
                        <Header />
                    </div>
                    
                    <div className="NewsletterLinks-spacer">
                        <NewsletterLinks />
                    </div>
    
                    <div className="para">
                        <p className="text">We are sad to see you go. Please fill in the form below to unsubscribe.</p>
                    </div>
    
                    <div className="form-width">
                        <LoadUnsubscribeForm
                        loading={loading}
                        setDone={setDone}
                        setLoading={setLoading}
                        />
                    </div>
    
                    <div className="subscribe-link">
                        <Link to="../subscribe/"><p className="text">Subscribe to the newsletter</p></Link>
                    </div>
                </div>
            )
        }
        else if (done === true) {
            return (
                <div className="Newsletter-unauth-unsubscribe-container container">
                    <div className="Header-spacer">
                        <Header />
                    </div>
                    
                    <div className="logout-response-spacer">
                        <NewsletterResponse
                        text={"You have successfully unsubscribed from the newsletter"}
                        />
                    </div>
                </div>
            )
        }
    }
    else if (isLoggedIn == true) {
        if (done == false) {
            return (
                <div className="Newsletter-auth-unsubscribe-container container">
    
                    <div className="para">
                        <p className="text">We are sad to see you go. Please fill in the form below to unsubscribe.</p>
                    </div>
    
                    <div className="form-width">
                        <LoadUnsubscribeForm
                        loading={loading}
                        setDone={setDone}
                        setLoading={setLoading}
                        />
                    </div>
    
                    <div className="subscribe-link">
                        <Link to="../subscribe/"><p className="text">Subscribe to the newsletter</p></Link>
                    </div>
                </div>
            )
        }
        else if (done === true) {
            return (
                <div className="Newsletter-auth-unsubscribe-container container">
                    
                    <div className="logout-response-spacer">
                        <NewsletterResponse
                        text={"You have successfully unsubscribed from the newsletter"}
                        />
                    </div>
                </div>
            )
        }
    }
}

export default Unsubscribe