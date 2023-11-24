<template>
  <div class="profile">
    <h1>프로필 정보</h1>
    <div class="profile-detail">
      <label>닉네임:</label>
      <p>{{ user.username }}</p>
    </div>
    <div class="profile-detail">
      <label>이메일:</label>
      <p>{{ user.email }}</p>
    </div>
    <div class="profile-detail">
      <label>이름:</label>
      <p>{{ user.first_name }}</p>
    </div>
    <div class="profile-detail">
      <label>성:</label>
      <p>{{ user.last_name }}</p>
    </div>
    <div class="profile-detail">
      <label>자산:</label>
      <p>{{ user.money }}</p>
    </div>
    <div class="profile-detail">
      <label>월 수입:</label>
      <p>{{ user.salary }}</p>
    </div>
    <!-- 뒤로가기 -->
    <button @click="router.push({ name: 'mypage', params: { username: store.loginUsername } })">뒤로 가기</button>
  </div>
</template>


<script setup>
	import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute, useRouter } from 'vue-router'

  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()
  const user = ref({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    money: '',
    salary: ''
  })

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/accounts/profile/${route.params.username}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        user.value = response.data
      })
      .catch((error) => { 
        console.error(error)
      })
  })
</script>

<style scoped>
.profile {
  background: #fff;
  max-width: 700px;
  margin: 2em auto;
  padding: 2em;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.profile h1 {
  color: #000;
  font-size: 1.5em;
  text-align: center;
  margin-bottom: 0.8em;
}

.profile-detail {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5em;
}

.profile-detail label {
  font-weight: bold;
  color: #333;
  flex-basis: 40%;
  text-align: left;
}

.profile-detail p {
  margin: 0;
  flex-basis: 60%;
  text-align: right;
  font-size: 1em;
}

button {
  background-color: #007aff;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  margin-top: 1em;
  width: 100%;
}

button:hover {
  background-color: #0051a8;
}
</style>