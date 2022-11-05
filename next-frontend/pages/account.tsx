import { useContext, useEffect, useState } from 'react';
import { getPicture } from '../utils/getPicture';
import requestService from '../service/api/request.service';
import { tabBarContext } from './_app';
import { useRouter } from 'next/router';
import Image from 'next/image';

const Account = () => {

  const { showTabBar, setShowTabBar } = useContext(tabBarContext);
  setShowTabBar(true)

  const [showModal, setShowModal] = useState(false);
  const [username, setUsername] = useState('')
  const [userImage, setImage] = useState<any>('')

  const [user, setUser] = useState<any>()
  const router = useRouter()

  useEffect(() => {
    if (localStorage.getItem("user") === null){
      const temp = localStorage.getItem('user')
      setUser(temp)
      router.push('/signin')
    } else {
      const temp2 = localStorage.getItem('image')
      setImage(temp2)
    }
  }, []);

  useEffect(() => {
    async function loadUserData() {
        const response: any = await requestService.getUserData()
        setUser(response.data[0])
    }
    loadUserData();
  }, [])  

  const handleLogout = (e: any) => {
    e.preventDefault()
    requestService.logoutUser()
    router.push('/signin')
  }

  const handleChangeUsername = async (e: any) => {
    e.preventDefault()
    const user_data = {'username': username, 'email': user.email}
    await requestService.changeUsername(user_data)
    setShowModal(false)

    router.reload()
  }

  return (
    <div className='flex flex-col min-w-screen min-h-screen bg-primaryDark pt-[60px] px-6 justify-items-center text-primaryLight'>
        <div className='w-[120px] mb-6 mx-auto bg-primaryLight aspect-square rounded-full overflow-hidden'>
          <img src={userImage.slice(1, -1)} alt="" />
        </div>
        
        <h2 className='text-center font-bold tracking-tight text-primaryLight text-xl'>{user?.username}</h2>
        <p className='text-center text-primaryLight text-lg'>{user?.email}</p>

        <button onClick={() => setShowModal(true)} className='flex items-center mt-[60px] pb-2'>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3" />
          </svg>
          <div className='ml-4'>Change username</div>
        </button>
        <hr className='border-secondaryDark'/>
        <form >
          <button onClick={handleLogout} type='submit' className='flex items-center pt-5 pb-2'>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
            </svg>
            <div className='ml-4'>Logout</div>
          </button>
        </form>
        <hr className='border-secondaryDark'/>

        <form action="http://localhost:5000/delete_account">
          <button className='flex items-center pt-5 pb-2'>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
            </svg>
            <div className='ml-4'>Delete account</div>
          </button>
        </form>

        {showModal ? (
        <>
          <div
            className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
          >
            <div className="relative w-auto my-6 mx-5 max-w-3xl">
              {/*content*/}
              <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
                {/*header*/}
                <div className='pt-10 px-5 text-center text-xl font-bold tracking-tight text-primaryDark'>Change username</div>

                {/*body*/}
                <form className='flex justify-center m-10 drop-shadow-xl text-primaryDark'>
                  <input value={username} onChange={(e) => {
                  setUsername(e.target.value)}} name='home_score' className='text-primaryDark aspect-square p-4 w-[180px] h-[60px] border rounded-md' type="text" />
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
                    onClick={handleChangeUsername}
                  >
                    Save
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

export default Account