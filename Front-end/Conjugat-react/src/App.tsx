import './App.css'
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import './index.css'

// Layouts
import AccountLayout from './layouts/AccountLayout'
import NewsletterLayout from './layouts/NewsletterLayout'
import SettingsLayout from './layouts/SettingsLayout'
import SubscriptionsLayout from './layouts/SubscriptionsLayout'

// pages
import Index from './pages/LandingPage'
import Contact from './pages/Contact'
import Faq from './pages/FAQs'
import Home from './pages/Home'
import Privacy from './pages/Privacy'
import Terms from './pages/Terms'

import Login from './pages/account/Login'
import Logout from './pages/account/Logout'
import PasswordReset from './pages/account/PasswordReset'
import PasswordResetToken from './pages/account/PasswordResetToken'
import Register from './pages/account/Register'
import Activate from './pages/account/Activate'

import Subscribe from './pages/newsletter/Subscribe'
import Unsubscribe from './pages/newsletter/Unsubscribe'

import Email from './pages/settings/ChangeEmail'
import Password from './pages/settings/ChangePassword'
import Username from './pages/settings/ChangeUsername'
import Account from './pages/settings/CloseAccount'
import Premium from './pages/settings/Premium'
import ResetAccount from './pages/settings/ResetAccount'
import Themes from './pages/settings/Themes'
import TwoFactorAuth from './pages/settings/TwoFactorAuth'

import Cancelled from './pages/subscriptions/Cancelled'
import Process from './pages/subscriptions/Process'
import Success from './pages/subscriptions/Success'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route index element={<Index />} />
      <Route path="contact" element={<Contact />} />
      <Route path="faq" element={<Faq />} />
      <Route path="home" element={<Home />} />
      <Route path="privacy" element={<Privacy />} />
      <Route path="terms" element={<Terms />} />


      <Route path="account" element={<AccountLayout />}>
        <Route path="login" element={<Login />} />
        <Route path="logout" element={<Logout />} />

        <Route path="password-reset" element={<PasswordReset />} />
        <Route path="password-reset/:uidb64/:token" element={<PasswordResetToken />} />

        <Route path="register" element={<Register />} />
        <Route path="activate/:uidb64/:token" element={<Activate />} />
      </Route>


      <Route path="newsletter" element={<NewsletterLayout />}>
        <Route path="subscribe" element={<Subscribe />} />
        <Route path="unsubscribe" element={<Unsubscribe />} />
      </Route>


      <Route path="settings" element={<SettingsLayout />}>
        <Route path="change-email" element={<Email />} />
        <Route path="change-password" element={<Password />} />
        <Route path="change-username" element={<Username />} />

        <Route path="reset-account" element={<ResetAccount />} />
        <Route path="close-account" element={<Account />} />

        <Route path="premium" element={<Premium />} />

        <Route path="themes" element={<Themes />} />
        <Route path="two-factor-auth" element={<TwoFactorAuth />} />
      </Route>


      <Route path="subscriptions" element={<SubscriptionsLayout />}>
        <Route path="cancelled" element={<Cancelled />} />
        <Route path="process" element={<Process />} />
        <Route path="success" element={<Success />} />
      </Route>
    </Route>
  )
)

function App() {
  return (
    <RouterProvider router={router} />
  )
}

export default App