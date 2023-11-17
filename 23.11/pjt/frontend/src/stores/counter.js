import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()

  const DRF_URL = 'http://127.0.0.1:8000'
  
  const depositList = ref([])
  const depositBankList = ref([])
  const installmentSavingList = ref([])
  const installmentSavingBankList = ref([])

  const getDepositList = () => {
    axios({
      method: 'get',
      url: `${DRF_URL}/interest/deposit_list/`
    })
      .then((response) => {
        depositList.value = response.data
      })
      .then(() => {
        for (const depositIndex in depositList.value) {
          if (!depositBankList.value.includes(depositList.value[depositIndex].kor_co_nm)) {
            depositBankList.value.push(depositList.value[depositIndex].kor_co_nm)
          }
        }
      })
      .catch((error) => {
        console.error(error)
      })
  }

  const getInstallmentSavingList = () => {
    axios({
      method: 'get',
      url: `${DRF_URL}/interest/installment_saving_list/`
    })
      .then((response) => {
        installmentSavingList.value = response.data
      })
      .then(() => {
        for (const installmentSavingIndex in installmentSavingList.value) {
          if (!installmentSavingBankList.value.includes(installmentSavingList.value[installmentSavingIndex].kor_co_nm)) {
            installmentSavingBankList.value.push(installmentSavingList.value[installmentSavingIndex].kor_co_nm)
          }
        }
      })
      .catch((error) => {
        console.error(error)
      })
  }

  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = (payload) => {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${DRF_URL}/dj_rest_auth/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = (payload) => {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${DRF_URL}/dj_rest_auth/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        console.log('로그인 성공')
      })
      .catch((error) => {
        console.error(error)
      })
  }

  const logOut = () => {
    axios({
      method: 'post',
      url: `${DRF_URL}/dj_rest_auth/logout/`,
    })
      .then((response) => {
        token.value = null
        console.log('로그아웃 성공')
      })
      .catch((error) => {
        console.error(error)
      })
  }

  return { DRF_URL, depositList, installmentSavingList, getDepositList, getInstallmentSavingList, depositBankList, installmentSavingBankList, token, isLogin, signUp, logIn, logOut }
}, { persist: true })
