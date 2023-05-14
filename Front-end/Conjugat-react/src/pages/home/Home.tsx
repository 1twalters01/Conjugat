import { useEffect, useState, useRef, MouseEvent } from "react"
import { Helmet } from "react-helmet"
import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"
import AxiosInstance from "../../functions/AxiosInstance"

import SettingsNavbar from "../../components/settings/SettingsNavbar"

import { Bar, getElementAtEvent } from 'react-chartjs-2';
import { Chart, registerables, ChartType } from 'chart.js';
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import HomeModal from "../../components/home/Home/HomeModal"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/Home"

Chart.register(...registerables);

function Home() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    
    const [correct, setCorrect] = useState<Boolean|null>(null)
    const [incorrect, setIncorrect] = useState<Boolean|null>(null)
    const [isOpen, setIsOpen] = useState(false)

    type TData = null | {
        labels: any;
        datasets: {
            label: string;
            data: any;
        }[];
    }
    const [basicData, setBasicData] = useState<TData>(null)
    const [modalFetchedData, setModalFetchedData] = useState([{
      TestID:'',
      Test:[{
        Answers:[''],
        Auxiliaries:[''],
        Base:"",
        Conjugations:[''],
        IDs:[],
        Language:"",
        Ranks:[],
        Status:[],
        Subjects:[''],
        Tense: ""
      }]
    }])

    async function retrieveData() {
        const res = await(
            AxiosInstance.Authorised
            .get('/home')
        )
        const formatted_data =
        {
          labels: res.data?.map((data: { Date: String }) => data.Date),
          
          datasets: [{
              label: "Correct",
              data: res.data?.map((data: { Correct: String }) => data.Correct),
              backgroundColor: 'rgba(10, 199, 53, 0.8)',
              hoverBackgroundColor: 'rgba(10, 199, 53, 0.95)',
              borderColor: 'rgba(0,0,0,1)',
              borderWidth: 1,
            },
            {
              label: "Incorrect",
              data: res.data?.map((data: { Incorrect: String }) => data.Incorrect),
              backgroundColor: 'rgba(204, 10, 10, 0.8)',
              hoverBackgroundColor: 'rgba(204, 10, 10, 0.95)',
              borderColor: 'rgba(0,0,0,1)',
              borderWidth: 1,
            }],
        }    
      
        setBasicData(formatted_data)
    }

    useEffect(() => {
      retrieveData()
    }, [])
    
    const options = {

    }

    type TmodalData = {correct:Boolean|null, incorrect: Boolean|null, modalFetchedData: null | { TestID: string; Test: { Answers: string[]; Auxiliaries: string[]; Base: string; Conjugations: string[]; IDs: never[]; Language: string; Ranks: never[]; Status: never[]; Subjects: string[]; Tense: string; }[]; }[]}
    const[modalData, setModalData] = useState<TmodalData>({correct:null, incorrect:null, modalFetchedData:null})

    // const chartRef = useRef<Chart<"bar", number[]>>(null)
    const chartRef = useRef<any>(null)
    const onClick = (event: MouseEvent<HTMLCanvasElement>) => {
      if (getElementAtEvent(chartRef.current, event).length > 0){
        const index = getElementAtEvent(chartRef.current, event)[0].index

        const fetchData = async () => {
            var res: any = await (
                AxiosInstance.Authorised
                .post('home/modal-data', {
                    date: basicData?.labels[index]
                })
            )
            setModalFetchedData(res.data)
        }

        fetchData()

        if (getElementAtEvent(chartRef.current, event)[0].datasetIndex === 0){
            setCorrect(true)
            setIncorrect(false)
            setModalData({correct:correct, incorrect:incorrect, modalFetchedData:modalFetchedData})
            setIsOpen(true)
        }
        else if(getElementAtEvent(chartRef.current, event)[0].datasetIndex === 1){
          setCorrect(false)
          setIncorrect(true)
          setModalData({correct:correct, incorrect:incorrect, modalFetchedData:modalFetchedData})
          setIsOpen(true)
        }
      }
    }

    useEffect(() => {
      setModalData({correct:correct, incorrect:incorrect, modalFetchedData:modalFetchedData})
    }, [modalFetchedData, correct, incorrect])

    useEffect(() => {
      if (modalData.correct != null || modalData.incorrect != null){
        setIsOpen(true)
      }
    }, [modalData])

    if (basicData != null) {
      return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>

            <SettingsNavbar language={language} />
            <div>
                <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
                
                <h1>{getTranslation(translations, language, 'Title1')}</h1>

                <Bar
                ref={chartRef}
                data={basicData}
                options={options}
                onClick={onClick}
                />
            </div>

            <HomeModal open={isOpen} setOpen={setIsOpen} modalData={modalData} />
        </>
      )
    }
    else{
        return(
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title2')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent2')}
                    />
                </Helmet>
            </>
        )
    }
}

export default Home