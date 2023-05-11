import { FormEvent } from "react"
import { useDispatch } from "react-redux";
import { onUsernameChange, onIdChange, onConfirmedChange } from "../../../redux/slices/loginSlice";
import { getTranslation } from "../../../functions/getTranslation"
import { ResetUsernameTranslation } from "../../../content/account/Login"
import '../../../sass/Components/account/Login/ResetUsername.scss'

function ResetUsername({ language, onPageChange}: { language:string, onPageChange:Function }) {
    const dispatch = useDispatch();
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        dispatch(onUsernameChange(''))
        dispatch(onIdChange(null))
        dispatch(onConfirmedChange(null))
        onPageChange('username')
    }

    return(
      <div className="reset-username">
        <form onSubmit={(e) => submit(e)}>
          <input type="submit"
            value={getTranslation(ResetUsernameTranslation, language, 'Label')}
            className="register strong-white-btn"
          />
        </form>
      </div>
    )
}

export default ResetUsername