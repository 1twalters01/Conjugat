import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface LoginState {
  username: string
  id: number|null
  confirmed: boolean|null
}
const initialState: LoginState = {
  username: '',
  id: null,
  confirmed: null
}

export const loginSlice = createSlice({

  name: 'login',
  initialState,
  reducers: {
    onUsernameChange:(state, action: PayloadAction<string>) => {
      state.username = action.payload
    },
    onIdChange:(state, action: PayloadAction<number|null>) => {
        state.id = action.payload
    },
    onConfirmedChange:(state, action: PayloadAction<boolean|null>) => {
      state.confirmed = action.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { onUsernameChange, onIdChange, onConfirmedChange } = loginSlice.actions

export default loginSlice.reducer