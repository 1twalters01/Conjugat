import { ChangeEvent } from "react"

function handleText(e:ChangeEvent<HTMLInputElement>, setText:Function) {
    setText(e.target.value)
}

export default handleText