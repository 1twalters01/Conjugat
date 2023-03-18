import { FormEvent } from "react"
import { useDispatch, useSelector } from "react-redux";
import AxiosInstance from "../../../functions/AxiosInstance";
import { onThemeChange } from "../../../redux/slices/themeSlice";
import { RootState } from "../../../redux/store";

function ThemeFunctionality() {
    const{ theme } = useSelector((state: RootState) => state.persistedReducer.theme)
    const dispatch = useDispatch();
    
    function submit(choice:string, e:FormEvent<HTMLDivElement>) {
      if (choice != theme) {
        e.preventDefault();
        AxiosInstance.Authorised
        .post('settings/themes/', {
          choice: choice
        })
        .then(res=>{
          console.log(typeof res.data.theme, res.data.theme)
          dispatch(onThemeChange(res.data.theme))
        })
        .catch(err=>{
          console.log(err)
        })
      }
    }
  
    return(
      <div>
        <div onClick={(e) => submit('Dark', e)} style={{height: '200px', width: '200px', background: 'black'}}>
        
        </div>
        <div onClick={(e) => submit('Light', e)} style={{height: '200px', width: '200px', background: 'yellow'}}>
        
        </div>
      </div>
    )
}

export default ThemeFunctionality