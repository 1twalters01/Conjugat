import { useEffect, useState } from 'react'
import { Helmet } from 'react-helmet-async'
import { useSelector } from 'react-redux'
import { RootState } from '../../redux/store'
import { Link, useParams } from 'react-router-dom'
// import { toast } from 'react-toastify'
import Header from '../../components/account/Header'
import Authorization from '../../functions/Authorization'
import AxiosInstance from '../../functions/AxiosInstance'
import { getTranslation } from '../../functions/getTranslation'
import { translations } from '../../content/account/Activate'
import '../../sass/pages/account/Activate.scss'

function Activate() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [Activated, SetActivated] = useState(false)
    const [Error, SetError] = useState(false)
    const { uidb64, token } = useParams()
    const activateAccount = async () => {const res = await (
        AxiosInstance.Unauthorised
        .post('/account/activate/', {
            uidb64: uidb64,
            token: token
        })
        .then(res =>
            SetActivated(true)
        )
        .catch(err => {
            SetError(true)
        })
    )}

    useEffect(() => {
      activateAccount();
    }, [])

    if(Activated == false && Error == false) {
        return (
          <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
                <link rel="canonical" href={`/account/activate/${uidb64}/${token}`} />
            </Helmet>
          </>
        )
    }
    else if(Activated == true) {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title2')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent2')}
                    />
                    <link rel="canonical" href={`/account/activate/${uidb64}/${token}`} />
                </Helmet>

                <div className='Activate-container container'>
                    <div className="header-spacer">
                        <Header language={language} />
                    </div>

                    <div className="text-spacer">
                        <p className='text'>{getTranslation(translations, language, 'Text1')}</p>
                    </div>

                    <div className="btn-spacer">
                        <Link to='../Login' ><div className="login-btn strong-gold-btn">{getTranslation(translations, language, 'Login')}</div></Link>
                    </div>
                </div>
            </>
        )
    }
    if (Error == true && Activated == false) {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title3')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent3')}
                    />
                    <link rel="canonical" href={`/account/activate/${uidb64}/${token}`} />
                </Helmet>

                <div className="Activate-container container">
                    <div className="header-spacer">
                        <Header language={language} />
                    </div>

                    <div className="text-spacer">
                        <p className='text'>{getTranslation(translations, language, 'Text2')}</p>
                    </div>

                    <div className="btn-spacer">
                        <Link to='../Login' ><div className="login-btn strong-gold-btn">{getTranslation(translations, language, 'Login')}</div></Link>
                    </div>
                </div>
            </>
        )
    }
    return <></>
}

export default Activate