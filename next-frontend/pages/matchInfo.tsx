import { useContext, useEffect, useState } from 'react'
import { useRouter } from 'next/router'
import { IMatch } from '../types/match'
import { AdminContext, tabBarContext } from './_app';
import requestService from '../service/api/request.service';

const MatchInfo = () => {

  const { showTabBar, setShowTabBar } = useContext(tabBarContext);
  setShowTabBar(true)

  const router = useRouter()
  const {partida, rodada, data, hora, estadio, key, grupo} = router.query
  const [showModal, setShowModal] = useState(false);
  
  const { isAdmin, setIsAdmin } = useContext(AdminContext);

  useEffect(() => {
    if (localStorage.getItem("user") === null){
      router.push('/signin')
    } else if (localStorage.getItem('is_admin') === '1'){
      setIsAdmin(true)
    }
  }, []);

  const handleResult = () => {
    requestService.registerResult(bet)
    setShowModal(false)
  }

  const handleBet = () => {
    requestService.makeBet(bet)
    setShowModal(false)
  }  

  const [bet, setBet] = useState({
    home_score: '',
    away_score: '',
    id_game: key,
    id_group: grupo
  })

  return (
    <div className='flex flex-col min-w-screen min-h-screen bg-primaryDark pt-[60px] px-6 justify-items-center text-primaryLight'>
        <h2 className="pt-10 text-center text-3xl font-bold tracking-tight text-primaryLight">{partida}</h2>

        <div className='flex items-center pt-[60px] pb-2'>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M5.25 8.25h15m-16.5 7.5h15m-1.8-13.5l-3.9 19.5m-2.1-19.5l-3.9 19.5" />
          </svg>

          <div className='ml-4'>Round {rodada}</div>
        </div>
        <hr className='border-secondaryDark'/>

        <div className='flex items-center pt-5 pb-2'>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z" />
          </svg>
          <div className='ml-4'>{data}, {hora}</div>
        </div>
        <hr className='border-secondaryDark'/>

        <div className='flex items-center pt-5 pb-2'>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
          </svg>
          <div className='ml-4'>{estadio}</div>
        </div>
        <hr className='border-secondaryDark'/>      
        
        <button type='button' onClick={() => setShowModal(true)}
          className='flex mt-10 break-inside bg-indigo-600 rounded-full px-8 py-4 mb-4 w-full dark:bg-indigo-600 dark:text-white'>
          <div className='flex items-center justify-between flex-1'>
            <span className='text-lg font-medium text-white'>{isAdmin ? 'Register result' : 'Make bet'}</span>
            <svg width='17' height='17' viewBox='0 0 17 17' fill='none' xmlns='http://www.w3.org/2000/svg'>
              <path fillRule='evenodd' clipRule='evenodd'
                d='M0 8.71423C0 8.47852 0.094421 8.25246 0.262491 8.08578C0.430562 7.91911 0.658514 7.82547 0.896201 7.82547H13.9388L8.29808 2.23337C8.12979 2.06648 8.03525 1.84013 8.03525 1.60412C8.03525 1.36811 8.12979 1.14176 8.29808 0.974875C8.46636 0.807989 8.6946 0.714233 8.93259 0.714233C9.17057 0.714233 9.39882 0.807989 9.5671 0.974875L16.7367 8.08499C16.8202 8.16755 16.8864 8.26562 16.9316 8.3736C16.9767 8.48158 17 8.59733 17 8.71423C17 8.83114 16.9767 8.94689 16.9316 9.05487C16.8864 9.16284 16.8202 9.26092 16.7367 9.34348L9.5671 16.4536C9.39882 16.6205 9.17057 16.7142 8.93259 16.7142C8.6946 16.7142 8.46636 16.6205 8.29808 16.4536C8.12979 16.2867 8.03525 16.0604 8.03525 15.8243C8.03525 15.5883 8.12979 15.362 8.29808 15.1951L13.9388 9.603H0.896201C0.658514 9.603 0.430562 9.50936 0.262491 9.34268C0.094421 9.17601 0 8.94995 0 8.71423Z'
                fill='white' />
            </svg>
          </div>
        </button>
        
        {showModal ? (
        <>
          <div
            className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
          >
            <div className="relative w-auto my-6 mx-5 max-w-3xl">
              {/*content*/}
              <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
                {/*header*/}
                <div className='pt-10 text-center text-3xl font-bold tracking-tight text-primaryDark'>{partida}</div>

                {/*body*/}
                <form className='flex justify-center m-10 drop-shadow-xl text-primaryDark' action="http://localhost:5000/make_bet" method="POST">
                  <input value={bet.home_score} onChange={(e) => {
                  setBet(prevBet => ({
                    ...prevBet, home_score: e.target.value
                  }))}} name='home_score' className='text-primaryDark aspect-square p-4 w-[60px] h-[60px] border rounded-md' type="number" pattern="[0-9]*" />
                  <div className='text-center m-auto text-3xl px-5 font-bold tracking-tight text-gray-400'>x</div>
                  <input value={bet.away_score} onChange={(e) => {
                  setBet(prevBet => ({
                    ...prevBet, away_score: e.target.value
                  }))}} name='away_score' className='text-primaryDark aspect-square p-4 w-[60px] h-[60px] border rounded-md' type="text" pattern="[0-9]*" />
                </form>
                {/*footer*/}
                <div className="flex items-center justify-end p-6 border-t border-solid border-slate-200 rounded-b">
                  <button
                    className="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
                    onClick={() => setShowModal(false)}
                  >
                    Close
                  </button>
                  <button
                    className="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="submit"
                    onClick={isAdmin ? handleResult : handleBet}
                  >
                    {isAdmin ? 'Save result' : 'Save bet'}
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
        </>
      ) : null}

    </div>
  )
}

interface PropTypes {
  dataMatch: IMatch
}

export default MatchInfo