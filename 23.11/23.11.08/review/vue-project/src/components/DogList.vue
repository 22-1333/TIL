<template>
  <div class="header">
    <h2>랜덤한 강이지</h2>
    <button @click="getRandomDogData" class="styled-button">새로운 강아지 가져오기</button>
  </div>
  <div v-if="dogIsEmpty" class="dog-container">
    <div v-for="dog in dogs" class="dog-box">
      <img :src="dog.url" alt="">
      <div v-if="dog.detail" class="dog-info">
        <p><strong>이름: </strong>{{ dog.detail.name }}</p>
        <p><strong>품종: </strong>{{ dog.detail.breed_group }}</p>
        <p><strong>높이: </strong>{{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }} cm)</p>
        <p><strong>수명: </strong>{{ dog.detail.age }}</p>
        <p><strong>성격: </strong>{{ dog.detail.temperament }}</p>
        <p><strong>무게: </strong>{{ dog.detail.weight.imperial }} 파운드 ({{ dog.detail.weight.metric }} kg)</p>
      </div>
      <div v-else class="dog-info">
        상세 정보 없음
      </div>
    </div>
  </div>
  <div v-else>
    아직 데이터를 받아오지 않았다.
  </div>
</template>

<script setup>
import { computed } from 'vue'

const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
  emit('getDogData')
}

const props = defineProps({
  dogs: Array
})

const dogIsEmpty = computed(() => {
  return props.dogs.length > 0 ? true : false
})
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.styled-button {
  background-color: lightgrey;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
}

.styled-button:hover {
  background-color: grey;
}

.dog-container {
  border: 2px solid #000;
}

.dog-box {
  border: 1px solid #000;
  margin: 10px;
  border-radius: 10px;
  display: flex;
}

.dog-box img {
  width: 200px;
  height: 200px;
  object-fit: fill;
  border-radius: 10px;
}

.dog-info {
  margin-left: 10px;
}
</style>