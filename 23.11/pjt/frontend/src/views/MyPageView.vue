<template>
  <div>
    <h1>마이 페이지</h1>
    <RouterLink :to="{ name: 'updateprofile' }">[회원정보 수정]</RouterLink>
    <br>
    <RouterLink :to="{ name: 'updatepassword' }">[비밀번호 수정]</RouterLink>
    <br>
    <RouterLink :to="{ name: 'profile', params: {username: store.loginUsername} }">[프로필 정보]</RouterLink>
  </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()
</script>

<style scoped>

</style>