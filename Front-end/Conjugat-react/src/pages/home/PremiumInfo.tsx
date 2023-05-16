import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/PremiumInfo"


function PremiumInfo() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
                <link rel="canonical" href="/premium" />
            </Helmet>

            <div className="Premium-container container">
                
            </div>
        </>
    )
}

export default PremiumInfo