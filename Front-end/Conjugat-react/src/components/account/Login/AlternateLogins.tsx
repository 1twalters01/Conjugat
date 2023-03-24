import '../../../sass/Components/account/Login/AlternateLogins.scss'
import GetFacebookURL from './FacebookBtn'
import GetGoogleURL from './GoogleBtn'
import GetTwitterURL from './TwitterBtn'

function AlternateLogins() {
    return (
      <div className="alternatives">
        <p className="options">Or log-in via:</p>
        <div className="alt-login">
          <GetFacebookURL />
          <GetGoogleURL />
          <GetTwitterURL />
        </div>
      </div>
    )
  }

export default AlternateLogins