import '../styles/globals.css'
import type { AppProps } from 'next/app'
import TabBar from '../components/TabBar';
import {createContext, useEffect, useState} from 'react'


export const tabBarContext = createContext<any>(undefined)
export const AdminContext = createContext<any>(undefined)

function MyApp({ Component, pageProps }: AppProps) {
  
  const [showTabBar, setShowTabBar] = useState(false)
  const Tbr = { showTabBar, setShowTabBar }

  const [isAdmin, setIsAdmin] = useState(false)
  const Adm = { isAdmin, setIsAdmin }
  
  return (
    <AdminContext.Provider value={Adm}>
      <tabBarContext.Provider value={Tbr}>
          <TabBar/>
          <Component {...pageProps} />
      </tabBarContext.Provider>
    </AdminContext.Provider>

  )
}

export default MyApp
