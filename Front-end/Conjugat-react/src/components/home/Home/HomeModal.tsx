import { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";

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
    // display: 'flex',
    // justifyContent: 'center',
    // alignItems: 'center',
    zIndex: 1000,
    overflowY: 'auto',
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
    function CorrectClick() {

    }

    function IncorrectClick() {

    }
    
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
        console.log(modalData.modalFetchedData[0].Test[0].Subjects)
        return ReactDOM.createPortal(
            <>
                <div style={overlay_styles}/>

                <div ref={HomeModalRef} style={Modal_styles}>
                    <div>
                        <p className={`${modalData.correct == true? ' correct': ''}`} onClick={CorrectClick}>Correct</p>
                        <p className={`${modalData.incorrect == true? ' incorrect': ''}`} onClick={IncorrectClick}>Incorrect</p>
                    </div>

                    <p style={{'color':'white', 'padding':'20px'}}>
                        {modalData.modalFetchedData.map((data:any, i:number) => (
                            <>
                                <Link to={`/verbs/test/results/${data.TestID}`}>Test {i+1}</Link>
                                {data.Test.map((res:any, j:any) => (
                                    <>
                                        <p>{res.Base}</p>
                                            {res.Subjects.map((subject:any, k:any) => (
                                                <>
                                                    <p className={`${res.Status == true? ' isCorrect': ' isFalse'}`}>
                                                        {subject} {res.Auxiliaries[k]} {res.Conjugations[k]}
                                                    </p>
                                                </>
                                            ))}
                                    </>
                                ))}
                            </>
                        ))}
                    </p>
                </div>    
            </>,
            document.getElementById('portal')!
        )
        
    }
}

export default HomeModal