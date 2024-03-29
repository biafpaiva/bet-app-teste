import { useContext, useEffect, useState } from 'react';
import requestService from '../service/api/request.service';
import { tabBarContext } from './_app';
import { IBet } from '../types/bets';
import { useRouter } from 'next/router';

const Bets = () => {

  const { showTabBar, setShowTabBar } = useContext(tabBarContext);
  setShowTabBar(true)
  const router = useRouter()

  useEffect(() => {
    if (localStorage.getItem("user") === null){
      router.push('/signin')
    }
  }, []);  

  const [bets, setBets] = useState<IBet[]>([])

  useEffect(() => {
    async function loadBets() {
        const response: any = await requestService.listBets()
        setBets(response.data)
    }
    loadBets();
  }, [])

  const handleDeleteBet = (bet: IBet) => {
    requestService.deleteBet(bet)
    router.reload()
  }

  return (
    <div className='flex flex-col min-w-screen min-h-screen bg-primaryDark pt-[60px] px-6 justify-items-center text-primaryLight'>
        <h2 className="pt-10 pb-10 text-center text-3xl font-bold tracking-tight text-primaryLight">You made {bets.length} Bets</h2>
        <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-5 pb-[100px]">
          {bets.map((bet) => {
            return(
              <div>
                <div className='flex items-center justify-between pt-5 pb-3'>
                  <div className=''>{bet.teams}, round {bet.round}</div>
                  <button onClick={() => handleDeleteBet(bet)}>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                    </svg>
                  </button>
                </div>
                <hr className='border-secondaryDark'/>
              </div>
            )
          })}
        </div>
    </div>
  )
}

export default Bets
