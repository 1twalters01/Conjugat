import { useEffect, useState, useRef, MouseEvent } from "react"
import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"
import AxiosInstance from "../../functions/AxiosInstance"

import SettingsNavbar from "../../components/settings/SettingsNavbar"
import HomeChart from "../../components/home/Home/HomeChart"

import { Bar, getElementAtEvent } from 'react-chartjs-2';
import { Chart, registerables, ChartType } from 'chart.js';
import HomeModal from "../../components/home/Home/HomeModal"

Chart.register(...registerables);

function Home() {
    Authorization.AuthRequired()
    const [isOpen, setIsOpen] = useState(false)

    type TData = null | {
        labels: any;
        datasets: {
            label: string;
            data: any;
        }[];
    }
    const [basicData, setBasicData] = useState<TData>(null)
    const [modalFetchedData, setModalFetchedData] = useState('')

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

    const[modalData, setModalData] = useState({status:'', modalFetchedData:''})

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
            console.log(res.data)
            console.log(modalFetchedData)
            // return res.data
        }
        // useEffect(() => {
          fetchData()
        // }, [])
        // setModalFetchedData(fetchData())

        // console.log(modalFetchedData)

        if (getElementAtEvent(chartRef.current, event)[0].datasetIndex === 0){
            var status = 'Correct'
            setModalData({status:status, modalFetchedData:modalFetchedData})
            setIsOpen(true)
        }
        else if(getElementAtEvent(chartRef.current, event)[0].datasetIndex === 1){
          var status = 'Incorrect'
          setModalData({status:status, modalFetchedData:modalFetchedData})
          setIsOpen(true)
        }
      }
    }

    if (basicData != null) {
      return (
        <>
            <SettingsNavbar />
            <div>
                <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
                
                <h1>Home</h1>

                <Bar
                ref={chartRef}
                data={basicData}
                options={options}
                onClick={onClick}
                />
            </div>

            <HomeModal open={isOpen} setOpen={setIsOpen}>
                <p style={{'color':'white', 'padding':'20px'}}>
                    {modalData.status}
                </p>
                <p style={{'color':'white', 'padding':'20px'}}>
                    {modalData.modalFetchedData}
                </p>
            </HomeModal>
        </>
      )
    }
    else{
        return(
            <></>
        )
    }
}

export default Home