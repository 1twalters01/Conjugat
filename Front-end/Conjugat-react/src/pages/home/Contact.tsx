import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import { Link } from "react-router-dom"
import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/Contact"
import '../../sass/pages/home/Contact.scss'

function Contact() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>
            
            <div className="Contact-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>

                <div className="navbar">
                    <MiscNavbar language={language} />
                </div>

                <div className="para">
                    <h1 className="text">{getTranslation(translations, language, 'Title')}</h1>
                    <p className="text">
                        {getTranslation(translations, language, 'Text1')}
                        <span className="blue-text"> Conjugat465@gmail.com</span>
                    </p>
                    <p className="text">
                        {getTranslation(translations, language, 'Text2')}
                        <Link to='https://github.com/1twalters01/Conjugat' className="text-gold-link"> https://github.com/1twalters01/Conjugat</Link>
                    </p>
                </div>
            </div>
        </>
    )
  }

export default Contact