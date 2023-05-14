import { useState } from "react"
import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import { getTranslation } from '../../functions/getTranslation'
import { translations } from '../../content/settings/ChangeUsername'
import UsernameChangeForm from "../../components/settings/Change username/UsernameChangeForm"

function ChangeUsername() {
  Authorization.AuthRequired()
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)
  const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title1')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent1')}
                    />
                </Helmet>

                <div className="rhs container">
                    <div className="Header-spacer">
                        <h1 className="text">{getTranslation(translations, language, 'Text1')}</h1>
                    </div>
                    
                    <div className="form-spacer">
                        <UsernameChangeForm
                        language={language}
                        onDoneChange={setDone}
                        />
                    </div>
                </div>
            </>
        )
    }
    else if (done == true) {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title2')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent2')}
                    />
                </Helmet>
                
                <div className="rhs container">
                    <div className="Header-spacer">
                        <h1 className="text">{getTranslation(translations, language, 'Text2')}</h1>
                    </div>                

                    <div className="para">
                        <p className="text">{getTranslation(translations, language, 'Text3')}</p>
                    </div>
                </div>
            </>
        )
    }
    return <div></div>
}

export default ChangeUsername