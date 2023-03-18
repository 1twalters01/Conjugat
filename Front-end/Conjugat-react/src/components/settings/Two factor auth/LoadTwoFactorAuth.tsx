import { useEffect, useState } from "react"

import AxiosInstance from "../../../functions/AxiosInstance"
import Qrcode from "./QrCode"
import QrForm from "./QrForm"


function LoadTwoFactorAuth({setDone }: {setDone:Function}) {
    const [qrString, setQrString] = useState("")

    const fetchdata = async () => {
      const res = await (
        AxiosInstance.Authorised
        .get('settings/two-factor-auth/')
      )
      setQrString(res.data.qr_string)  
    }

    useEffect(() => {
      fetchdata();
    }, [])

    if (qrString!= '') {
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
    return <></>
}

export default LoadTwoFactorAuth