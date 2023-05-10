import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface LanguageState {
  language: string
}
const initialState: LanguageState = {
  language: 'Dark'
}

export const languageSlice = createSlice({
  name: 'language',
  initialState,
  reducers: {
    onLanguageChange:(state, action: PayloadAction<string>) => {
        state.language = action.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { onLanguageChange } = languageSlice.actions

export default languageSlice.reducer