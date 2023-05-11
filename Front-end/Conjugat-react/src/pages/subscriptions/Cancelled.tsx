import Authorization from '../../functions/Authorization'
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import { Link } from 'react-router-dom'
import { getTranslation } from '../../functions/getTranslation'
import { translations } from '../../content/subscriptions/Cancelled'
import '../../sass/pages/subscriptions/Cancelled.scss'

function Cancelled() {
  Authorization.AuthRequired()
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)

  return (
    <div className='Cancelled-container container'>
      <h1 className='text'>{getTranslation(translations, language, 'Text1')}</h1>
      
      <div className="text-spacer">
          <p className='text'>{getTranslation(translations, language, 'Text2')}</p>
      </div>

      <div className="btn-spacer">
          <Link to="../process" className='retry-btn strong-gold-btn'>{getTranslation(translations, language, 'Link')}</Link>
      </div>
      
    </div>
  )
}

export default Cancelled