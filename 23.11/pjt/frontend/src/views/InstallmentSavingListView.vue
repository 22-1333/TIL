<template>
  <div>
    <h2>Installment Saving List</h2>
    <select v-model="selectedBank" @change="selectBank">
      <option v-for="bank in store.installmentSavingBankList" :value="bank">{{ bank }}</option>
    </select>
    <div v-if="!isSelected">
      <InstallmentSavingListItem v-for="installment_saving in store.installmentSavingList" :key="installment_saving.fin_prdt_cd" :installment_saving="installment_saving" />
    </div>
    <div v-else>
      <InstallmentSavingListItem v-for="installment_saving in store.installmentSavingList.filter(isSameBank)" :key="installment_saving.fin_prdt_cd" :installment_saving="installment_saving" />
    </div>
  </div>
</template>

<script setup>
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import InstallmentSavingListItem from '@/components/InstallmentSavingListItem.vue'

  const store = useCounterStore()
  const isSelected = ref(false)
  const selectedBank = ref()

  onMounted(() => {
    store.getInstallmentSavingList()
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