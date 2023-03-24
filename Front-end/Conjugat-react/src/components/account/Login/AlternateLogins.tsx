

import { Link } from 'react-router-dom'
import '../../../sass/Components/account/Login/AlternateLogins.scss'
import GetGoogleURL from './GoogleBtn'

function AlternateLogins() {
    return (
      <div className="alternatives">
        <p className="options">Or log-in via:</p>
        <div className="alt-login">
          <a href="{% url 'social:begin' 'facebook' %}" className='link'><div className="facebook Facebook-btn"><p>Facebook</p></div></a>
          <GetGoogleURL />
          {/* <a href="{% url 'social:begin' 'google-oauth2' %}" className='link'><div className="google Google-btn"><p>Google</p></div></a> */}
          <a href="{% url 'social:begin' 'twitter' %}" className='link'><div className="twitter Twitter-btn"><p>Twitter</p></div></a>
        </div>
      </div>
    )
  }

export default AlternateLogins