import { Outlet, NavLink } from "react-router-dom"

function SubscriptionsLayout() {
    return(
        <div className="root-layout">
            <header>
                <nav>
                    <NavLink to="/">Landing page</NavLink>
                    <NavLink to="cancelled">cancelled</NavLink>
                    <NavLink to="process">process</NavLink>
                    <NavLink to="success">success</NavLink>
                </nav>
            </header>
            <main>
                <Outlet />
            </main>
        </div>
    )
}

export default SubscriptionsLayout