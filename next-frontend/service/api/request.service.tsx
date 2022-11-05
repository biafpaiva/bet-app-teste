import api from './api'
import PropTypes from 'prop-types'

interface PropTypes {
  email: string,
  password: string
}

const getUserData = () => {
  return api.get("/user_data")
            .catch((error) => {
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
  .then((response) => {
    if (response) {
         localStorage.setItem("user", JSON.stringify(response.data))
         //console.log(response)
    }
    return response
  })
}

const logoutUser = () => {
  localStorage.clear
}

const listMatches = () => {
  return api.get("/list_matches")
            .catch((error) => {
              console.log(error)
            })
}

const listBets = () => {
  return api.get("/list_bets")
            .catch((error) => {
              console.log(error)
            })
}


const listRanking = () => {
  return api.get("/list_ranking")
            .catch((error) => {
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
  .then((response) => {
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
    makeBet
}

export default requestService