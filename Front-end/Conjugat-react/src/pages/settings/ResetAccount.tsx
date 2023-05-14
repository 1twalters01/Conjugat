import { useState } from "react"
import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from "../../functions/Authorization"
import AccountResetForm from "../../components/settings/reset account/AccountResetForm"
import { getTranslation } from '../../functions/getTranslation'
import { translations } from '../../content/settings/ResetAccount'
import '../../sass/pages/settings/ResetAccount.scss'

function ResetAccount() {
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
                        <AccountResetForm
                            language={language}
                            onDoneChange={setDone}
                        />
                    </div>
                </div>
            </>
        )
    }
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

export default ResetAccount