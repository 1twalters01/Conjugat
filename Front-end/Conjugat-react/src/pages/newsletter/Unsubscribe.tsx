import { useEffect, useState } from "react"
import { Helmet } from "react-helmet-async";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/store";
import { Link } from "react-router-dom";
import Header from "../../components/account/Header";
import NewsletterLinks from "../../components/newsletter/NewsletterLinks";
import NewsletterResponse from "../../components/newsletter/NewsletterResponse";
import LoadUnsubscribeForm from "../../components/newsletter/unsubscribe/LoadUnsubscribeform"
import { getTranslation } from "../../functions/getTranslation";
import { translations } from "../../content/newsletter/Unsubscribe";
import '../../sass/pages/newsletter/Unsubscribe.scss';

function Unsubscribe() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
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
                <>
                    <Helmet>
                        <title>{getTranslation(translations, language, 'Title1')}</title>
                        <meta name="description"
                            content={getTranslation(translations, language, 'metaContent1')}
                        />
                        <link rel="canonical" href="/newsletter/unsubscribe" />
                    </Helmet>

                    <div className="Newsletter-unauth-unsubscribe-container container">
                        <div className="Header-spacer">
                            <Header language={language} />
                        </div>
                        
                        <div className="NewsletterLinks-spacer">
                            <NewsletterLinks language={language} />
                        </div>
        
                        <div className="para">
                            <p className="text">{getTranslation(translations, language, 'Text1')}</p>
                        </div>
        
                        <div className="form-width">
                            <LoadUnsubscribeForm
                            language={language}
                            loading={loading}
                            setDone={setDone}
                            setLoading={setLoading}
                            />
                        </div>
        
                        <div className="subscribe-link">
                            <Link to="../subscribe/"><p className="text">{getTranslation(translations, language, 'Text2')}</p></Link>
                        </div>
                    </div>
                </>
            )
        }
        else if (done === true) {
            return (
                <>
                    <Helmet>
                        <title>{getTranslation(translations, language, 'Title2')}</title>
                        <meta name="description"
                            content={getTranslation(translations, language, 'metaContent2')}
                        />
                        <link rel="canonical" href="/newsletter/unsubscribe" />
                    </Helmet>

                    <div className="Newsletter-unauth-unsubscribe-container container">
                        <div className="Header-spacer">
                            <Header language={language} />
                        </div>
                        
                        <div className="logout-response-spacer">
                            <NewsletterResponse
                            language={language}
                            text={getTranslation(translations, language, 'Text3')}
                            />
                        </div>
                    </div>
                </>
            )
        }
    }
    else if (isLoggedIn == true) {
        if (done == false) {
            return (
                <>
                    <Helmet>
                        <title>{getTranslation(translations, language, 'Title3')}</title>
                        <meta name="description"
                            content={getTranslation(translations, language, 'metaContent3')}
                        />
                        <link rel="canonical" href="/newsletter/unsubscribe" />
                    </Helmet>

                    <div className="Newsletter-auth-unsubscribe-container container">
        
                        <div className="para">
                            <p className="text">{getTranslation(translations, language, 'Text4')}</p>
                        </div>
        
                        <div className="form-width">
                            <LoadUnsubscribeForm
                            language={language}
                            loading={loading}
                            setDone={setDone}
                            setLoading={setLoading}
                            />
                        </div>
        
                        <div className="subscribe-link">
                            <Link to="../subscribe/"><p className="text">{getTranslation(translations, language, 'Text5')}</p></Link>
                        </div>
                    </div>
                </>
            )
        }
        else if (done === true) {
            return (
                <>
                
                    <Helmet>
                            <title>{getTranslation(translations, language, 'Title4')}</title>
                            <meta name="description"
                                content={getTranslation(translations, language, 'metaContent4')}
                            />
                            <link rel="canonical" href="/newsletter/unsubscribe" />
                    </Helmet>
                    
                    <div className="Newsletter-auth-unsubscribe-container container">
                        
                        <div className="logout-response-spacer">
                            <NewsletterResponse
                            language={language}
                            text={getTranslation(translations, language, 'Text6')}
                            />
                        </div>
                    </div>
                </>
            )
        }
    }
    return <></>
}

export default Unsubscribe