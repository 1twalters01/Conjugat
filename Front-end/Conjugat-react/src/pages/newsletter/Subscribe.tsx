import { useState } from "react"
import { Link } from "react-router-dom";
import Header from "../../components/account/Header";
import LoadSubscribeForm from "../../components/newsletter/subscribe/LoadSubscribeForm";
import NewsletterLinks from "../../components/newsletter/NewsletterLinks";
import '../../sass/pages/newsletter/Subscribe.scss';

function Subscribe() {
    const [loading, setLoading] = useState(true);
    const [done, setDone] = useState(false)
    if (done == false) {
        return (
            <div className="Newsletter-subscribe-container container">
                <div className="Header-spacer">
                    <Header />
                </div>

                <div className="NewsletterLinks-spacer">
                    <NewsletterLinks />
                </div>
                
                <div className="para">
                    <p className="text">Thank you for your interest in joining our newsletter!</p>
                    <p className="text">Fill in the form below to subscribe.</p>
                </div>

                <div className="form-width">
                    <LoadSubscribeForm
                      loading={loading}
                      setDone={setDone}
                      setLoading={setLoading}
                    />
                </div>
                
                <div className="unsubscribe-link">
                    <Link to="../unsubscribe/"><p className="text">Unsubscribe from the newsletter</p></Link>
                </div>
            </div>
        )
    }
    else if (done === true) {
        return (
            <p>Sign up successful</p>
        )
    }
}

export default Subscribe