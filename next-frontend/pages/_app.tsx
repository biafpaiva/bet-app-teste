import '../styles/globals.css'
import type { AppProps } from 'next/app'
import TabBar from '../components/TabBar';
import {createContext, useState} from 'react'


export const tabBarContext = createContext<any>(undefined)

function MyApp({ Component, pageProps }: AppProps) {
  
  const [showTabBar, setShowTabBar] = useState(false)
  const Tbr = { showTabBar, setShowTabBar }
  
  return (
    <tabBarContext.Provider value={Tbr}>
        <TabBar/>
        <Component {...pageProps} />
    </tabBarContext.Provider>
  )
}

export default MyApp
