<template>
  <div>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/interest">금리 비교</RouterLink>
    <RouterLink to="/exchange">환율</RouterLink>
    <RouterLink to="/bank">은행 검색</RouterLink>
    <RouterLink to="/recommendation">추천</RouterLink>
  </div>  
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>