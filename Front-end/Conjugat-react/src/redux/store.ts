import { configureStore } from '@reduxjs/toolkit'
import loginReducer from './slices/loginSlice'
import themeReducer from './slices/themeSlice'
import tokenReducer from './slices/tokenSlice'

import thunk from 'redux-thunk';
import { combineReducers } from '@reduxjs/toolkit';
import { persistReducer, persistStore } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

const persistConfig = {
  key: 'root',
  version: 1,
  storage,
}

const reducer = combineReducers({
  login: loginReducer,
  theme: themeReducer,
  token: tokenReducer
})

const persistedReducer = persistReducer(persistConfig, reducer)

export const store = configureStore({
  reducer: {
    persistedReducer,
  },
  middleware: [thunk],
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

export const persistor = persistStore(store)