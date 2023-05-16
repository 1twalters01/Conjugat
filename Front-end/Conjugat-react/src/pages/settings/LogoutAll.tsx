import { useState } from 'react'
import { useSelector } from 'react-redux'
import { RootState } from '../../redux/store'
import Authorization from '../../functions/Authorization'
import LogoutAllBtn from '../../components/settings/Logout all/LogoutAllBtn'
import { Link } from 'react-router-dom'
import { translations } from '../../content/settings/LogoutAll'
import { getTranslation } from '../../functions/getTranslation'
import { Helmet } from 'react-helmet-async'

function LogoutAll() {
  Authorization.AuthRequired()
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)
  const [LoggedOut, SetLoggedOut] = useState(false)
  if (LoggedOut==false) {
      return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
                <link rel="canonical" href="/settings/logout-all" />
            </Helmet>

            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">{getTranslation(translations, language, 'Text1')}</h1>
                </div>
                
                <div className="para">
                    <p className='text'>{getTranslation(translations, language, 'Text2')}</p>
                </div>

                <div className="form-spacer">
                    <LogoutAllBtn
                    onLoggedOutChange={SetLoggedOut}
                    />
                </div>
            </div>
          </>
      )
  }
  else if (LoggedOut==true) {
      return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title1')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent1')}
                    />
                    <link rel="canonical" href="/settings/logout-all" />
                </Helmet>
                
                <div className="rhs container">
                    <div className="Header-spacer">
                        <h1 className="text">{getTranslation(translations, language, 'Text3')}</h1>
                    </div>                

                    <div className="para">
                        <p className="text">{getTranslation(translations, language, 'Text4')}</p>
                        <Link to="../login"><div className="register weak-btn">{getTranslation(translations, language, 'Text5')}</div></Link>
                    </div>
                </div>
            </>
      )
  }
  return <div></div>
}

export default LogoutAll