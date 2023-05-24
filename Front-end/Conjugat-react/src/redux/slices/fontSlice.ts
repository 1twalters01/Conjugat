import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface FontState {
  font: string
}
const initialState: FontState = {
  font: 'English'
}

export const fontSlice = createSlice({
  name: 'font',
  initialState,
  reducers: {
    onFontChange:(state, action: PayloadAction<string>) => {
        state.font = action.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { onFontChange } = fontSlice.actions

export default fontSlice.reducer