import { useEffect, useState } from "react"
import { Helmet } from "react-helmet-async";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/store";
import { Link } from "react-router-dom";
import Header from "../../components/account/Header";
import LoadSubscribeForm from "../../components/newsletter/subscribe/LoadSubscribeForm";
import NewsletterLinks from "../../components/newsletter/NewsletterLinks";
import NewsletterResponse from "../../components/newsletter/NewsletterResponse";
import SettingsNavbar from "../../components/settings/SettingsNavbar";
import { getTranslation } from "../../functions/getTranslation"
import { translations } from '../../content/newsletter/Subscribe'
import '../../sass/pages/newsletter/Subscribe.scss';

function Subscribe() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [loading, setLoading] = useState(true);
    const [done, setDone] = useState(false)

    type ILoggedIn = boolean|null
    const [isLoggedIn, setIsLoggedIn] = useState<ILoggedIn>(null);
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
                        <link rel="canonical" href="/newsletter/subscribe" />
                    </Helmet>

                    <div className="Newsletter-unauth-subscribe-container container">
                        <div className="Header-spacer">
                            <Header language={language} />
                        </div>
        
                        <div className="NewsletterLinks-spacer">
                            <NewsletterLinks language={language} />
                        </div>
                        
                        <div className="para">
                            <p className="text">{getTranslation(translations, language, 'Text1')}</p>
                            <p className="text">{getTranslation(translations, language, 'Text2')}</p>
                        </div>
        
                        <div className="form-width">
                            <LoadSubscribeForm
                                language={language}
                                loading={loading}
                                setDone={setDone}
                                setLoading={setLoading}
                            />
                        </div>
                        
                        <div className="unsubscribe-link">
                            <Link to="../unsubscribe/"><p className="text">{getTranslation(translations, language, 'Text3')}</p></Link>
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
                    </Helmet>

                    <div className="Newsletter-unauth-subscribe-container container">
                        <div className="Header-spacer">
                            <Header language={language} />
                        </div>
                        
                        <div className="logout-response-spacer">
                            <NewsletterResponse
                                language={language}
                                text={getTranslation(translations, language, 'Text4')}
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
                    </Helmet>

                    <div className="Settings-navbar-container container">
                        <SettingsNavbar language={language} />
                    </div>

                    <div className="Newsletter-auth-container container">
                        <div className="Header-spacer">
                            <h1 className="header">{getTranslation(translations, language, 'Text5')}</h1>
                        </div>

                        <div className="para">
                            <p className="text">{getTranslation(translations, language, 'Text6')}</p>
                            <p className="text">{getTranslation(translations, language, 'Text7')}</p>
                        </div>
        
                        <div className="form-width">
                            <LoadSubscribeForm
                            language={language}
                            loading={loading}
                            setDone={setDone}
                            setLoading={setLoading}
                            />
                        </div>
                        
                        <div className="unsubscribe-link">
                            <Link to="../unsubscribe/"><p className="text">{getTranslation(translations, language, 'Text8')}</p></Link>
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
                    </Helmet>

                    <div className="Settings-navbar-container container">
                        <SettingsNavbar language={language} />
                    </div>
                    
                    <div className="Newsletter-auth-container container">
                        
                        <div className="logout-response-spacer">
                            <NewsletterResponse
                            language={language}
                            text={getTranslation(translations, language, 'Text9')}
                            />
                        </div>
                    </div>

                </>
            )
        }
    }
    
    return <></>
}

export default Subscribe