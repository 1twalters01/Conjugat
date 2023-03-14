import { FormEvent } from "react"

import '../../../sass/Components/account/Login/ResetUsername.scss'

function ResetUsername({onUsernameChange, onPageChange, onIdChange, onConfirmedChange}: {onUsernameChange:Function, onPageChange:Function, onIdChange:Function, onConfirmedChange:Function}) {
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        onUsernameChange('')
        onIdChange('')
        onConfirmedChange(null)
        onPageChange('username')
    }

    return(
        <div className="reset-username">
            <form onSubmit={(e) => submit(e)}>
                <input type="submit"
                    value="Choose a different username"
                    className="register weak-btn"
                />
            </form>
        </div>
    )
}

export default ResetUsername