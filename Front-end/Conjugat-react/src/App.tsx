import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
import { lazy, Suspense } from 'react'
import './index.css'

// pages
import Index from './pages/home/LandingPage'
const Contact = lazy(() => import('./pages/home/Contact'))
const Faq = lazy(() => import('./pages/home/FAQs'))
const Home = lazy(() => import('./pages/home/Home'))
const Privacy = lazy(() => import('./pages/home/Privacy'))
const Terms = lazy(() => import('./pages/home/Terms'))
const PremiumInfo = lazy(() => import('./pages/home/PremiumInfo'))

const Login = lazy(() => import('./pages/account/Login'))
const OauthLogin = lazy(() => import('./pages/account/OauthLogin'))
const Logout = lazy(() => import('./pages/account/Logout'))
const PasswordReset = lazy(() => import('./pages/account/PasswordReset'))
const PasswordResetToken = lazy(() => import('./pages/account/PasswordResetToken'))
const Register = lazy(() => import('./pages/account/Register'))
const Activate = lazy(() => import('./pages/account/Activate'))

const Newsletter = lazy(() => import('./pages/newsletter/Newsletter'))
const Subscribe = lazy(() => import('./pages/newsletter/Subscribe'))
const Unsubscribe = lazy(() => import('./pages/newsletter/Unsubscribe'))

const Settings = lazy(() => import('./pages/settings/Settings'))
const Email = lazy(() => import('./pages/settings/ChangeEmail'))
const Password = lazy(() => import('./pages/settings/ChangePassword'))
const Username = lazy(() => import('./pages/settings/ChangeUsername'))
const LogoutAll = lazy(() => import('./pages/settings/LogoutAll'))
const Account = lazy(() => import('./pages/settings/CloseAccount'))
const Premium = lazy(() => import('./pages/settings/Premium'))
const ResetAccount = lazy(() => import('./pages/settings/ResetAccount'))
const Themes = lazy(() => import('./pages/settings/Themes'))
const TwoFactorAuth = lazy(() => import('./pages/settings/TwoFactorAuth'))


const Subscriptions = lazy(() => import('./pages/subscriptions/Subscriptions'))
const Cancelled = lazy(() => import('./pages/subscriptions/Cancelled'))
const Process = lazy(() => import('./pages/subscriptions/Process'))
const Success = lazy(() => import('./pages/subscriptions/Success'))

const Test = lazy(() => import('./pages/test/Test'))
const TestResults = lazy(() => import('./pages/test/TestResults'))

import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

import './sass/app.scss'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route index element={<Index />} />
      <Route path="contact" element={<Suspense fallback=''><Contact /></Suspense>} />
      <Route path="faq" element={<Suspense fallback=''><Faq /></Suspense>} />
      <Route path="home" element={<Suspense fallback=''><Home /></Suspense>} />
      <Route path="privacy" element={<Suspense fallback=''><Privacy /></Suspense>} />
      <Route path="terms" element={<Suspense fallback=''><Terms /></Suspense>} />
      <Route path="premium" element={<Suspense fallback=''><PremiumInfo /></Suspense>} />


      <Route path="account">
        <Route path="login" element={<Suspense fallback=''><Login /></Suspense>} />
        <Route path="oauth" element={<Suspense fallback=''><OauthLogin /></Suspense>} />
        <Route path="logout" element={<Suspense fallback=''><Logout /></Suspense>} />

        <Route path="password-reset" element={<Suspense fallback=''><PasswordReset /></Suspense>} />
        <Route path="password-reset/:uidb64/:token" element={<Suspense fallback=''><PasswordResetToken /></Suspense>} />

        <Route path="register" element={<Suspense fallback=''><Register /></Suspense>} />
        <Route path="activate/:uidb64/:token" element={<Suspense fallback=''><Activate /></Suspense>} />
      </Route>


      <Route path="newsletter" element={<Suspense fallback=''><Newsletter /></Suspense>}>
        <Route path="subscribe" element={<Suspense fallback=''><Subscribe /></Suspense>} />
        <Route path="unsubscribe" element={<Suspense fallback=''><Unsubscribe /></Suspense>} />
      </Route>


      <Route path="settings" element={<Suspense fallback=''><Settings /></Suspense>}>
        <Route path="change-email" element={<Suspense fallback=''><Email /></Suspense>} />
        <Route path="change-password" element={<Suspense fallback=''><Password /></Suspense>} />
        <Route path="change-username" element={<Suspense fallback=''><Username /></Suspense>} />

        <Route path="logout-all" element={<Suspense fallback=''><LogoutAll /></Suspense>} />
        <Route path="reset-account" element={<Suspense fallback=''><ResetAccount /></Suspense>} />
        <Route path="close-account" element={<Suspense fallback=''><Account /></Suspense>} />

        <Route path="premium" element={<Suspense fallback=''><Premium /></Suspense>} />

        <Route path="themes" element={<Suspense fallback=''><Themes /></Suspense>} />
        <Route path="two-factor-auth" element={<Suspense fallback=''><TwoFactorAuth /></Suspense>} />
      </Route>


      <Route path="subscriptions" element={<Suspense fallback=''><Subscriptions /></Suspense>}>
        <Route path="cancelled" element={<Suspense fallback=''><Cancelled /></Suspense>} />
        <Route path="process" element={<Suspense fallback=''><Process /></Suspense>} />
        <Route path="success" element={<Suspense fallback=''><Success /></Suspense>} />
      </Route>

      <Route path="verbs">
        <Route path="test" element={<Suspense fallback=''><Test /></Suspense>} />
        <Route path="test/results/:testID" element={<Suspense fallback=''><TestResults /></Suspense>} />
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
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)
  

  const{ theme } = useSelector((state: RootState) => state.persistedReducer.theme)
  if (theme == 'Dark') {
    document.body.setAttribute('style', 'background: #060607;');
    // document.body.style = 'background: #060607;'
  }
  else if (theme == 'Light') {
    document.body.setAttribute('style', 'background: #ffffff;');
    // document.body.style = 'background: #ffffff;'
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