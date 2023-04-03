import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"
import { onThemeChange } from "../../../redux/slices/themeSlice"
import { RootState } from "../../../redux/store"
import '../../../sass/Components/home/Landing page/Navbar.scss'
import { useState } from "react"

function Navbar() {
    const dispatch = useDispatch();
    const{ theme } = useSelector((state: RootState) => state.persistedReducer.theme)
    const [navbarOpen, setNavbarOpen] = useState(false);

    function NavbarSwitch() {
        setNavbarOpen((!navbarOpen))
    }

    function ThemeSwitch() {
        if (theme == 'Dark') {
            dispatch(onThemeChange('Light'))
        }
        else {
            dispatch(onThemeChange('Dark'))
        }
        
    }
    return(
        <nav className="Landing-page-navbar container">
            <div className="logo">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="hamburger text" viewBox="0 0 16 16" onClick={NavbarSwitch}>
                    <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
                </svg>
                <h1 className="logo"><Link to='/' className="logoLink text">Conjugat</Link></h1>
            </div>
            <div className={`options${navbarOpen? ' show-menu container' : ''}`}>
                <Link to='/Contact' ><p className="link text-gold-link">Contact</p></Link>
                <Link to='/Faq' ><p className="link text-gold-link">Faq</p></Link>
                <Link to='/Privacy' ><p className="link text-gold-link">Privacy</p></Link>
                <Link to='/Terms' ><p className="link text-gold-link">Terms</p></Link>
            </div>
            <div className={`settings${navbarOpen? ' show-menu container' : ''}`}>
                <Link to='/' ><p className="link text-blue-link" onClick={ThemeSwitch}>Theme</p></Link>
                <Link to='/' ><p className="link text-gold-link">Language</p></Link>
                <Link to='/Premium' ><p className="link text-gold-link">Premium</p></Link>
            </div>
            <div className={`login-div${navbarOpen? ' show-menu container' : ''}`}><Link to='/account/Login' >
                <p className="login strong-gold-btn">Log in</p>
            </Link></div>
        </nav>
    )
}

export default Navbar