import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/Terms"
import '../../sass/pages/home/Terms.scss'

function Terms() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>

            <div className="Terms-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>

                <div className="navbar">
                    <MiscNavbar language={language} />
                </div>

                <div className="para">
                    <h1 className="text">{getTranslation(translations, language, 'Title')}</h1>
                    <h3 className="subtitle text">
                        {getTranslation(translations, language, 'Subtitle')}
                    </h3>
                    
                    <ol>
                        <li className="text">
                            <h3 className="text">{getTranslation(translations, language, 'Heading1')}</h3>
                            <p className="text">{getTranslation(translations, language, 'Text1-1')}</p>
                            <p className="text bold"><span>{getTranslation(translations, language, 'Text1-2')}</span></p>
                        </li>

                        <li className="text">
                            <h3 className="text"><h3 className="text">{getTranslation(translations, language, 'Heading2')}</h3></h3>
                            <p className="text">{getTranslation(translations, language, 'Text2')}</p>
                        </li>

                        <li className="text">
                            <h3 className="text">{getTranslation(translations, language, 'Heading3')}</h3>
                            <p className="text">{getTranslation(translations, language, 'Text3')}</p>
                        </li>

                        <li className="text">
                            <h3 className="text">{getTranslation(translations, language, 'Heading4')}</h3>
                            <p className="text">{getTranslation(translations, language, 'Text4')}</p>
                        </li>

                        <li className="text">
                            <h3 className="text">{getTranslation(translations, language, 'Heading5')}</h3>
                            <p className="text">{getTranslation(translations, language, 'Text5')}</p>
                        </li>

                        <li className="text">
                            <h3 className="text">{getTranslation(translations, language, 'Heading6')}</h3>
                            <p className="text">{getTranslation(translations, language, 'Text6-1')}</p>
                            <p className="text">{getTranslation(translations, language, 'Text6-2')}</p>
                            <p className="text">{getTranslation(translations, language, 'Text6-3')}</p>
                        </li>
                    </ol>
                </div>
            </div>
        </>
    )
}

export default Terms