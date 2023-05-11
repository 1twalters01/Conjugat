import { Link } from "react-router-dom"
import { getTranslation } from '../../../functions/getTranslation';
import { BottomContainerTranslations } from '../../../content/home/LandingPage'
import '../../../sass/Components/home/Landing page/BottomContainer.scss'

function BottomContainer({language}: {language:string}) {
    return (
        <div className="Landing-page-bottom-container">
            <div className="section">
                <div className="Text">
                    <h1 className="subheader">{getTranslation(BottomContainerTranslations, language, 'Left-subheader')}</h1>
                    <p className="text">{getTranslation(BottomContainerTranslations, language, 'Left-text')}</p>
                </div>
                <Link to='account/register' className=""><p className="link-btn strong-green-btn">{getTranslation(BottomContainerTranslations, language, 'Left-button')}</p></Link>
            </div>

            <div className="section">
                <div className="Text">
                    <h1 className="subheader">{getTranslation(BottomContainerTranslations, language, 'Center-subheader')}</h1>
                    <p className="text">{getTranslation(BottomContainerTranslations, language, 'Center-text')}</p>
                </div>
            </div>

            <div className="section">
                <div className="Text">
                    <h1 className="subheader">{getTranslation(BottomContainerTranslations, language, 'Right-subheader')}</h1>
                    <p className="text">{getTranslation(BottomContainerTranslations, language, 'Right-text')}</p>
                </div>
                <Link to='newsletter/subscribe' className="link"><p className="link-btn weak-gold-btn">{getTranslation(BottomContainerTranslations, language, 'Right-button')}</p></Link>
            </div>
        </div>
    )
}

export default BottomContainer