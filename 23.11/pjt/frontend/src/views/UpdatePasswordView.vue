<template>
  <div>
    <h1>비밀번호 수정</h1>
    <form @submit.prevent="updatepassword">
      <input type="password" v-model.trim="new_password1">
      <input type="password" v-model.trim="new_password2">
      <input type="password" v-model.trim="old_password">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios'
  
  const new_password1 = ref()
  const new_password2 = ref()
  const old_password = ref()
  const store = useCounterStore()

  const updatepassword = () => {
    axios({
      method: 'post',
      url: `${store.DRF_URL}/dj_rest_auth/password/change/`,
      data: {
        new_password1: new_password1.value, 
        new_password2: new_password2.value,
        old_password: old_password.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        window.alert('비밀번호 변경 완료')
      })
      .catch((error) => {
        console.error(error)
      })
  }
</script>

<style scoped>

</style>