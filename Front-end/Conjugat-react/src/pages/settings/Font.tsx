import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from "../../functions/Authorization"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/settings/Font"

function Font() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
 	const [loaded, isLoaded] = useState(true)
	const [done, isDone] = useState(false)
	if (done === false) {
		return (
	        <>
        		<Helmet>
            		<title>{getTranslation(translations, language, 'Title1')}</title>
            		<meta name="description"
            			content={getTranslation(translations, language, 'metaContent1')}
            		/>
            		<link rel="canonical" href="/settings/font" />
        		</Helmet>

        		<div>
            
        		</div>
        	</>
	    )
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

				<div>
				
				</div>
			</>
		)
	}
	else {
		return (<></>)
	}
}

export default Font