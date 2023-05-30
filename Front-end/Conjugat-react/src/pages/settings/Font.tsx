import { useState } from "react"
import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from "../../functions/Authorization"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/settings/Font"
import FontForm from "../../components/settings/Font/FontForm"

function Font() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
	return (
		<>
			<Helmet>
				<title>{getTranslation(translations, language, 'Title1')}</title>
				<meta name="description"
					content={getTranslation(translations, language, 'metaContent1')}
				/>
				<link rel="canonical" href="/settings/font" />
			</Helmet>

			<div className="rhs container">
				<div className="Header-spacer">
					<h1 className="text">{getTranslation(translations, language, 'Text1')}</h1>
				</div>
				
				<div className="form-spacer">
					<FontForm language={language} />
				</div>
			</div>
		</>
	)
    
}

export default Font