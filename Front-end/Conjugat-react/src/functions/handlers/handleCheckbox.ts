import { ChangeEvent } from "react";

function handleCheckbox(e:ChangeEvent<HTMLInputElement>, setRememberMe:Function) {
    setRememberMe(e.target.checked)
}

export default handleCheckbox