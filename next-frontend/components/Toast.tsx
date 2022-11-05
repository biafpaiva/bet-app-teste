import React, { useContext } from 'react'

const Toast = () => {
    return (
        <div id="toast-default" className="flex items-center w-full px-5 py-2 text-gray-500 bg-white rounded-lg shadow dark:text-white dark:bg-red-600" role="alert">
            <div className="ml-3 text-sm font-normal">Invalid UserId / Password</div>
        </div>
    )
}

export default Toast