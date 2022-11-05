import type { NextPage } from 'next'
import { useState, useEffect, useContext } from 'react'
import { IMatch } from '../types/match'
import requestService from '../service/api/request.service';
import Card from '../components/Card';
import Link from 'next/link';
import { tabBarContext } from './_app';
import { useRouter } from 'next/router';

const Home: NextPage = () => {
  const router = useRouter()
  useEffect(() => {
    if (localStorage.getItem("user") === null){
      router.push('/signin')
    }
  }, []);  

  const { showTabBar, setShowTabBar } = useContext(tabBarContext);
  setShowTabBar(true)

  const [games, setGames] = useState<IMatch[]>([])
  useEffect(() => {
    async function loadGames() {
        const response: any = await requestService.listMatches()
        setGames(response.data)
    }
    loadGames();
  }, [])

  return (
    <>
      <div className='min-h-screen bg-primaryDark pt-[60px] px-6'>

        <h2 className="py-4 pt-5 text-2xl font-bold tracking-tight text-primaryLight">Matches</h2>
        
        <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-5 pb-[100px]">
          {games.map((match) => {
            return(
                <Link href={{pathname: "/matchInfo", query: {
                  key: match.id,
                  partida: match.teams,
                  rodada: match.round,
                  data: match.date,
                  hora: match.time,
                  estadio: match.stadium,
                  grupo: match.group
                  }}} >
                  <div className="pt-5">
                    <Card key={match.id} match={ match }
                    />
                  </div>
                </Link>
            )
          })}
        </div>
      </div>    
    </>
  )
}

export default Home
