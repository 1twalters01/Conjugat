import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"
import { onThemeChange } from "../../../redux/slices/themeSlice"
import { RootState } from "../../../redux/store"
import '../../../sass/Components/home/Landing page/Navbar.scss'

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
        <nav className="Landing-page-navbar">
            <div className="logo">
                <Link to='/' ><h1 className="logo text">Conjugat</h1></Link>
            </div>
            <div className="options">
                <Link to='/Contact' ><p className="link text-gold-link">Contact</p></Link>
                <Link to='/Faq' ><p className="link text-gold-link">Faq</p></Link>
                <Link to='/Privacy' ><p className="link text-gold-link">Privacy</p></Link>
                <Link to='/Terms' ><p className="link text-gold-link">Terms</p></Link>
            </div>
            <div className="settings">
                <Link to='/' ><p className="link text-blue-link" onClick={ThemeSwitch}>Theme</p></Link>
                <Link to='/' ><p className="link text-gold-link">Language</p></Link>
                <Link to='/Premium' ><p className="link text-gold-link">Premium</p></Link>
            </div>
            <Link to='/account/Login' ><div className="">
                <p className="login strong-gold-btn">Log in</p>
            </div></Link>
        </nav>
    )
}

export default Navbar