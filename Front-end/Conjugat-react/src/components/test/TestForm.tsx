import { ChangeEvent } from "react"
import { getTranslation } from "../../functions/getTranslation";
import { testFormTranslations } from "../../content/verbs/Test";

function TestForm({language, submit, test, handleChange, i, QuestionData, handleNext}: {language:string, submit:Function, test:{ language: string; Base: string; Tense: string; IDs: string[]; Subjects: string[]; Auxiliaries: string[]; Verbs: string[]; }, handleChange:Function, i:number, QuestionData:any, handleNext:Function}) {
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
                    <input type="submit" className="strong-btn strong-gold-btn" value={getTranslation(testFormTranslations, language, 'Text1')} />
                </div>
                :
                <div className="submit-btn">
                    <button type="button"  className="strong-btn strong-gold-btn" onClick={() =>handleNext(i)}>{getTranslation(testFormTranslations, language, 'Text2')}</button>
                </div>
                }
            </div>
        </form>
    )
}

export default TestForm