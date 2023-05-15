import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Dropdowns from "../../components/home/FAQs/Dropdowns"
import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/Faq"
import '../../sass/pages/home/FAQ.scss'

function Faq() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>

            <div className="FAQ-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>

                <div className="navbar">
                    <MiscNavbar language={language} />
                </div>
                
                <div className="para">
                    <h1 className="text">{getTranslation(translations, language, 'Title')}</h1>
                </div>

                <div className="dropdown-spacer">
                    <Dropdowns language={language} />
                </div>
            </div>
        </>
    )
  }

export default Faq