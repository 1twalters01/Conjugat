import { Link } from "react-router-dom"
import '../../sass/Components/home/MiscNavbar.scss'

function MiscNavbar(){
    return(
        <div className="Misc-navbar">
            <Link to='/Contact' ><p className="nav-link text-blue-link">Contact</p></Link>
            <Link to='/Faq' ><p className="nav-link text-blue-link">FAQ</p></Link>
            <Link to='/Privacy' ><p className="nav-link text-blue-link">Privacy</p></Link>
            <Link to='/Terms' ><p className="nav-link text-blue-link">Terms</p></Link>
            <Link to='/Premium' ><p className="nav-link text-blue-link">Premium</p></Link>
        </div>
    )
}

export default MiscNavbar