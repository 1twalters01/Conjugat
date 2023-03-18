import { FormEvent } from "react"
import { useDispatch } from "react-redux";
import { onUsernameChange, onIdChange, onConfirmedChange } from "../../../redux/slices/loginSlice";
import '../../../sass/Components/account/Login/ResetUsername.scss'

function ResetUsername({ onPageChange}: { onPageChange:Function }) {
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
            value="Different username"
            className="register weak-btn"
          />
        </form>
      </div>
    )
}

export default ResetUsername