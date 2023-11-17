<template>
  <div>
    <h1>환율 계산기</h1>
    <input type="number" v-model="koreaMoney" @keyup="inputKorea">
    <input type="number" v-model="otherMoney" @keyup="inputOther">
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios'

  const store = useCounterStore()
  const koreaMoney = ref()
  const otherMoney = ref()

  const inputKorea = (() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/exchange/USD/`
    })
      .then((response) => {
        otherMoney.value = response.data.rate * koreaMoney.value
      })
      .catch((error) => {
        console.error(error)
      })
  })

  const inputOther = (() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/exchange/USD/`
    })
      .then((response) => {
        koreaMoney.value = otherMoney.value / response.data.rate
      })
      .catch((error) => {
        console.error(error)
      })
  })
</script>

<style scoped>

</style>