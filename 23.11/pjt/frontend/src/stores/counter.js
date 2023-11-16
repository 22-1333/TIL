import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const DRF_URL = 'http://127.0.0.1:8000'

  const depositList = ref([])
  const installmentSavingList = ref([])

  const getDepositList = function () {
    axios({
      method: 'get',
      url: `${DRF_URL}/interest/deposit_list/`
    })
      .then((response) => {
        depositList.value = response.data
      })
      .catch((error) => {
        console.error(error)
      })
  }

  const getInstallmentSavingList = function () {
    axios({
      method: 'get',
      url: `${DRF_URL}/interest/installment_saving_list/`
    })
      .then((response) => {
        installmentSavingList.value = response.data
      })
      .catch((error) => {
        console.error(error)
      })
  }
  
  return { DRF_URL, depositList, installmentSavingList, getDepositList, getInstallmentSavingList }
}, { persist: true })
