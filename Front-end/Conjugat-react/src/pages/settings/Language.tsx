import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from "../../functions/Authorization"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/settings/Language"
import { useState } from "react"
import LanguageForm from "../../components/settings/Language/LanguageForm"

function Language() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
	const [done, setDone] = useState(false)
	if (done === false) {
		return (
	        <>
        		<Helmet>
            		<title>{getTranslation(translations, language, 'Title1')}</title>
            		<meta name="description"
            			content={getTranslation(translations, language, 'metaContent1')}
            		/>
            		<link rel="canonical" href="/settings/language" />
        		</Helmet>

        		<div className="rhs container">
					<div className="Header-spacer">
						<h1 className="text">{getTranslation(translations, language, 'Text1')}</h1>
					</div>
					
					<div className="form-spacer">
						<LanguageForm language={language} />
					</div>
        		</div>
        	</>
        )
    }
	else if (done === true) {
		return (
			<>
				<Helmet>
					<title>{getTranslation(translations, language, 'Title2')}</title>
            		<meta name="description"
            			content={getTranslation(translations, language, 'metaContent2')}
            		/>
            		<link rel="canonical" href="/settings/font" />
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
	else {
		return (<></>)
	}
}

export default Language