<template>
  <button class="bank-button" @click="findNearestBank">가장 가까운 은행 찾기</button>
  <div>
    <RouterLink :to="{ name: 'bank'}" v-if="nearestBank">
      <p>은행 이름: {{ nearestBank.place_name }}</p>
      <p>주소: {{ nearestBank.address_name }}</p>
      <p>거리: {{ nearestBank.distance }}m</p>
    </RouterLink>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router'

export default {
  data() {
    return {
      nearestBank: null
    };
  },
  methods: {
    findNearestBank() {
      navigator.geolocation.getCurrentPosition((position) => {
        const { latitude, longitude } = position.coords;
        this.searchBank(latitude, longitude);
      }, (error) => {
        console.error(error);
      });
    },
    searchBank(latitude, longitude) {
      const places = new kakao.maps.services.Places();
      const callback = (result, status) => {
        if (status === kakao.maps.services.Status.OK) {
          this.nearestBank = result[0];
        }
      };
      places.keywordSearch('은행', callback, {
        location: new kakao.maps.LatLng(latitude, longitude),
        radius: 2000
      });
    }
  }
};
</script>

<style>
.bank-button {
  height: 40px;
  background-color: #333; /* 버튼 배경색을 검은색으로 설정 */
  color: white; /* 글자색을 흰색으로 설정 */
  border: none; /* 테두리 제거 */
  padding: 5px 15px; /* 상하 10px, 좌우 20px 패딩 설정 */
  border-radius: 20px; /* 타원형 모양을 만들기 위해 border-radius 설정 */
  cursor: pointer; /* 마우스 오버 시 커서 변경 */
  font-size: 16px; /* 폰트 크기 설정 */
  transition: background-color 0.3s; /* 배경색 변화에 애니메이션 효과 적용 */
  margin-top: 10px;
  margin-bottom: 50px;
}

</style>