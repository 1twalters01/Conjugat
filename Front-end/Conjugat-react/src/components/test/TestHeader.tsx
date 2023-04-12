function TestHeader({test}: {test:any}) {
    return (
        <>
            <h1 className="title header">{test.Base.charAt(0).toUpperCase()+test.Base.slice(1)}</h1>
            <h2 className="subtitle subheader">{test.Tense}</h2>
        </>
    )
}

export default TestHeader