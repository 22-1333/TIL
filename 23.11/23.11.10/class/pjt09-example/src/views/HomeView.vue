<template>
  <div>
    <h1>메인 페이지</h1>
    <div v-if="productIsEmpty" class="product-list">
      <div v-for="product in products" :key="product.id" class="product-card">
        <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="addCart(product)">장바구니에 추가</button>
      </div>
    </div>
    <div v-else>
      <strong>로딩 중...</strong>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const products = ref([])
const storeURL = 'https://fakestoreapi.com/products'

axios.get(storeURL)
  .then((response) => {
    products.value = response.data
  }).catch((error) => {
    console.error(error)
  })

const productIsEmpty = computed(() => {
  return products.value.length > 0 ? true : false
})

const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const addCart = (product) => {
  const exisitingCart = JSON.parse(sessionStorage.getItem('cart')) || []

  const isDuplicate = exisitingCart.length > 0 && exisitingCart.find((item) => item.id === product.id)

  if(!isDuplicate) {
    alert('장바구니에 추가합니다')
    exisitingCart.push(product)
  } else {
    alert('이미 있는 상품입니다. 장바구니로 이동합니다.')
  }

  sessionStorage.setItem('cart', JSON.stringify(exisitingCart))
}

</script>

<style>
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.product-card{
  border: 1px solid black;
  width: 205px;
}

.product-card img {
  width: 200px;
  height: 200px;
  object-fit: fill;
}
</style>