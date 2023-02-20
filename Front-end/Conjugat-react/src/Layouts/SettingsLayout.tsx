import { Outlet, NavLink } from "react-router-dom"

function SettingsLayout() {
    return(
        <div className="root-layout">
            <header>
                <nav>
                    <NavLink to="/">Landing page</NavLink>
                    <NavLink to="change-email">Change email</NavLink>
                    <NavLink to="change-password">Change password</NavLink>
                    <NavLink to="change-username">Change username</NavLink>
                    <NavLink to="close-account">Close account</NavLink>
                    <NavLink to="premium">Premium</NavLink>

                    <NavLink to="reset-account">Reset account</NavLink>
                    <NavLink to="themes">Themes</NavLink>
                    <NavLink to="two-factor-auth">2FA</NavLink>
                </nav>
            </header>
            <main>
                <Outlet />
            </main>
        </div>
    )
}

export default SettingsLayout