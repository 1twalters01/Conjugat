function Test() {
    return (
        <div>
            {exmpleQustionData.map((test, i) => (
                <div>
                    <h1>{test.Base}</h1>
                    <h1>{test.Tense}</h1>

                    {test.IDs.map((id, j) => (
                        <h2>
                            {id},
                            {test.Subjects[j]},
                            {test.Auxiliaries[j]},
                            {test.Verbs[j]}
                        </h2>
                    ))}
                </div>
            ))}
        </div>
    )
}

const exmpleQustionData = [
    {
        language: 'English',
        Base: 'be',
        Tense: 'Present',
        IDs: [1, 2, 3, 4, 5, 6],
        Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
        Auxiliaries: ["", "", "", "", "", "", ""],
        Verbs: ["am", "are", "is", "are", "are", "are"],
    },
    {
        language: 'English',
        Base: 'have',
        Tense: 'Present',
        IDs: [7, 8, 9, 10, 11, 12],
        Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
        Auxiliaries: ["", "", "", "", "", "", ""],
        Verbs: ["have", "have", "have", "have", "have", "have"],
    },
    {
        language: 'English',
        Base: 'know',
        Tense: 'Present',
        IDs: [13, 14, 15, 16, 17, 18],
        Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
        Auxiliaries: ["", "", "", "", "", "", ""],
        Verbs: ["know", "know", "knows", "know", "know", "know"],

    }
]

export default Test