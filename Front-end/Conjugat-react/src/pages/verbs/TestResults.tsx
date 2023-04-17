import { useEffect } from "react"
import { useParams } from "react-router-dom"
import AxiosInstance from "../../functions/AxiosInstance"

function TestResults() {
    const { testID } = useParams()
    const activateAccount = async () => {const res = await (
        AxiosInstance.Unauthorised
        .post('verbs/verb-test-results', {
            testID: testID,
        })
        .then(res =>
            console.log(res.data)
        )
        .catch(err => {
            console.log(err)
        })
    )}

    useEffect(() => {
      activateAccount();
    }, [])
    
    return (
        <>
        {exampleAnswerData.map((answer, i) => (
            <div>
                
            </div>
        ))}
        </>
    )
}

const exampleAnswerData = [
    [
        {
            language: 'English',
            Base: 'be',
            Tense: 'Present',
            IDs: [1, 2, 3, 4, 5, 6],
            Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
            Auxiliaries: ["", "", "", "", "", "", ""],
            Verbs: ["am", "are", "is", "are", "are", "are"],
            Answer:["am", "are", "", "are", "is", "is"],
            Result:[true, true, null, true, false, false],
        },
        {
            language: 'English',
            Base: 'have',
            Tense: 'Present',
            IDs: [7, 8, 9, 10, 11, 12],
            Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
            Auxiliaries: ["", "", "", "", "", "", ""],
            Verbs: ["have", "have", "have", "have", "have", "have"],
            Answer: ["have", "have", "have", "have", "have", "have"],
            Result:[true, true, true, true, true, false],
        },
        {
            language: 'English',
            Base: 'know',
            Tense: 'Present',
            IDs: [25, 14, 15, 16],
            Subjects: ['He/She/It', 'We', 'You', 'They'],
            Auxiliaries: ["", "", "", "", ""],
            Verbs: ["know", "know", "knows", "know"],
            Answer:["know", "know", "know", "know"],
            Result:[true, true, false, true],
        }
    ]
]

export default TestResults