import { useState, useEffect, useContext } from 'react'

import { IUser } from '../types/user'

import requestService from '../service/api/request.service';
import RankingCard from '../components/rankingCard';
import { tabBarContext } from './_app';
import { useRouter } from 'next/router';

const Ranking = () => {

  const { showTabBar, setShowTabBar } = useContext(tabBarContext);
  setShowTabBar(true)  

  const [users, setUsers] = useState<IUser[]>([])
  const router = useRouter()

  useEffect(() => {
    if (localStorage.getItem("user") === null){
      router.push('/signin')
    }
  }, []);

  useEffect(() => {
    async function loadGames() {
        const response: any = await requestService.listRanking()
        setUsers(response.data)
        console.log(users)
    }
    loadGames();
  }, [])
  
  return (
    <div className='grid h-full'>
      <div className='min-h-screen bg-primaryDark pt-[40px] px-6'>
          <h2 className="pb-4 pt-10 text-2xl font-bold tracking-tight text-primaryLight">Global ranking</h2>
          <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-5 pb-[100px]">
            {users.map((user, n) => {
              return(
                <div className="pt-5">
                  <RankingCard position={n + 1} user={user}/>
                </div>
              )
            })} 
          </div>
      </div>    
    </div>

  )
}

export default Ranking