import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
import './index.css'

// pages
import Index from './pages/home/LandingPage'
import Contact from './pages/home/Contact'
import Faq from './pages/home/FAQs'
import Home from './pages/home/Home'
import Privacy from './pages/home/Privacy'
import Terms from './pages/home/Terms'
import PremiumInfo from "./pages/home/PremiumInfo";

import Login from './pages/account/Login'
import OauthLogin from "./pages/account/OauthLogin";
import Logout from './pages/account/Logout'
import PasswordReset from './pages/account/PasswordReset'
import PasswordResetToken from './pages/account/PasswordResetToken'
import Register from './pages/account/Register'
import Activate from './pages/account/Activate'

import Newsletter from "./pages/newsletter/Newsletter";
import Subscribe from './pages/newsletter/Subscribe'
import Unsubscribe from './pages/newsletter/Unsubscribe'

import Settings from "./pages/settings/Settings";
import Email from './pages/settings/ChangeEmail'
import Password from './pages/settings/ChangePassword'
import Username from './pages/settings/ChangeUsername'
import LogoutAll from "./pages/settings/LogoutAll";
import Account from './pages/settings/CloseAccount'
import Premium from './pages/settings/Premium'
import ResetAccount from './pages/settings/ResetAccount'
import Themes from './pages/settings/Themes'
import TwoFactorAuth from './pages/settings/TwoFactorAuth'

import Subscriptions from "./pages/subscriptions/Subscriptions";
import Cancelled from './pages/subscriptions/Cancelled'
import Process from './pages/subscriptions/Process'
import Success from './pages/subscriptions/Success'

import Test from "./pages/verbs/Test";
import TestResults from "./pages/verbs/TestResults";

import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

import './sass/app.scss'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route index element={<Index />} />
      <Route path="contact" element={<Contact />} />
      <Route path="faq" element={<Faq />} />
      <Route path="home" element={<Home />} />
      <Route path="privacy" element={<Privacy />} />
      <Route path="terms" element={<Terms />} />
      <Route path="premium" element={<PremiumInfo />} />


      <Route path="account">
        <Route path="login" element={<Login />} />
        <Route path="oauth" element={<OauthLogin />} />
        <Route path="logout" element={<Logout />} />

        <Route path="password-reset" element={<PasswordReset />} />
        <Route path="password-reset/:uidb64/:token" element={<PasswordResetToken />} />

        <Route path="register" element={<Register />} />
        <Route path="activate/:uidb64/:token" element={<Activate />} />
      </Route>


      <Route path="newsletter" element={<Newsletter />}>
        <Route path="subscribe" element={<Subscribe />} />
        <Route path="unsubscribe" element={<Unsubscribe />} />
      </Route>


      <Route path="settings" element={<Settings />}>
        <Route path="change-email" element={<Email />} />
        <Route path="change-password" element={<Password />} />
        <Route path="change-username" element={<Username />} />

        <Route path="logout-all" element={<LogoutAll />} />
        <Route path="reset-account" element={<ResetAccount />} />
        <Route path="close-account" element={<Account />} />

        <Route path="premium" element={<Premium />} />

        <Route path="themes" element={<Themes />} />
        <Route path="two-factor-auth" element={<TwoFactorAuth />} />
      </Route>


      <Route path="subscriptions" element={<Subscriptions />}>
        <Route path="cancelled" element={<Cancelled />} />
        <Route path="process" element={<Process />} />
        <Route path="success" element={<Success />} />
      </Route>

      <Route path="verbs">
        <Route path="test" element={<Test />} />
        <Route path="test/results/:testID" element={<TestResults />} />
      </Route>

    </Route>
  )
)

import { Provider, useSelector } from "react-redux"
import { RootState, store } from './redux/store';
import { PersistGate } from "redux-persist/integration/react"
import { persistStore } from "redux-persist"

var persistor = persistStore(store)

function App() {
  const{ theme } = useSelector((state: RootState) => state.persistedReducer.theme)
  if (theme == 'Dark') {
     document.body.style = 'background: #060607;'
  }
  else if (theme == 'Light') {
    document.body.style = 'background: #ffffff;'
  }
  return (
    <Provider store={store}>
      <div className={theme}>
        <PersistGate persistor={persistor}>
          <RouterProvider router={router} />
        </PersistGate>
      </div>
      {theme == 'Dark' ?
        <ToastContainer
          position="top-right"
          autoClose={2000}
          theme='colored'
        />
      :
        <ToastContainer
          position="top-right"
          autoClose={2000}
          theme='light'
        />
      }
    </Provider>
  )
}

export default App