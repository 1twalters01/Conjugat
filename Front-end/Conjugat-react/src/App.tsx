import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
import { lazy, Suspense } from 'react'
import './index.css'

// pages

// import Index from './pages/home/LandingPage'
// const Index = lazy(() => import('./pages/home/LandingPage'))
const IndexPromise = import('./pages/home/LandingPage');
const Index = lazy(() => IndexPromise);
// const Contact = lazy(() => import('./pages/home/Contact'))
const ContactPromise = import('./pages/home/Contact');
const Contact = lazy(() => ContactPromise);
// const Faq = lazy(() => import('./pages/home/FAQs'))
const FaqPromise = import('./pages/home/FAQs');
const Faq = lazy(() => FaqPromise);
// const Home = lazy(() => import('./pages/home/Home'))
const HomePromise = import('./pages/home/Home');
const Home = lazy(() => HomePromise);
// const Privacy = lazy(() => import('./pages/home/Privacy'))
const PrivacyPromise = import('./pages/home/Privacy');
const Privacy = lazy(() => PrivacyPromise);
// const Terms = lazy(() => import('./pages/home/Terms'))
const TermsPromise = import('./pages/home/Terms');
const Terms = lazy(() => TermsPromise);
// const PremiumInfo = lazy(() => import('./pages/home/PremiumInfo'))
const PremiumInfoPromise = import('./pages/home/PremiumInfo');
const PremiumInfo = lazy(() => PremiumInfoPromise);


// const Login = lazy(() => import('./pages/account/Login'))
const LoginPromise = import('./pages/account/Login');
const Login = lazy(() => LoginPromise);
// const OauthLogin = lazy(() => import('./pages/account/OauthLogin'))
const OauthLoginPromise = import('./pages/account/OauthLogin');
const OauthLogin = lazy(() => OauthLoginPromise);
// const Logout = lazy(() => import('./pages/account/Logout'))
const LogoutPromise = import('./pages/account/Logout');
const Logout = lazy(() => LogoutPromise);
// const PasswordReset = lazy(() => import('./pages/account/PasswordReset'))
const PasswordResetPromise = import('./pages/account/PasswordReset');
const PasswordReset = lazy(() => PasswordResetPromise);
// const PasswordResetToken = lazy(() => import('./pages/account/PasswordResetToken'))
const PasswordResetTokenPromise = import('./pages/account/PasswordResetToken');
const PasswordResetToken = lazy(() => PasswordResetTokenPromise);
// const Register = lazy(() => import('./pages/account/Register'))
const RegisterPromise = import('./pages/account/Register');
const Register = lazy(() => RegisterPromise);
// const Activate = lazy(() => import('./pages/account/Activate'))
const ActivatePromise = import('./pages/account/Activate');
const Activate = lazy(() => ActivatePromise);


// const Newsletter = lazy(() => import('./pages/newsletter/Newsletter'))
const NewsletterPromise = import('./pages/newsletter/Newsletter');
const Newsletter = lazy(() => NewsletterPromise);
// const Subscribe = lazy(() => import('./pages/newsletter/Subscribe'))
const SubscribePromise = import('./pages/newsletter/Subscribe');
const Subscribe = lazy(() => SubscribePromise);
// const Unsubscribe = lazy(() => import('./pages/newsletter/Unsubscribe'))
const UnsubscribePromise = import('./pages/newsletter/Unsubscribe');
const Unsubscribe = lazy(() => UnsubscribePromise);

