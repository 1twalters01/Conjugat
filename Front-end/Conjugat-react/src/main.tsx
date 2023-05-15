import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

import { store } from './redux/store'
import { Provider } from 'react-redux'
import { HelmetProvider } from 'react-helmet-async'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
    <React.StrictMode>
        <Provider store={store}>
            <HelmetProvider>
                <App />
            </HelmetProvider>
        </Provider>
    </React.StrictMode>,
)
