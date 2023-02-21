import { Outlet, NavLink } from "react-router-dom"

function AccountLayout() {
    return(
        <div className="root-layout">
            <header>
                <nav>
                    <NavLink to="/">Landing page</NavLink>
                    <NavLink to="login">Login</NavLink>
                    <NavLink to="logout">Logout</NavLink>
                    <NavLink to="password-reset">Password-reset</NavLink>
                    <NavLink to="register">Register</NavLink>
                </nav>
            </header>
            <main>
                <Outlet />
            </main>
        </div>
    )
}

export default AccountLayout