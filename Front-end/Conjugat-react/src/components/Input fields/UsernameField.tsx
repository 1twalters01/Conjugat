import '../../sass/Components/Input fields/UsernameField.scss'
import { useSelector, useDispatch } from "react-redux";

import { onUsernameChange } from '../../redux/slices/loginSlice';
import { RootState } from '../../redux/store';

function UsernameField({ labelText="Email or Username" }: {labelText:string}) {
  const{ username } = useSelector((state: RootState) => state.login)
  const dispatch = useDispatch();
  console.log(username)
  return (
    <div className='username-field'>
      <label htmlFor="username" className="field-text">{labelText}</label>
      <input
        id="username"
        type="text"
        name="username"
        value={ username }
        onChange={(e) => dispatch(onUsernameChange(e.target.value))}
        required={true}
      />
    </div>
  )
}

export default UsernameField