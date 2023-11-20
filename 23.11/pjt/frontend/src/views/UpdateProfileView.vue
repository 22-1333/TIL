<template>
  <div>
		<h1>회원 정보 수정</h1>
    <form @submit.prevent="updateprofile">
      <label for="username">유저이름</label>
      <input type="text" id="username" v-model.trim="username"> 
      <label for="first">이름</label>
      <input type="text" id="first" v-model.trim="first_name">
      <label for="last">성</label>
      <input type="text" id="last" v-model.trim="last_name">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios'
  
  const store = useCounterStore()
  const username = ref()
  const first_name = ref()
  const last_name = ref()
  
  const updateprofile = () => {

    axios({
      method: 'patch',
      url: `${store.DRF_URL}/dj_rest_auth/user/`,
      data: {
        username: username.value, 
        first_name: first_name.value, 
        last_name: last_name.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log(error)
      })
  }
</script>

<style scoped>

</style>
