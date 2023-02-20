import { Outlet, NavLink } from "react-router-dom"

function NewsletterLayout() {
    return(
        <div className="root-layout">
            <header>
                <nav>
                    <NavLink to="/">Landing page</NavLink>
                    <NavLink to="subscribe">Subscribe</NavLink>
                    <NavLink to="unsubscribe">Unsubscribe</NavLink>
                </nav>
            </header>
            <main>
                <Outlet />
            </main>
        </div>
    )
}

export default NewsletterLayout