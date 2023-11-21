<template>
  <div class="signup-page">
    <div class="top-box">
      <div class="top">
        <div><strong>Home ID</strong></div>
        <div class="top-right">회원가입</div>
      </div>
    </div>
    <hr>
    <div class="signup-box">
      <h2><strong>Home ID 생성</strong></h2>
      <h5>회원가입을 통해 Home Page의 모든 서비스를 사용해 보세요.</h5>
      <div class="signup">
        <div class="namebox">
          <div class="input-container name">
            <input id="lastname" class="input-field" placeholder=" " type="text">
            <label for="lastname" class="input-label">성</label>
          </div>
          <div class="input-container name">
            <input id="firstname" class="input-field" placeholder=" " type="text">
            <label for="firstname" class="input-label">이름</label>
          </div>
        </div>
        <br>
        <br>
        <form class="signup-form" @submit.prevent="signUp">
          <div class="input-container">
            <input id="username" class="input-field" type="text" placeholder=" " v-model.trim="username">
            <label for="username" class="input-label">아이디</label>
          </div>
          <div class="input-container">
            <input id="password1" class="input-field" type="password" placeholder=" " v-model.trim="password1">
            <label for="password1" class="input-label">비밀번호</label>
          </div>
          <div class="input-container">
            <input id="password2" class="input-field" type="password" placeholder=" " v-model.trim="password2">
            <label for="password2" class="input-label">비밀번호 확인</label>
          </div>
          <div class="button-container">
            <button class="signup-button" type="submit">생성</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'

  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const store = useCounterStore()

  const signUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    store.signUp(payload)
  }
</script>

<style scoped>
.top-box {
  display: flex;
  justify-content: center;
}

.top {
  margin-top: 10px;
  margin-bottom: 10px;
  width: 60%;
  display: flex;
  justify-content: space-between;
}

.top-right {
  font-size: 70%;
  display: flex;
  flex-direction: column-reverse;
}

hr {
  margin-top: 0;
  margin-bottom: 20px
}

.signup-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.signup {
  width: 40%;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

h2 {
  margin-top: 10px;
  margin-bottom: 10px;
}

h5 {
  font-size: 15px;
  margin-bottom: 30px;
}

.input-field {
  width: 100%;
  margin-top: 5px;
  margin-bottom: 5px;
  padding: 10px 40px 10px 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  font-size: 16px;
  line-height: 1.5;
}

.namebox {
  display: flex;
  justify-content: space-between;
}

.input-container {
  position: relative;
  margin-top: 5px;
  margin-bottom: 5px;
}

.input-field:focus {
  outline: none;
  border-color: #111;
}

.input-field:focus + .input-label,
.input-field:not(:placeholder-shown) + .input-label {
  top: -10px;
  left: 10px;
  font-size: 12px;
  color: #111;
}

.input-label {
  position: absolute;
  top: 10px;
  left: 20px;
  font-size: 16px;
  color: #999;
  transition: all 0.3s ease;
  pointer-events: none;
}

.name {
  width: 48%;
}

.button-container {
  display: flex;
  justify-content: center;
}

.signup-button {
  width: 65px;
  height: 40px;
  background-color: #007bff; /* 버튼의 배경색 */
  color: white; /* 버튼의 텍스트 색상 */
  padding: 10px 10px; /* 내부 여백 */
  border: none; /* 테두리 제거 */
  border-radius: 10px; /* 둥근 모서리 */
  font-size: 16px; /* 글꼴 크기 */
  cursor: pointer; /* 마우스 커서를 포인터로 설정 */
  outline: none; /* 포커스시 테두리 제거 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 그림자 효과 */
  transition: background-color 0.3s; /* 호버 효과를 위한 색상 변화 전환 */
  margin-top: 50px;
}

.signup-button:hover {
  background-color: #0056b3; /* 마우스 호버시 버튼 색상 변화 */
}

</style>