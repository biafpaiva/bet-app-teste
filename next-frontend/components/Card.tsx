import React from 'react'
import { IMatch } from '../types/match'
import Image from 'next/image'

const Card = ({match}: PropTypes) => {
  return (
    <>
      <div className="container py-5 px-auto rounded-xl bg-secondaryDark shadow-[0_0_30px_rgba(0,0,0,0.25)] text-primaryLight">
        <div className="grid grid-cols-4 content-center items-center place-items-center">

            <div className='w-[60px] ml-6 my-auto bg-primaryLight rounded-xl overflow-hidden'>
              <img className='object-cover' src={ match.home } alt="" />
            </div>

            <div className='col-span-2'>
              <div className='text-center font-black'>{match.teams}</div>
              <p className='text-center'>{match.weekDay}, {match.date} </p>
            </div>

            <div className='w-[60px] mr-6 my-auto bg-primaryLight rounded-xl overflow-hidden'>
              <img className='object-cover' src={ match.visitor } alt="" />
            </div>
        </div>
      </div>
    </>
  )
}

interface PropTypes{
  match: IMatch
}

export default Card