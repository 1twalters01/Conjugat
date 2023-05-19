import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from "../../functions/Authorization"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/settings/Language"

function Language() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
        <Helmet>
            <title>{getTranslation(translations, language, 'Title1')}</title>
            <meta name="description"
                content={getTranslation(translations, language, 'metaContent1')}
            />
            <link rel="canonical" href="/settings/premium" />
        </Helmet>

        <div>
            
        </div>
        </>
    )
}

export default Language