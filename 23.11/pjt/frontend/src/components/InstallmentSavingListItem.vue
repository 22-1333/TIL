<template>
  <div>
    <h5>{{ installment_saving.fin_prdt_nm }}</h5>
    <RouterLink :to="{ name: 'interestDetail', params: { fin_prdt_cd: installment_saving.fin_prdt_cd }}">detail</RouterLink>
    <hr>
  </div>
  <RouterView />
</template>
    
<script setup>
  import { RouterLink } from 'vue-router'
    
  defineProps({
    installment_saving: Object
  })
</script>
