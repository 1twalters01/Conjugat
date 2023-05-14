import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/Privacy"
import '../../sass/pages/home/Privacy.scss'

function Privacy() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>

            <div className="Privacy-container container">
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
                            <p className="text">
                                {getTranslation(translations, language, 'Text1-1')}
                            </p>

                            <p className="text">
                                {getTranslation(translations, language, 'Text1-2')}
                            </p>

                            <p className="text">
                                {getTranslation(translations, language, 'Text1-3')}
                            </p>

                            <p className="text">
                                {getTranslation(translations, language, 'Text1-4')}
                            </p>
                        </li>

                        <li className="text">
                            <h3 className="text">{getTranslation(translations, language, 'Heading2')}</h3>
                            <p className="text">
                                {getTranslation(translations, language, 'Text2-1')}
                            </p>

                            <p className="italics text">
                                {getTranslation(translations, language, 'Text2-2')}
                            </p>

                            <p className="text">
                                {getTranslation(translations, language, 'Text2-3')}
                            </p>

                            <p className="italics text">
                                {getTranslation(translations, language, 'Text2-4')}
                            </p>

                            <p className="text">
                                {getTranslation(translations, language, 'Text2-5')}
                            </p>
                        </li>
                    </ol>
                </div>
            </div>
        </>
    )
}

export default Privacy