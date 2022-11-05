import React from 'react'
import { IUser } from '../types/user'
import { getPicture } from '../utils/getPicture';

const RankingCard = ({position, user}: PropTypes) => {
  return (
    <>
      <div className="w-full container py-3 rounded-xl bg-secondaryDark shadow-[0_0_30px_rgba(0,0,0,0.25)]">
        <div className="grid grid-cols-5 content-center items-center place-items-center place-content-between text-primaryLight font-bold tracking-tight">
            <div className='col-span-auto -mx-[80px]'>{position} th</div>
            <div className='w-[60px] -ml-1 m-auto bg-primaryLight aspect-square rounded-full overflow-hidden'>
              <img className='object-cover' src={ user.image } alt="" />
            </div>
            <div className='pl-5'> {user.username} </div>
            <div className='col-span-2 text-md'>{user.score ? user.score : 0} points</div>
        </div>
      </div>
    </>
  )
}

interface PropTypes{
  user: IUser,
  position: number
}
export default RankingCard