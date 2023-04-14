import { ChangeEvent, useRef, useState } from 'react'
import '../../sass/Components/verbs/Test/TestSlideshow.scss'

function TextSlideshow({setPage, QuestionData, i} : {setPage:Function, QuestionData:any, i:number}) {
    const [InputNumber, setInputNumber] = useState('')
    function handlePrevious(i:number) {
        if (i > 0) {
            setPage(i - 1)
        }
    }

    const numInput = useRef<HTMLInputElement>(null);
    function handleNumberSubmit(e:ChangeEvent<HTMLInputElement>) {
        if (e.key === 'Enter') {
            if (isNaN(+e.target.value) == false && +e.target.value > 0 && e.target.value < QuestionData.length+1 && numInput.current) {
                setPage(+e.target.value - 1)
                numInput.current.value = ''
            }
        }
    }

    function handleNext(i:number) {
        if (i < QuestionData.length-1) {
            setPage(i + 1)
        }
    }

    return (
        <div className="Test-Slideshow-container">
            <div className="link weak-gold-btn" onClick={() =>handlePrevious(i)}>Previous</div>
            <input type="number" name="" ref={numInput} id="" placeholder={(i+1).toString()} className='page-number' onKeyDown={handleNumberSubmit}/>
            <div className="link weak-gold-btn" onClick={() =>handleNext(i)}>Next</div>
        </div>
    )
}

export default TextSlideshow