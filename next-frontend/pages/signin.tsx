import { useState, useEffect } from 'react'
import MainLayout from '../layouts/MainLayout'
import requestService from '../service/api/request.service';
import { useContext } from "react";
import { tabBarContext } from '../pages/_app'
import { useRouter } from 'next/router';

const SignIn = () => {
  const router = useRouter()
  
  const { showTabBar, setShowTabBar } = useContext(tabBarContext);
  setShowTabBar(false)

  const [user, setUser] = useState({
    email: "",
    password: ""
  })

  const handleLogin = async (e: any) => {
    e.preventDefault()
    await requestService.loginUser(user)
    //e.preventDefault()
    router.push('/')
  }

  const handleClick = (e: any) => {
    e.preventDefault()
    router.push('/signup')
  }

  return (
    <MainLayout>
      <div className='w-full max-w-md m-auto'>
        <div className="space-y-8 ">
          <h2 className="mt-6 text-center text-3xl font-bold tracking-tight text-primaryLight">Sign in</h2>
          <form className="mt-8 space-y-6" action="http://localhost:5000/login_user" method="POST">
            <input type="hidden" name="remember" value="true"/>
            <div className="-space-y-px rounded-md shadow-sm">
              <div>
                <label className="sr-only">Email address</label>
                <input value={user.email} onChange={(e) => {
                  setUser(prevUser => ({
                    ...prevUser, email: e.target.value
                  }))}} id="email-address" name="email" type="email" required className="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm" placeholder="Email address"/>
              </div>
              
              <div>
                <label className="sr-only">Password</label>
                <input value={user.password} onChange={(e) => {
                  setUser(prevUser => ({
                    ...prevUser, password: e.target.value
                  }))}} id="password" name="password" type="password" required className="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm" placeholder="Password"/>
              </div>
            </div>
      
            <div>
              <button onClick={handleLogin} className="group relative flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                <span className="absolute inset-y-0 left-0 flex items-center pl-3">
                  
                  <svg className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fillRule="evenodd" d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z" clipRule="evenodd" />
                  </svg>
                </span>
                Sign in
              </button>
              <button onClick={handleClick} className="group relative flex w-full justify-center rounded-md border-b border-transparent my-5 py-2 px-4 text-sm font-medium text-white hover:border-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                <span className="absolute inset-y-0 left-0 flex items-center pl-3">
                </span>
                Don't have an account yet?  Sign Up
              </button>
            </div>
          </form>
        </div>
      </div>
    </MainLayout>    
  )
}

export default SignIn