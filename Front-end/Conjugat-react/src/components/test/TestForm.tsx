import { ChangeEvent } from "react"

function TestForm({submit, test, handleChange, i, QuestionData, handleNext}: {submit:Function, test:{ language: string; Base: string; Tense: string; IDs: string[]; Subjects: string[]; Auxiliaries: string[]; Verbs: string[]; }, handleChange:Function, i:number, QuestionData:any, handleNext:Function}) {
    return (
        <form action="" autoComplete="off" key={i} onSubmit={(e) => submit(e)}>
            {test.IDs.map((id, j) => (
            
                <div className="text-spacer" key={id}>
                    <p className="text">{test.Subjects[j]}</p>
                    
                    <div className="text-field">
                        <input
                        id={id.toString()}
                        type="text"
                        name="text"
                        className='line'
                        onChange={(e:ChangeEvent<HTMLInputElement>) => handleChange(e)} />
                    </div>
                </div>                   
            ))}
            
            <div className="btn">
                {i === QuestionData.length-1 ?
                <div className="submit-btn">
                    <input type="submit" value="Submit" className="strong-btn strong-gold-btn"/>
                </div>
                :
                <div className="submit-btn">
                    <button type="button"  className="strong-btn strong-gold-btn" onClick={() =>handleNext(i)}>Continue</button>
                </div>
                }
            </div>
        </form>
    )
}

export default TestForm