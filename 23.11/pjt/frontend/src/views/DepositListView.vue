<template>
  <div class="top">
    다양한 은행의 예금과 적금 상품을 비교해보세요.
  </div>
  <div class="page">
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="move">
      <RouterLink class="move-button" :to="{ name: 'depositList' }">
        <img class="deposit-icon" src="/deposit.png" alt="">
        예금 상품
      </RouterLink>
      <RouterLink class="move-button" :to="{ name: 'installmentSavingList' }">
        <img class="saving-icon" src="/saving.png" alt="">
        적금 상품
      </RouterLink>
    </div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="page-info"><strong><span class="black">예금 상품.&nbsp;</span><span class="red">큰 금액</span>으로&nbsp;<span class="red">한 번</span>에 목돈 만들기!</strong></div>
    <div class="space"></div>
    <div class="bank-select">
      <select class="custom-select" v-model="selectedBank" @change="selectBank">
        <option :value="null">모든 은행</option>
        <option v-for="bank in store.depositBankList" :value="bank">{{ bank }}</option>
      </select>
      <i class="fas fa-chevron-down select-chevron"></i>
    </div>
    <div class="space"></div>
    <div class="page-detail"><strong><span class="black">{{ bankDetail }}</span>에서 운영 중인 예금 상품을 확인해보세요.</strong></div>
    <div class="product-container">
      <div class="product-grid" v-if="!isSelected">
        <DepositListItem v-for="deposit in store.depositList" :key="deposit.fin_prdt_cd" :deposit="deposit" :options="getOption(deposit.fin_prdt_cd)" />
      </div>
      <div class="product-grid" v-else>
        <DepositListItem v-for="deposit in store.depositList.filter(isSameBank)" :key="deposit.fin_prdt_cd" :deposit="deposit" :options="getOption(deposit.fin_prdt_cd)" />
      </div>
    </div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
  </div>
  <RouterView />
</template>

<script setup>
  import { onMounted, ref, computed } from 'vue'
  import { RouterView, RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  import DepositListItem from '@/components/DepositListItem.vue'
  import axios from 'axios'

  const store = useCounterStore()
  const isSelected = ref(false)
  const selectedBank = ref(null)

  const bankDetail = computed(() => {
    if (isSelected.value) {
      if (selectedBank.value) {
        return selectedBank.value
      }
      else {
        return "모든 은행"
      }
    }
    else {
      return "모든 은행"
    }
  })

  const getOption = (fin_prdt_cd) => {
    const optionList = ref([])
    const options = ref({})

    axios({
      method: 'get',
      url: `${store.DRF_URL}/interest/${fin_prdt_cd}`
    })
      .then((response) => {
        optionList.value = response.data.option
      })
      .then((response) => {
        for (const option of optionList.value) {
          const save_trm = option.save_trm
          options.value[save_trm] = option.intr_rate2
        }
      })
      .catch((error) => {
        console.error(error)
      })

    return options
  }

  onMounted(() => {
    store.getDepositList()
    store.getRegisteredDepositList()
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
.space {
  height: 10px;
}

.top {
  height: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12px;
  color: #6E6E73;
}

.page {
  display: flex;
  flex-direction: column;
  background-color:  #f8f9fa;
  align-items: center;
}

.move {
  display: flex;
  width: 300px;
  justify-content: space-between;
}

.move-button {
  display: flex;
  flex-direction: column;
  text-align: center;
  color: black;
  font-size: 13px;
}

.deposit-icon {
  width: 70px;
  height: 70px;
  margin-bottom: 8px;
}

.saving-icon {
  width: 70px;
  height: 70px;
  margin-bottom: 8px;
}

.page-info {
  display: flex;
  align-items: center;
  width: 80%;
  height: 60px;
  font-size: 30px;
  min-width: 580px;
  color: #6E6E73;
}

.black {
  color: black;
}

.red {
  color: #E30000;
}

.bank-select {
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
}

.custom-select {
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  appearance: none; 
  -webkit-appearance: none;
  -moz-appearance: none;
  background-color: white;
  width: 250px;
  font-size: 16px;
  cursor: pointer;
}

select:focus {
  border: 2px solid #007bff;
}

.select-chevron {
  position: absolute;
  top: 50%;
  left: 217px;
  transform: translateY(-50%);
  color: #007bff;
  pointer-events: none;
}

.page-detail {
  display: flex;
  align-items: center;
  width: 80%;
  height: 60px;
  font-size: 20px;
  min-width: 580px;
  color: #6E6E73;
}

.product-container {
  width: 90%;
}

.product-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: space-evenly;
}

</style>