<template>
  <div class="password-change-container">
    <h1>비밀번호 수정</h1>
    <form @submit.prevent="updatepassword">
      <input type="password" placeholder="기존 비밀번호" v-model.trim="old_password" @focus="old_password = ''">
      <input type="password" placeholder="새 비밀번호" v-model.trim="new_password1" @focus="new_password1 = ''">
      <input type="password" placeholder="비밀번호 확인" v-model.trim="new_password2" @focus="new_password2 = ''">
      <input type="submit" value="제출">
      <!-- 뒤로가기 -->
      <button @click="router.push({ name: 'mypage', params: { username: store.loginUsername } })">뒤로 가기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const store = useCounterStore();
const route = useRoute()
const router = useRouter()

const old_password = ref('');
const new_password1 = ref('');
const new_password2 = ref('');

const updatepassword = () => {
  axios({
    method: 'post',
    url: `${store.DRF_URL}/dj_rest_auth/password/change/`,
    data: {
      new_password1: new_password1.value,
      new_password2: new_password2.value,
      old_password: old_password.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    window.alert('비밀번호가 수정되었습니다');
    router.push({ name: 'mypage', params: { username: store.loginUsername } }).catch(e => {
      console.error(e);
    });
  })
  .catch((error) => {
    console.error(error);
    window.alert('비밀번호 수정에 실패했습니다');
  });
};
</script>

<style scoped>
  .password-change-container {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    background-color: #fff;
  }

  h1 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }

  input[type="password"] {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
  }

  input[type="password"]:focus {
    border-color: #007aff;
    outline: none;
  }

  input[type="submit"] {
    background-color: #007aff;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.3s ease;
  }

  input[type="submit"]:hover {
    background-color: #0051a8;
  }

  input[type="submit"]:active {
    background-color: #003d82;
  }

  input[type="password"]::placeholder {
    font-weight: normal;
    color: #999;
  }

  input[type="password"]:not(:placeholder-shown) {
    font-weight: bold;
  }

  button {
    background-color: #ccc;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #999;
  }

  button:active {
    background-color: #777;
  }
</style>
