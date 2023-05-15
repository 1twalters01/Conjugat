import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"

import Authorization from '../../functions/Authorization'
import RetrieveStatus from "../../components/subscriptions/Process/RetrieveStatus"

import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/subscriptions/Process"
import '../../sass/pages/subscriptions/Process.scss'

function Process() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>
            
            <div className='Process-container container'>
                <h1>{getTranslation(translations, language, 'Text1')}</h1>

                <div className="status-container">
                    <RetrieveStatus />
                </div>
            </div>
        </>
    )
}

export default Process