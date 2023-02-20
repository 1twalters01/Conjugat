import { Outlet, NavLink } from "react-router-dom"

function RootLayout() {
    return(
        <div className="root-layout">
            <header>
                <nav>
                    <NavLink to="/">Landing page</NavLink>
                    <NavLink to="contact">Contact</NavLink>
                    <NavLink to="faq">FAQs</NavLink>
                    <NavLink to="home">Home</NavLink>
                    <NavLink to="privacy">Privacy</NavLink>
                    <NavLink to="terms">Terms</NavLink>

                    <NavLink to="account">Account</NavLink>
                    <NavLink to="newsletter">Newsletter</NavLink>
                    <NavLink to="settings">Settings</NavLink>
                    <NavLink to="subscriptions">Subscriptions</NavLink>
                </nav>
            </header>
            <main>
                <Outlet />
            </main>
        </div>
    )
}

export default RootLayout