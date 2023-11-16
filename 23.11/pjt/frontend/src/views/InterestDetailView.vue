<template>
  <div>
    <h2>Interest Detail</h2>
    <div>
      {{ product }}
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router'

  const store = useCounterStore()
  const route = useRoute()
  const product = ref(null)

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/interest/${route.params.fin_prdt_cd}`
    })
      .then((response) => {
        product.value = response.data
      })
      .catch((error) => {
        console.error(error)
      })
  })
</script>

<style>

</style>
