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
    const [typeface, setTypeface] = useState<string[]>([])
    const [FieldList, setFieldList] = useState<string[]>([])
    const [FieldList2, setFieldList2] = useState<string[]>([])
    const [headerFont, setHeaderFont] = useState<string>('')
    const [bodyFont, setBodyFont] = useState<string>('')


    const fetchdata = async () => {
        const res = await (
            AxiosInstance.Authorised
            .get('settings/font/read/')
        )
        console.log(res.data.fonts)
        console.log(res.data.typefaces)
        setfetchedFonts(res.data.fonts)
        setTypeface(res.data.typefaces)
    }

    useEffect(() => {
        fetchdata()
    }, [])

    const updateFieldlist = async () => {
        // for (var font in fetchedFonts.font) {
        //     if 
        // }

        console.log(fetchedFonts.typeface[2], 'hi')
        console.log(typeface)

        const fontHolder = fetchedFonts.font.filter(checkTypeface)

        function checkTypeface(fetchedFont:TFetchedFonts, i:number) {
            console.log(fetchedFont, i)
            console.log(fetchedFonts.typeface[i], typeface)
            if (typeface.includes(fetchedFonts.typeface[i])) {
                return fetchedFont
            }
        }

        console.log(fontHolder, 'yoo')
        setFieldList(fontHolder)
    }

    const updateFieldlist2 = async () => {
        const fontHolder: string[] = []
        
        fetchedFonts.map((font, i) => (font.typeface in fetchedFonts) ?
            fontHolder.push(font["font"]) :
            fontHolder.push()
        )
        setFieldList2(fontHolder)
    }

    useEffect(() =>{
        updateFieldlist()
    }, [typeface])

    function changeHeaderFont(e:ChangeEvent<HTMLSelectElement>) {
        setHeaderFont(e.target.value)
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
                <div>
                    {/* Change what typefaces are selectable */}
                </div>
                <div className="password-spacer">
                    <SelectField
                    labelText={getTranslation(FontFormTranslations, language, 'Select')}
                    field={[headerFont]}
                    changeField={changeHeaderFont}
                    FieldList = {FieldList}
                    FieldListValues = {FieldList}
                    />
                </div>

                <div>
                    {/* Change what typefaces are selectable */}
                </div>
                <div className="password-spacer">
                    <SelectField
                    labelText={getTranslation(FontFormTranslations, language, 'Select')}
                    field={[bodyFont]}
                    changeField={setBodyFont}
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
