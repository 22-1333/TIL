<template>
	<div>
    {{ user }}
	</div>
</template>

<script setup>
	import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router'

  const store = useCounterStore()
  const route = useRoute()
  const user = ref(null)

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/accounts/profile/${route.params.username}/`
    })
      .then((response) => {
        user.value = response.data
      })
      .catch((error) => {
        console.error(error)
      })
  })
</script>

<style scoped>

</style>