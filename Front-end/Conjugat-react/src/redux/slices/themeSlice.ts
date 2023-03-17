import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface ThemeState {
  theme: string
}
const initialState: ThemeState = {
  theme: 'Light'
}

export const themeSlice = createSlice({
  name: 'theme',
  initialState,
  reducers: {
    onThemeChange:(state, action: PayloadAction<string>) => {
        state.theme = action.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { onThemeChange } = themeSlice.actions

export default themeSlice.reducer