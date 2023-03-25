import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom"
import { onThemeChange } from "../../../redux/slices/themeSlice";
import { RootState } from "../../../redux/store";

function Navbar() {
    const dispatch = useDispatch();
    const{ theme } = useSelector((state: RootState) => state.persistedReducer.theme)
    function ThemeSwitch() {
        if (theme == 'Dark') {
            dispatch(onThemeChange('Light'))
        }
        else {
            dispatch(onThemeChange('Dark'))
        }
        
    }
    return(
        <nav>
            <div className="logo">
                <Link to='/' ><p className="logo">Conjugat</p></Link>
            </div>
            <div className="options">
                <Link to='/Contact' ><p className="link">Contact</p></Link>
                <Link to='/FAQ' ><p className="link">FAQ</p></Link>
                <Link to='/Privacy' ><p className="link">Privacy</p></Link>
                <Link to='/Terms' ><p className="link">Terms</p></Link>
            </div>
            <div className="settings">
                <Link to='/' ><p className="link" onClick={ThemeSwitch}>Theme</p></Link>
                <Link to='/' ><p className="link">Language</p></Link>
                <Link to='/' ><p className="link">Premium</p></Link>
            </div>
            <Link to='/account/Login' ><div className="login">
                <p className="">Log in</p>
            </div></Link>
        </nav>
    )
}

export default Navbar