<template>
  <div>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'interest' }">Interest</RouterLink>
    <RouterLink :to="{ name: 'exchange' }">Exchange</RouterLink>
    <RouterLink :to="{ name: 'bank' }">Bank</RouterLink>
    <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink>
    <RouterLink :to="{ name: 'login' }">LogIn</RouterLink>
    <RouterLink :to="{ name: 'profile', params: { username: 'admin' } }">Profile</RouterLink>
  </div>
  <div>
    <form @submit.prevent="store.logOut">
      <input type="submit" value="logOut">
    </form>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>

</style>