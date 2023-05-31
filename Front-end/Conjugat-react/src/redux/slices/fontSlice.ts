import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface FontState {
  headerFont: string,
  bodyFont: string
}
const initialState: FontState = {
  headerFont: 'Open-Dyslexic',
  bodyFont: 'Open-Dyslexic'
}

export const fontSlice = createSlice({
  name: 'font',
  initialState,
  reducers: {
    onHeaderFontChange:(state, action: PayloadAction<string>) => {
        state.headerFont = action.payload
    },
    onBodyFontChange:(state, action: PayloadAction<string>) => {
        state.bodyFont = action.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { onHeaderFontChange, onBodyFontChange } = fontSlice.actions

export default fontSlice.reducer