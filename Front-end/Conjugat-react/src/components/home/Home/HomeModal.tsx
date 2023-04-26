import { useEffect, useRef } from "react";
import ReactDOM from "react-dom";

const Modal_styles = {
    position: 'fixed',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    'padding': '50px',
    backgroundColor: 'grey',
    height: '620px',
    width: '900px',
    textAlign: 'center',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000
}

const overlay_styles = {
    position: 'fixed',
    top: 0,
    left: 0,
    bottom: 0,
    right: 0,
    backgroundColor: 'rgba(0, 0, 0, .7)',
    zIndex: 1000
}


function HomeModal({ modalData, open, setOpen }: {modalData: any, open: boolean, setOpen: Function}) {
    function useOutsideAlerter(ref: any) {
        useEffect(() => {
          /**
           * Alert if clicked on outside of element
           */
          function handleClickOutside(event: { target: any; }) {
            if (ref.current && !ref.current.contains(event.target)) {
                setOpen(false)
            }
          }
          // Bind the event listener
          document.addEventListener("mousedown", handleClickOutside);
          return () => {
            // Unbind the event listener on clean up
            document.removeEventListener("mousedown", handleClickOutside);
          };
        }, [ref]);
      }
      
    const HomeModalRef = useRef<HTMLDivElement>(null)
    useOutsideAlerter(HomeModalRef);
    if (!open){
        return null
    }
    else{
        return ReactDOM.createPortal(
            <>
                <div style={overlay_styles}/>
                <div ref={HomeModalRef} style={Modal_styles}>
                    <p style={{'color':'white', 'padding':'20px'}}>
                        {modalData.status}
                    </p>
                    <p style={{'color':'white', 'padding':'20px'}}>
                        {/* {modalData.modalFetchedData} */}
                    </p>
                </div>    
            </>,
            document.getElementById('portal')!
        )
        
    }
}

export default HomeModal