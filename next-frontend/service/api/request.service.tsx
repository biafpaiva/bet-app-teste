import api from './api'
import PropTypes from 'prop-types'
import { IBet } from '../../types/bets'
import { IUser } from '../../types/user'

interface PropTypes {
  email: string,
  password: string
}

const getUserData = () => {
  return api.get("/user_data")
            .catch((error: any) => {
              console.log(error)
            })  
}

const loginUser = ({email, password}: PropTypes) => {

  const formData = new FormData();
  formData.set('email', email)
  formData.set('password', password)

  return api.post("/login_user", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }})
  .then((response: any) => {
    if (response.data) {
         localStorage.setItem("user", JSON.stringify(response.data))
         localStorage.setItem('image', JSON.stringify(response.data[0].image))
         console.log(response.data.token)

        if(response.data[0].email == 'admin@admin.com'){
          localStorage.setItem('is_admin', '1')
        } else{
          localStorage.setItem('is_admin', '0')
        }
    }
    return response.data
  })
}

const logoutUser = () => {
  localStorage.clear()
  return api.get("/logout")
  .catch((error: any) => {
    console.log(error)
  })
}

const listMatches = () => {
  return api.get("/list_matches")
            .catch((error: any) => {
              console.log(error)
            })
}

const listBets = () => {
  return api.get("/list_bets")
            .catch((error: any) => {
              console.log(error)
            })
}

const deleteBet = (bet: IBet) => {

  const formData = new FormData();
  formData.set('id_game', bet.id_game)
  formData.set('email', bet.email)

  return api.post("/delete_bet", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }})
  .then((response: any) => {
    if (response) {
         /*localStorage.setItem("user", JSON.stringify(response.data))*/
         console.log(response)
    }
    return response
  }) 
}

const changeUsername = (user: any) => {

  const formData = new FormData();
  formData.set('username', user.username)
  formData.set('email', user.email)

  return api.post("/change_username", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }})
  .then((response: any) => {
    if (response) {
         /*localStorage.setItem("user", JSON.stringify(response.data))*/
         console.log(user.email)
         console.log(response)
    }
    return response
  }) 
}


const listRanking = () => {
  return api.get("/list_ranking")
            .catch((error: any) => {
              console.log(error)
            })
}

const makeBet = ({home_score, away_score, id_game, id_group}: any) => {

  const formData = new FormData();
  formData.set('home_score', home_score)
  formData.set('away_score', away_score)
  formData.set('game_id', id_game)
  formData.set('id_group', id_group)

  return api.post("/make_bet", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }})
  .then((response: any) => {
    if (response) {
         /*localStorage.setItem("user", JSON.stringify(response.data))*/
         console.log(response)
    }
    return response
  }) 
}

const registerResult = ({home_score, away_score, id_game}: any) => {
  const formData = new FormData();
  formData.set('home_score', home_score)
  formData.set('away_score', away_score)
  formData.set('game_id', id_game)

  return api.post("/register_result", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }})
  .then((response: any) => {
    if (response) {
         /*localStorage.setItem("user", JSON.stringify(response.data))*/
         console.log(response)
    }
    return response
  })

}

const requestService = {
    getUserData,
    loginUser,
    logoutUser,
    listMatches,
    listBets,
    listRanking,
    makeBet,
    deleteBet,
    changeUsername,
    registerResult
}

export default requestService