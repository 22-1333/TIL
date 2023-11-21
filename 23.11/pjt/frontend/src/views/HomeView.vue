<template>
  <div class="temp">
  </div>
  <div class="menu-container">
    <nav class="menu-bar">
      <ul>
        <li>
          <RouterLink class="link" :to="{ name: 'interest'}">예적금 금리 비교</RouterLink>
        </li>
        <li>
          <RouterLink class="link" :to="{ name: 'exchange'}">환율계산기</RouterLink>
        </li>
        <li>
          <RouterLink class="link" :to="{ name: 'bank'}">은행 찾기</RouterLink>
        </li>
        <li>
          <RouterLink class="link" :to="{ name: 'article'}">커뮤니티</RouterLink>
        </li>
      </ul>
    </nav>
  </div>

</template>

<script setup>
  import { ref, onMounted } from 'vue'

</script>

<style scoped>
.temp {
  height: 450px; /* 임시 공간의 높이 설정 */
}

.menu-container {
  display: flex; /* Flexbox 사용 */
  justify-content: center; /* 가로 방향 중앙 정렬 */
  align-items: center; /* 세로 방향 중앙 정렬 */
  margin: 0 auto; /* 수평 중앙 정렬 */
  background-color: #2F2F2F; /* 매우 어두운 회색 배경 */
  border-radius: 10px; /* 둥근 모서리 */
  width: max-content; /* 메뉴 너비를 내용에 맞춤 (fit-content 대신 max-content 사용) */
  padding: 10px 20px; /* 내부 패딩 */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5); /* 메뉴바에 그림자 추가 */
}

.menu-bar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* 메뉴바의 전체 높이를 채우도록 설정 */
}

.menu-bar li {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 20px; /* 좌우 패딩을 줄여 조정 */
}

.menu-bar li:not(:last-child)::after {
  content: "|";
  color: #FFF; /* 구분선 색상을 하얀색으로 설정 */
  padding-left: 30px;
  height: 100%; /* 구분선의 높이를 늘림 */
  display: flex;
  align-items: center; /* 구분선을 수직 중앙으로 정렬 */
}

.link {
  text-decoration: none;
  color: #FFF;
  font-weight: bold;
  font-size: 16px;
  display: block; /* 링크를 블록 요소로 설정 */
  padding: 10px 0; /* 링크 상하 패딩 추가 */
}
</style>