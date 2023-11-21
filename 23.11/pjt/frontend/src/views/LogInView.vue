<template>
  <div class="login-container">
    <h5><strong>HomePage에 로그인하세요</strong></h5>
    <div class="input-container">
      <input type="text" id="username" class="input-field" placeholder=" " v-model.trim="username" required>
      <label for="username" class="input-label">username</label>
      <span class="input-icon"><i class="fas fa-search"></i></span>
    </div>
    <div class="input-container">
      <input type="password" id="password" class="input-field" placeholder=" " v-model.trim="password" required>
      <label for="password" class="input-label">비밀번호</label>
      <span class="input-icon"><i class="fas fa-search"></i></span>
    </div>
    <form class="login-button-container" @submit.prevent="logIn">
      <input type="submit" class="login-button">
    </form>
  </div>
  <div class="signup">
    <p>ID가 없으신가요? <span><RouterLink class="signup-link" :to="{ name: 'signup' }">지금 만드세요. </RouterLink>↗</span></p>
  </div>

</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink } from 'vue-router'

  const store = useCounterStore()
  const username = ref(null)
  const password = ref(null)

  const logIn = function () {
    const payload = {
      username: username.value,
      password: password.value
    }
    store.logIn(payload)
  }
</script>

<style scoped>
.login-container {
  text-align: center;
  padding-top: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

h5 {
  margin-bottom: 20px;
  color: #555;
}

.input-container {
  position: relative;
  margin: 10px;
  width: 40%;
  min-width: 400px;
}

.input-field {
  width: 100%;
  padding: 10px 40px 10px 20px;
  border: 1px solid #ccc;
  border-radius: 20px;
  font-size: 16px;
  line-height: 1.5;
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

.input-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  font-size: 16px;
  color: #ccc;
}

.login-button-container {
  margin-top: 30px;
  width: 40%;
  min-width: 400px;
  display: flex;
  flex-direction: row-reverse;
}

.login-button {
  padding: 10px 15px;
  background-color: #d3d3d3; 
  color: #fff; 
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #a9a9a9;
}

.signup {
  margin-top: 70px;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 10px;
}

.signup-link {
  text-decoration: none;
}
</style>
