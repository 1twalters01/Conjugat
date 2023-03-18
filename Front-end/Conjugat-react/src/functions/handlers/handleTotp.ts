import { ChangeEvent } from "react"

function handleTotp(e:ChangeEvent<HTMLInputElement>, setTotp:Function) {
    if (isNaN(+e.target.value) == false){
        setTotp(e.target.value)
    }
}

export default handleTotp