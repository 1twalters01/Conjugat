import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface TokenState {
  token: string
}
const initialState: TokenState = {
  token: 'Light'
}

export const tokenSlice = createSlice({
  name: 'token',
  initialState,
  reducers: {
    onTokenChange:(state, action: PayloadAction<string>) => {
        state.token = action.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { onTokenChange } = tokenSlice.actions

export default tokenSlice.reducer