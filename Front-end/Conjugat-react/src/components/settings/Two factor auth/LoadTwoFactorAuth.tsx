import { useEffect, useState } from "react"

import AxiosInstance from "../../../functions/AxiosInstance"
import Qrcode from "./QrCode"
import QrForm from "./QrForm"
import '../../../sass/Components/settings/Two factor auth/LoadTwoFactorAuth.scss'


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
        <div className="Load-2FA-container">
            <div className="QrCode">
                <Qrcode
                qrString = {qrString}
                />
            </div>
          
            <QrForm
            setDone={setDone}
            />
        </div>
      )
    }
    return <></>
}

export default LoadTwoFactorAuth