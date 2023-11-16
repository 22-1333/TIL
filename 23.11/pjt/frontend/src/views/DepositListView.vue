<template>
  <div>
    <h2>Deposit List</h2>
    <select v-model="selectedBank" @change="selectBank">
      <option value="">선택하세요.</option> 
      <option v-for="deposit in store.depositList" :value="deposit.fin_co_no">{{ deposit.kor_co_nm }}</option>
    </select>
    <div v-if="!isSelected">
      <DepositListItem v-for="deposit in store.depositList" :key="deposit.fin_prdt_cd" :deposit="deposit" />
    </div>
    <div v-else>
      <DepositListItem v-for="deposit in store.depositList.filter(isSameBank)" :key="deposit.fin_prdt_cd" :deposit="deposit" />
    </div>
  </div>
</template>

<script setup>
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import DepositListItem from '@/components/DepositListItem.vue'

  const store = useCounterStore()
  const isSelected = ref(false)
  const selectedBank = ref()

  onMounted(() => {
    store.getDepositList()
  })

  const selectBank = (() => {
    if (selectedBank.value) {
      isSelected.value = true
    }
    else {
      isSelected.value = false
    }
  })

  const isSameBank = ((value) => {
    return value.fin_co_no === selectedBank.value
  })
</script>

<style scoped>

</style>