// const Settings = lazy(() => import('./pages/settings/Settings'))
const SettingsPromise = import('./pages/settings/Settings');
const Settings = lazy(() => SettingsPromise);
// const Email = lazy(() => import('./pages/settings/ChangeEmail'))
const EmailPromise = import('./pages/settings/ChangeEmail');
const Email = lazy(() => EmailPromise);
// const Password = lazy(() => import('./pages/settings/ChangePassword'))
const PasswordPromise = import('./pages/settings/ChangePassword');
const Password = lazy(() => PasswordPromise);
// const Username = lazy(() => import('./pages/settings/ChangeUsername'))
const UsernamePromise = import('./pages/settings/ChangeUsername');
const Username = lazy(() => UsernamePromise);
// const Font = lazy(() => import('./pages/settings/Font'))
const FontPromise = import('./pages/settings/Font');
const Font = lazy(() => FontPromise);
// const Language = lazy(() => import('./pages/settings/Language'))
const LanguagePromise = import('./pages/settings/Language');
const Language = lazy(() => LanguagePromise);
// const LogoutAll = lazy(() => import('./pages/settings/LogoutAll'))
const LogoutAllPromise = import('./pages/settings/LogoutAll');
const LogoutAll = lazy(() => LogoutAllPromise);
// const Account = lazy(() => import('./pages/settings/CloseAccount'))
const AccountPromise = import('./pages/settings/CloseAccount');
const Account = lazy(() => AccountPromise);
// const Premium = lazy(() => import('./pages/settings/Premium'))
const PremiumPromise = import('./pages/settings/Premium');
const Premium = lazy(() => PremiumPromise);
// const ResetAccount = lazy(() => import('./pages/settings/ResetAccount'))
const ResetAccountPromise = import('./pages/settings/ResetAccount');
const ResetAccount = lazy(() => ResetAccountPromise);
// const Themes = lazy(() => import('./pages/settings/Themes'))
const ThemesPromise = import('./pages/settings/Themes');
const Themes = lazy(() => ThemesPromise);
// const TwoFactorAuth = lazy(() => import('./pages/settings/TwoFactorAuth'))
const TwoFactorAuthPromise = import('./pages/settings/TwoFactorAuth');
const TwoFactorAuth = lazy(() => TwoFactorAuthPromise);


// const Subscriptions = lazy(() => import('./pages/subscriptions/Subscriptions'))
const SubscriptionsPromise = import('./pages/newsletter/Unsubscribe');
const Subscriptions = lazy(() => SubscriptionsPromise);
// const Cancelled = lazy(() => import('./pages/subscriptions/Cancelled'))
const CancelledPromise = import('./pages/newsletter/Unsubscribe');
const Cancelled = lazy(() => CancelledPromise);
// const Process = lazy(() => import('./pages/subscriptions/Process'))
const ProcessPromise = import('./pages/newsletter/Unsubscribe');
const Process = lazy(() => ProcessPromise);
// const Success = lazy(() => import('./pages/subscriptions/Success'))
const SuccessPromise = import('./pages/newsletter/Unsubscribe');
const Success = lazy(() => SuccessPromise);

// const Test = lazy(() => import('./pages/test/Test'))
const TestPromise = import('./pages/newsletter/Unsubscribe');
const Test = lazy(() => TestPromise);
// const TestOptions = lazy(() => import('./pages/test/TestOptions'))
const TestOptionsPromise = import('./pages/newsletter/Unsubscribe');
const TestOptions = lazy(() => TestOptionsPromise);
// const TestResults = lazy(() => import('./pages/test/TestResults'))
const TestResultsPromise = import('./pages/newsletter/Unsubscribe');
const TestResults = lazy(() => TestResultsPromise);

import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

import './sass/app.scss'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route index element={<Suspense fallback=''><Index /></Suspense>} />
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

        <Route path="font" element={<Suspense fallback=''><Font /></Suspense>} />
        <Route path="language" element={<Suspense fallback=''><Language /></Suspense>} />

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

      <Route path="test">
        <Route path="options" element={<Suspense fallback=''><TestOptions /></Suspense>} />
        <Route path="" element={<Suspense fallback=''><Test /></Suspense>} />
        <Route path="results/:testID" element={<Suspense fallback=''><TestResults /></Suspense>} />
      </Route>

    </Route>
  )
)

import { Provider, useSelector } from "react-redux"
import { RootState, store } from "./redux/store"
import { PersistGate } from "redux-persist/integration/react"
import { persistStore } from "redux-persist"

var persistor = persistStore(store)

function App() {
  const { headerFont } = useSelector((state: RootState) => state.persistedReducer.font)
  const { bodyFont } = useSelector((state: RootState) => state.persistedReducer.font)
  const { theme } = useSelector((state: RootState) => state.persistedReducer.theme)

  if (theme == 'Dark') {
    document.body.setAttribute('style', 'background: #060607;');
  }
  else if (theme == 'Light') {
    document.body.setAttribute('style', 'background: #ffffff;');
  }

  return (
    <Provider store={store}>
      <div className={`${theme} ${bodyFont} ${headerFont}-header`}>
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