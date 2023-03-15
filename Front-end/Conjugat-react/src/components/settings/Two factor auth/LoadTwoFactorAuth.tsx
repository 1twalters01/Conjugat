import { useState } from "react"

import AxiosInstance from "../../../functions/AxiosInstance"
import Qrcode from "./QrCode"
import QrForm from "./QrForm"


function LoadTwoFactorAuth({setDone, loading, setLoading}: {setDone:Function, loading:boolean, setLoading:Function}) {
    const [qrString, setQrString] = useState("")
  
    if (loading) {
      AxiosInstance.Authorised
      .get('settings/two-factor-auth/')
      .then(res =>{
        setQrString(res.data.qr_string)
        setLoading(false)
      })
      return <></>
    }
    return (
      <>
        <Qrcode
          qrString = {qrString}
        />
        <QrForm
          setDone={setDone}
        />
      </>
    )
}

export default LoadTwoFactorAuth