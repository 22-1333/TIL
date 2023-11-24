import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  
  const token = ref(null)
  const loginUsername = ref(null)
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

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = (payload) => {
    const { username, password1, password2, email, first_name, last_name, nickname, age, money, salary, duration } = payload

    axios({
      method: 'post',
      url: `${DRF_URL}/dj_rest_auth/registration/`,
      data: {
        username, email, password1, password2, first_name, last_name, nickname, age, money, salary, duration
      }
    })
      .then((res) => {
        const password = password1
        logIn({ username, password })
      })
      .then((response) => {
        router.push({ name: 'home' })
      })
      .catch((err) => {
        window.alert(`010-9915-7609로 연락주세요.\n${err}`)
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
        loginUsername.value = username
      })
      .then((response) => {
        router.push({ name: 'home' })
      })
      .catch((error) => {
        window.alert('로그인에 실패하였습니다.')
      })
  }

  const logOut = () => {
    axios({
      method: 'post',
      url: `${DRF_URL}/dj_rest_auth/logout/`,
    })
      .then((response) => {
        token.value = null
        loginUsername.value = null
      })
      .then((response) => {
        router.push({ name: 'home' })
      })
      .catch((error) => {
        console.error(error)
      })
  }

  const registeredDepositList = ref([])

  const getRegisteredDepositList = () => {
    axios({
      method: 'get',
      url: `${DRF_URL}/interest/get_registered_list/0/${loginUsername.value}/`,
    })
      .then((response) => {
        registeredDepositList.value = response.data.registered_list
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const registeredInstallmentSavingList = ref([])

  const getRegisteredInstallmentSavingList = () => {
    axios({
      method: 'get',
      url: `${DRF_URL}/interest/get_registered_list/1/${loginUsername.value}/`,
    })
      .then((response) => {
        registeredInstallmentSavingList.value = response.data.registered_list
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const bankLogos = ref({
    '우리은행': 'https://www.blockfintoday.com/data/photos/20210415/art_16182801067188_90b765.jpg',
    '한국스탠다드차타드은행': 'https://icons-for-free.com/iconfiles/png/512/chartered+indonesia+standard+icon-1320086020035558541.png',
    '대구은행': '/daegu.png',
    '부산은행': '/busan.png',
    '광주은행': 'https://www.whitepaper.co.kr/news/photo/201601/59879_39413_654.PNG',
    '제주은행': 'https://multibank.co.kr/data/file/cars_1/554936764_QIeplfMT_66c6a1ca8d3c895d3fed492c2ff1a47d84500b01.jpg',
    '전북은행': 'https://t1.daumcdn.net/cfile/tistory/99A4CF3359DC974A35',
    '경남은행': 'https://www.knbank.co.kr/resource/img/bank_logo.jpg',
    '중소기업은행': 'https://www.businesspost.co.kr/news/photo/202104/20210430183320_12777.png',
    '한국산업은행': 'https://blog.kakaocdn.net/dn/cnOWmz/btrUgi7fH06/xNDd8QN7nd1xjbVvDGuqik/img.png',
    '국민은행': 'https://www.paxetv.com/news/photo/202308/184443_160096_1713.jpg',
    '신한은행': 'https://i0.wp.com/inthiswork.com/wp-content/uploads/2023/03/SHINHAN-BANK-3.jpg?fit=1152%2C768&ssl=1',
    '농협은행주식회사': 'https://www.ajou.ac.kr/app/board/attach/image/99527_1635397801000.do',
    '하나은행': 'https://www.ezyeconomy.com/news/photo/202001/97505_37189_4937.jpg',
    '주식회사 케이뱅크': 'https://t1.daumcdn.net/cfile/tistory/99952E4D5B1E31E730',
    '수협은행': 'https://t1.daumcdn.net/cfile/tistory/21172B43586A89DD25',
    '주식회사 카카오뱅크': 'https://mblogthumb-phinf.pstatic.net/MjAyMDEyMjJfMjc1/MDAxNjA4NjAzNjI5NjY3.XW5GXQhzHBNPsDlEbakIHbi6tAuwz6lLpXg3UuIx11og.DDBEmjHsJ438XZuIO0uYhgr2rWiIs4fxd3Hwvx3QD3Ag.JPEG.congha/%EC%B9%B4%EC%B9%B4%EC%98%A4%EC%9D%80%ED%96%89-%EB%A1%9C%EA%B3%A0copy_copy.jpg?type=w800',
    '토스뱅크 주식회사': 'https://cdn.fortunekorea.co.kr/news/photo/202203/21819_12691_2643.png'
  })

  return { DRF_URL, depositList, installmentSavingList, getDepositList, getInstallmentSavingList, depositBankList, installmentSavingBankList, token, isLogin, loginUsername, signUp, logIn, logOut, registeredDepositList, getRegisteredDepositList, registeredInstallmentSavingList, getRegisteredInstallmentSavingList, bankLogos }
}, { persist: true })
