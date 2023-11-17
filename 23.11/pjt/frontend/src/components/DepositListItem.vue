<template>
  <div>
    <h5>{{ deposit.fin_prdt_nm }}</h5>
    <RouterLink :to="{ name: 'interestDetail', params: { fin_prdt_cd: deposit.fin_prdt_cd }}">detail</RouterLink>
    <hr>
  </div>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'

  defineProps({
    deposit: Object
  })
</script>

<style scoped>

</style>