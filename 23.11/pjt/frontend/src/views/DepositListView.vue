<template>
  <div>
    <h2>Deposit List</h2>
    <select v-model="selectedBank" @change="selectBank">
      <option v-for="bank in store.depositBankList" :value="bank">{{ bank }}</option>
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
    return value.kor_co_nm === selectedBank.value
  })
</script>

<style scoped>

</style>