import GetFacebookURL from './FacebookBtn'
import GetGoogleURL from './GoogleBtn'
import GetTwitterURL from './TwitterBtn'
import '../../../sass/Components/account/Login/AlternateLogins.scss'

function AlternateLogins() {
    return (
      <div className="alternatives">
        <p className="options text">Or log-in via:</p>
        <div className="alt-login">
          <GetFacebookURL />
          <GetGoogleURL />
          <GetTwitterURL />
        </div>
      </div>
    )
  }

export default AlternateLogins