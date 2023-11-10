<template>
  <div>
    <h1>장바구니</h1>
    <div v-if="!cartIsEmpty" class="product-list">
      <div v-for="product in cartItems" :key="product.id" class="product-card">
        <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="removeCart(product)">장바구니에 삭제</button>
      </div>
    </div>
    <div v-else>
      <strong>장바구니에 담긴 상품이 없습니다.</strong>
    </div>
  </div>
</template>

<script setup>
import { computed } from '@vue/reactivity';
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const cartItems = ref([])

cartItems.value = JSON.parse(sessionStorage.getItem('cart'))

const cartIsEmpty = computed(() => {
  return cartItems.value.length > 0 ? false : true
})

const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const removeCart = (product) => {
  const itemIdx = cartItems.value.findIndex((item) => item.id === product.id)
  
  cartItems.value.splice(itemIdx, 1)

  sessionStorage.setItem('cart', JSON.stringify(cartItems.value))
}
</script>


<style scoped>

</style>