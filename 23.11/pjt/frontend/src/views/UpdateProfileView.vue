<template>
  <div class="profile-container">
    <h1>회원 정보 수정</h1>
    <form @submit.prevent="updateProfile" class="profile-form">
      <div class="form-group">
        <label for="username">닉네임:</label>
        <input type="text" id="username" v-model.trim="profileData.username" class="form-input">
      </div>
      <div class="form-group">
        <label for="email">이메일:</label>
        <input type="email" id="email" v-model.trim="profileData.email" class="form-input">
      </div>
      <div class="form-group">
        <label for="first">이름:</label>
        <input type="text" id="first" v-model.trim="profileData.first_name" class="form-input">
      </div>
      <div class="form-group">
        <label for="last">성:</label>
        <input type="text" id="last" v-model.trim="profileData.last_name" class="form-input">
      </div>
      <div class="form-group">
        <label for="age">나이:</label>
        <input type="text" id="age" v-model.trim="profileData.age" class="form-input">
      </div>
      <div class="form-group">
        <label for="money">자산:</label>
        <input type="text" id="money" v-model.trim="profileData.money" class="form-input">
      </div>
      <div class="form-group">
        <label for="salary">월 수입:</label>
        <input type="text" id="salary" v-model.trim="profileData.salary" class="form-input">
      </div>
      <button type="button" @click="router.push({ name: 'mypage', params: { username: store.loginUsername } })" class="back-button">뒤로 가기</button>
      <input type="submit" value="저장" class="submit-button">
    </form>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter, useRoute } from 'vue-router'
  import axios from 'axios'

  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()
  const profileData = ref({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    age: '',
    money: '',
    salary: ''
  })

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/accounts/profile/${store.loginUsername}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      profileData.value = response.data
    })
    .catch((error) => {
      console.error(error)
    })
  })

  const updateProfile = () => {
    axios({
      method: 'patch',
      url: `${store.DRF_URL}/accounts/profile/${store.loginUsername}/`,
      data: {
      username: profileData.value.username,
      email: profileData.value.email,
      first_name: profileData.value.first_name, 
      last_name: profileData.value.last_name,
      age: profileData.value.age,
      money: profileData.value.money,
      salary: profileData.value.salary
    },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      window.alert('수정되었습니다');
      router.push({ name: 'mypage', params: { username: store.loginUsername } }).catch(e => {
      console.error(e);
    }); 
    })
    .catch((error) => {
      console.error(error)
      window.alert('실패했습니다'); 
    })
  }
</script>

<style scoped>
.profile-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #f8f8f8;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  text-align: left;
}

label {
  font-weight: bold;
  color: #555;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.back-button {
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s;
}

.back-button:hover {
  background-color: #555;
}

.submit-button {
  background-color: #007aff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s;
}

.submit-button:hover {
  background-color: #0051a8;
}
</style>