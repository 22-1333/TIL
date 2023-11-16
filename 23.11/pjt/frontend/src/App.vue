<template>
  <div>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'interest' }">Interest</RouterLink>
    <RouterLink :to="{ name: 'exchange' }">Exchange</RouterLink>
    <RouterLink :to="{ name: 'bank' }">Bank</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>

</style>