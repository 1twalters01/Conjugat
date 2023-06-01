import { ChangeEvent, FormEvent, useEffect, useState } from "react"
import { FontFormTranslations } from "../../../content/settings/Font"
import { getTranslation } from "../../../functions/getTranslation"
import SubmitBtn from "../../Buttons/SubmitBtn"
import SelectField from "../../Input fields/SelectField"
import AxiosInstance from "../../../functions/AxiosInstance"
import { onHeaderFontChange, onBodyFontChange } from "../../../redux/slices/fontSlice"
import { toast } from "react-toastify"
import { useDispatch } from "react-redux"

function FontForm({language}: {language:string}) {
    // fetch list of supported fonts from settings/font/read/
    // Post on update of font to settings/font/
    const dispatch = useDispatch()
    
    type TFetchedFonts = {
        "font": '',
        "typeface": ''
    }

    const [fetchedFonts, setfetchedFonts] = useState<TFetchedFonts[]>([])
    const [fetchedTypeface, setTypeface] = useState<string[]>([])
    const [bodyTypefaces, setBodyTypefaces] = useState<string[]>([])
    const [headerTypefaces, setHeaderTypefaces] = useState<string[]>([])
    const [FieldList, setFieldList] = useState<string[]>([])
    const [FieldList2, setFieldList2] = useState<string[]>([])
    const [headerFont, setHeaderFont] = useState<string>('')
    const [bodyFont, setBodyFont] = useState<string>('')


    const fetchdata = async () => {
        const res = await (
            AxiosInstance.Authorised
            .get('settings/font/read/')
        )
        setfetchedFonts(res.data.fonts)
        setTypeface(res.data.typefaces)
        setHeaderTypefaces(res.data.typefaces)
        setHeaderFont(res.data.headerFont)
        setBodyTypefaces(res.data.typefaces)
        setBodyFont(res.data.bodyFont)
    }

    useEffect(() => {
        fetchdata()
    }, [])



    function changeHeaderTypeface(e:ChangeEvent<HTMLSelectElement>) {
        if (headerTypefaces.includes(e.target.value)) {
            setHeaderTypefaces(headerTypefaces.filter(headerTypefaces => headerTypefaces !== e.target.value))
        }
        else {
            setHeaderTypefaces([...headerTypefaces, e.target.value])
        }
    }
    
    useEffect(() =>{
        updateHeaderFieldlist()
    }, [headerTypefaces])

    const updateHeaderFieldlist = async () => {
        // const fontHolder = fetchedFonts.filter(checkTypeface)
        function checkTypeface(fetchedFont:TFetchedFonts, i:number) {
            if (headerTypefaces.includes(fetchedFonts[i].typeface)) {
                return fetchedFont.font
            }
            else {
                return null
            }
        }
        var fontHolder:string[] = []
        console.log(fetchedFonts)
        for (var index in fetchedFonts) {
            if (fetchedFonts[index].font === checkTypeface(fetchedFonts[index], +index))
            fontHolder.push(fetchedFonts[index].font)
        }
        setFieldList(fontHolder)
    }

    useEffect(() =>{
        updateHeaderFieldlist()
    }, [fetchedTypeface])

    function changeHeaderFont(e:ChangeEvent<HTMLSelectElement>) {
        setHeaderFont(e.target.value)
    }



    function changeBodyTypeface(e:ChangeEvent<HTMLSelectElement>) {
        if (bodyTypefaces.includes(e.target.value)) {
            setBodyTypefaces(bodyTypefaces.filter(bodyTypefaces => bodyTypefaces !== e.target.value))
        }
        else {
          setBodyTypefaces([...bodyTypefaces, e.target.value])
        }
    }
    
    useEffect(() =>{
        updateBodyFieldlist()
    }, [bodyTypefaces])

    const updateBodyFieldlist = async () => {
        // const fontHolder = fetchedFonts.filter(checkTypeface)
        function checkTypeface(fetchedFont:TFetchedFonts, i:number) {
            if (bodyTypefaces.includes(fetchedFonts[i].typeface)) {
                return fetchedFont.font
            }
            else {
                return null
            }
        }
        var fontHolder:string[] = []
        console.log(fetchedFonts)
        for (var index in fetchedFonts) {
            if (fetchedFonts[index].font === checkTypeface(fetchedFonts[index], +index))
            fontHolder.push(fetchedFonts[index].font)
        }
        setFieldList2(fontHolder)
    }

    useEffect(() =>{
        updateBodyFieldlist()
    }, [fetchedTypeface])

    function changeBodyFont(e:ChangeEvent<HTMLSelectElement>) {
        setBodyFont(e.target.value)
    }

    

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Authorised
        .post('settings/font/', {
            headerFont: headerFont,
            bodyFont: bodyFont
        })
        .then(res=>{
            dispatch(onHeaderFontChange(res.data.headerFont))
            dispatch(onBodyFontChange(res.data.bodyFont))
        })
        .catch(err=>{
          toast.error(err.response.data.error)
        })
    }

    return (
        <div>
            <form onSubmit={(e) => submit(e)}>
                <div className="Font-lhs">
                    <h4>Header</h4>
                    
                    <SelectField
                    id = {'headerSelectTypeface'}
                    labelText = 'placeholder'
                    field = {headerTypefaces}
                    changeField = {changeHeaderTypeface}
                    FieldList = {fetchedTypeface}
                    FieldListValues = {fetchedTypeface}
                    />

                    <SelectField
                    id={'headerFontFields'}
                    labelText={getTranslation(FontFormTranslations, language, 'Select')}
                    field={[headerFont]}
                    changeField={changeHeaderFont}
                    FieldList = {FieldList}
                    FieldListValues = {FieldList}
                    />
                </div>

                <div className="Font-rhs">
                    <h4>Body</h4>
                    
                    <SelectField
                    id = {'bodySelectTypeface'}
                    labelText = 'placeholder'
                    field = {bodyTypefaces}
                    changeField = {changeBodyTypeface}
                    FieldList = {fetchedTypeface}
                    FieldListValues = {fetchedTypeface}
                    />

                    <SelectField
                    id={'bodyFontFields'}
                    labelText = {getTranslation(FontFormTranslations, language, 'Select')}
                    field = {[bodyFont]}
                    changeField = {changeBodyFont}
                    FieldList = {FieldList2}
                    FieldListValues = {FieldList2}
                    />
                </div>

                <SubmitBtn
                    value={getTranslation(FontFormTranslations, language, 'Submit')}
                    style="strong-red-btn"
                />
            </form>
        </div>
    )
}

export default FontForm
