import QRCode from "react-qr-code"
import '../../../sass/Components/settings/Two factor auth/QrCode.scss'

function Qrcode({qrString}: { qrString:string}) {
    return(
      <div className='QRCode-container'>
        { qrString == "" ?
        <div style={{ height: '260px'}}></div>
        :
        <QRCode value={qrString} />
        }
        
      </div>
    )
}

export default Qrcode