import { Link } from "react-router-dom"
import { getTranslation } from '../../../functions/getTranslation';
import { translations } from '../../../content/home/Landing page/BottomContainer'
import '../../../sass/Components/home/Landing page/BottomContainer.scss'

function BottomContainer({language}: {language:string}) {
    return (
        <div className="Landing-page-bottom-container">
            <div className="section">
                <div className="Text">
                    <h1 className="subheader">{getTranslation(translations, language, 'Left-subheader')}</h1>
                    <p className="text">{getTranslation(translations, language, 'Left-text')}</p>
                </div>
                <Link to='account/register' className=""><p className="link-btn strong-green-btn">{getTranslation(translations, language, 'Left-button')}</p></Link>
            </div>

            <div className="section">
                <div className="Text">
                    <h1 className="subheader">{getTranslation(translations, language, 'Center-subheader')}</h1>
                    <p className="text">{getTranslation(translations, language, 'Center-text')}</p>
                </div>
            </div>

            <div className="section">
                <div className="Text">
                    <h1 className="subheader">{getTranslation(translations, language, 'Right-subheader')}</h1>
                    <p className="text">{getTranslation(translations, language, 'Right-text')}</p>
                </div>
                <Link to='newsletter/subscribe' className="link"><p className="link-btn weak-gold-btn">{getTranslation(translations, language, 'Right-button')}</p></Link>
            </div>
        </div>
    )
}

export default BottomContainer