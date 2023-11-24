<template>
  <RouterLink class="product-card" :to="{ name: 'interestDetail', params: { fin_prdt_cd: deposit.fin_prdt_cd }}">
    <img :src="store.bankLogos[deposit.kor_co_nm]" alt="">
    <div class="product-card-content">
      <button v-if="isRegistered" class="registered">가입한 상품</button>
      <div class="bank-name">{{ deposit.kor_co_nm }}</div>
      <div class="product-name">{{ clearName }}</div>
      <div class="join-way">{{ deposit.join_way }}</div>
    </div>
  </RouterLink>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  import { ref, computed } from 'vue'

  const props = defineProps({
    deposit: Object,
    options: Object
  })

  const store = useCounterStore()

  const isRegistered = computed(() => {
    const inList = ref(false)
    for (const registeredDeposit of store.registeredDepositList) {
      if (registeredDeposit === props.deposit.fin_prdt_cd) {
        inList.value = true
        break
      }
    }
    return inList.value
  })

  const clearName = computed(() => {
    return props.deposit.fin_prdt_nm.replace(/\s*\([^)]*\)\s*/gs, '')
  })
</script>

<style scoped>
.product-card {
  width: 300px;
  height: 450px;
  border: 1px solid #eaeaea;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background: #fff;
  overflow: hidden;
  margin-top: 10px;
  margin-bottom: 10px; /* Space below each card */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for transform and shadow */
  position: relative;
}

.product-card img {
  margin-top: 60px;
  width: 290px;
  height: 230px;
  display: block;
  margin-bottom: 20px;
}

.product-card-content {
  padding: 16px;
}

.bank-name {
  font-size: 12px;
  color: #C36242;
  margin-bottom: 8px;
}

.product-name {
  font-size: 16px;
  color: black;
  font-weight: bold;
}

.join-way {
  font-size: 14px;
  color: black;
  margin-top: 20px;
}

.product-card:hover {
  transform: scale(1.05); /* Slightly increase the size */
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); /* Darker shadow */
}

.registered {
  padding: 5px 10px; /* Adjust the padding to control the size */
  position: absolute;
  top: 20px; 
  right: 20px;
  z-index: 2;
  font-size: 12px;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
  border: none; /* No border */
  border-radius: 20px; /* Rounded corners */
  background-color: #E0E0E0; /* Light grey background */
  color: #555; /* Dark grey text */
}
</style>