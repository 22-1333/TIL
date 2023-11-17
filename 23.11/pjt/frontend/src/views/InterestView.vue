<template>
  <div>
    <h1>예적금 금리 비교</h1>
    <div>
      <RouterLink :to="{ name: 'depositList' }">Deposit List</RouterLink>
      <RouterLink :to="{ name: 'installmentSavingList' }">Installment Saving List</RouterLink>
    </div>
  </div>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'

</script>

<style scoped>

</style>