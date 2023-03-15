import ThemeFunctionality from '../../components/settings/Theme/ThemeFunctionality'
import Authorization from '../../functions/Authorization'

function Themes() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Theme</h1>
    
      <ThemeFunctionality />
    </div>
  )
}


export default Themes