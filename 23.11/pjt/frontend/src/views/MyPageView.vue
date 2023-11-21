<template>
  <div class="mypage">
    <div class="mypage-info">
      <p class="info"><strong>내 정보</strong></p>
      <RouterLink class="password" :to="{ name: 'updatepassword' }">비밀번호 수정</RouterLink>
    </div>
    <hr>
    <div class="greeting">
      {{ store.loginUsername }} 님, 안녕하세요.
    </div>
    <div>
      <RouterLink :to="{ name: 'updateprofile' }">[회원정보 수정]</RouterLink>
      <RouterLink :to="{ name: 'profile', params: {username: store.loginUsername} }">[프로필 정보]</RouterLink>
    </div>
  </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()
</script>

<style scoped>
.mypage {
  width: 60%;
  margin: 5px auto;
  display: flex;
  flex-direction: column;
}

.mypage-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5px;
}

.info {
  margin: 0;
}

hr {
  margin-top: 0;
  margin-bottom: 50px;
}

.greeting {
  font-size: 30px;
  font-weight: bold;
}

.password {
  background-color: transparent; /* 배경색 없음 */
  color: #007BFF; /* 파란색 글자 */
  border: none; /* 테두리 없음 */
  padding: 8px 16px; /* 상하 8px, 좌우 16px 패딩 */
  text-align: center; /* 글자 중앙 정렬 */
  text-decoration: none; /* 텍스트 밑줄 없음 */
  display: inline-block; /* 인라인 블록 요소로 표시 */
  font-size: 14px; /* 글자 크기 */
  margin: 4px 2px; /* 마진 설정 */
  cursor: pointer; /* 마우스 오버시 커서 변경 */
  transition: color 0.3s, text-decoration 0.3s; /* 색상과 텍스트 장식 전환 효과 */
}

.password:hover {
  text-decoration: underline; /* 호버 시 밑줄 */
}


</style>