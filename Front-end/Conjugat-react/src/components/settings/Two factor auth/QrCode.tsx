import { useState } from "react";
import QRCode from "react-qr-code"

function Qrcode({qrString}: { qrString:string}) {
    var init_width
    if (window.innerWidth > 1201) {
      init_width = 250
    }
    else{
      init_width = window.innerWidth/4.8
    }

    const [qrSize, SetQrSize] = useState(init_width)
    function resizeFunction() {
        var width = window.innerWidth
        if (width > 1201){
            SetQrSize(250)
        }
        else {
          SetQrSize(width/4.8)
        }
    }

    window.addEventListener("resize", resizeFunction);
    
    



    return(
      <div className='QRCode-container'>
        { qrString == "" ?
        <div style={{ height: `${qrSize}`}}></div>
        :
        <div style={{border: '3px solid #fff', width: `${qrSize+6}px`, height: `${qrSize+6}px`, margin:'auto'}}>
            <QRCode value={qrString} size={qrSize}/>
        </div>
        
        }
        
      </div>
    )
}

export default Qrcode