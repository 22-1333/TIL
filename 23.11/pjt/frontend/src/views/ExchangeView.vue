<template>
  <div>
    <input type="number" v-model="inputWon" @keyup="input">
    <p>{{ output }}</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios'

  const store = useCounterStore()
  const output = ref(0)
  const inputWon = ref()

  const input = (() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/exchange/USD/`
    })
      .then((response) => {
        console.log(typeof(response.data.rate))
        output.value = response.data.rate * inputWon.value
      })
      .catch((error) => {
        console.error(error)
      })
  })
</script>

<style scoped>

</style>