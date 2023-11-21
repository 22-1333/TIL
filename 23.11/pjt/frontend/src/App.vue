<template>
  <header class="header">
    <nav class="navbar">
      <div class="left">
        <RouterLink class="nav-item" :to="{ name: 'home' }"><strong>Home</strong></RouterLink>
      </div>
      <div class="login-items" v-if="store.isLogin">
        <RouterLink class="nav-item" :to="{ name: 'mypage', params: {username: store.loginUsername} }">MyPage</RouterLink>
        <form class="logout" @submit.prevent="store.logOut">
          <input class="nav-item" type="submit" value="logOut">
        </form>
      </div>
      <div v-else>
        <RouterLink class="login nav-item" :to="{ name: 'login' }">Login</RouterLink>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Noto Sans KR';
}
</style>

<style scoped>
.header {
  width: 100%;
  height: 50px;
  background-color: #f8f9fa; /* 연한 회색 배경 */
  display: flex;
  justify-content: center; /* 중앙 정렬 */
  align-items: center;
}

.navbar {
  width: 60%;
  display: flex;
  justify-content: space-between;
  list-style: none;
}

.login-items {
  display: flex;
  align-items: center;
  margin-right: 2px;
}

.nav-item {
  height: 80%;
  margin: 0 0px; /* 메뉴 항목 간격 조절 */
  font-size: 16px; /* 폰트 크기 */
  color: #333; /* 폰트 색상 */
  text-decoration: none; /* 밑줄 제거 */  
  transition: color 0.3s; /* 색상 변화 애니메이션 */
  position: relative;
}

.dropdown-content {
  display: none; /* 기본적으로 드롭다운 메뉴 숨김 */
  position: absolute; /* 상위 항목에 대해 절대 위치 */
  background-color: #f9f9f9; /* 드롭다운 메뉴 배경색 */
  min-width: 160px; /* 최소 너비 설정 */
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); /* 그림자 효과 */
  z-index: 1; /* 다른 요소 위에 표시 */
}

.dropdown-content a {
  color: black; /* 드롭다운 메뉴 항목 색상 */
  padding: 12px 16px; /* 여백 */
  text-decoration: none; /* 링크 밑줄 제거 */
  display: block; /* 블록 레벨 요소로 표시 */
  text-align: left; /* 왼쪽 정렬 */
}

.dropdown-content a:hover {
  background-color: #f1f1f1; /* 호버 시 배경색 변경 */
}

.nav-item:hover .dropdown-content {
  display: block; /* 마우스 오버 시 드롭다운 메뉴 표시 */
}

.login-items a,
.login-items form {
  margin: 0 15px; /* 메뉴 항목 간격 조절 */
  /* 필요한 스타일 속성 추가 */
}

.login, .login-items form input[type="submit"] {
  height: 70%;
  background-color: #333; /* 버튼 배경색을 검은색으로 설정 */
  color: white; /* 글자색을 흰색으로 설정 */
  border: none; /* 테두리 제거 */
  padding: 5px 15px; /* 상하 10px, 좌우 20px 패딩 설정 */
  border-radius: 20px; /* 타원형 모양을 만들기 위해 border-radius 설정 */
  cursor: pointer; /* 마우스 오버 시 커서 변경 */
  font-size: 16px; /* 폰트 크기 설정 */
  transition: background-color 0.3s; /* 배경색 변화에 애니메이션 효과 적용 */
}

.login:hover, .login-items form input[type="submit"]:hover {
  background-color: #111; /* 마우스 오버 시 배경색 변경 */
}

.logout {
  height: 70%;
  padding: 5px 15px; /* 상하 10px, 좌우 20px 패딩 설정 */
  margin: 0;
}
</style>