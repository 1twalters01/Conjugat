import QRCode from "react-qr-code"

function Qrcode({qrString}: { qrString:string}) {
    return(
      <div style={{ background: 'white', padding: '10px' }}>
        { qrString == "" ?
        <div style={{ height: '260px'}}></div>
        :
        <QRCode value={qrString} />
        }
        
      </div>
    )
}

export default Qrcode