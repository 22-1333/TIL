<script setup>
import { ref } from 'vue'
import DogList from './components/DogList.vue'
import axios from 'axios'

const dogs = ref([])

const getDogData = async () => {
  const URL = 'https://api.thedogapi.com/v1/images/search?limit=10'

  try {
    const response = await axios.get(URL)
    
    const dogData = response.data

    // 암기1. 비동기 쓸 때 forEach 쓰지 말자!
    //     map 으로 변경! -> map: 기존 데이터를 토대로 새로운 배열 반환
    // 암기2. map 안에 async 쓰면 자동으로 Promise 객체 반환

    const details = dogData.map(async (dog) => {
      const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
      const detailres = await axios.get(detailURL)
      dog.detail = detailres.data.breeds ? detailres.data.breeds[0] : null
    })

    // dogData.forEach(async (dog) => {
    //   const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
    //   const detailres = await axios.get(detailURL)
    //   dog.detail = detailres.data.breeds ? detailres.data.breeds[0] : null
    // })

    await Promise.all(details)

    dogs.value = dogData

  } catch (error) {
    console.error('에러 발생' ,error)
  }

  // axios.get(URL)
  //   .then((response) => {
  //     const dogData = response.data
      
  //     dogData.forEach((dog) => {
  //       const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
  //       axios.get(detailURL)
  //         .then((response) => {
  //           dog.detail = response.data
  //           console.log(dog)
  //         }).catch((error) => {
  //           console.log(error)
  //         })
  //     })

  //     dogs.value = dogData

  //   }).catch((error) => {
  //     console.error(error)
  //   })
}
</script>

<template>
  <div class="container">
    <h1>2023-11-08 실습</h1>
    <DogList :dogs="dogs" @get-dog-data="getDogData"/>
  </div>  
</template>

<style scoped>
.container {
  width: 80%;
  margin: 0 auto;
}
</style>