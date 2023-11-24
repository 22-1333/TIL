<template>
  <div class="mypage">
    <div class="mypage-info">
      <p class="info"><strong>내 정보</strong></p>
      <div class="top-right">
        <RouterLink class="password" :to="{ name: 'updatepassword' }">비밀번호 수정</RouterLink>
      </div>
    </div>
    <hr>
    <div class="mypage-body">
      <div class="greeting">
        {{ store.loginUsername }} 님, 안녕하세요.
      </div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="updateprofile">
        <RouterLink :to="{ name: 'updateprofile' }">회원정보 수정</RouterLink>
      </div>
      <div>

      </div>
    </div>
    <div class="good-container">
      <div class="bankfind-container">
        <BankFinder :userLocation="userLocation" />
      </div>
      <div class="recommend-container">
        <button class="recommend-button" @click="fetchRecommendation">추천 상품 받기</button>
        <div v-if="recommendedProducts">
          <RouterLink :to="{ name: 'interestDetail', params: { fin_prdt_cd: product.fin_prdt_cd }}" class="each-product" v-for="(product, index) in recommendedProducts" :key="index">
            <p>은행명: {{ product.company_name }}</p>
            <p>상품명: {{ product.product_name }}</p>
            <p>최대 금리: {{ product.interest_rate }}%</p>
          </RouterLink>
        </div>
        <div v-else>
          추천 상품이 없습니다.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  import BankFinder from '@/components/BankFinder.vue'
  import axios from 'axios'

  const store = useCounterStore();
  const userLocation = ref(null); // 사용자 위치 정보를 저장할 데이터

  onMounted(() => {
    // 사용자 위치 정보를 가져오는 함수
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          userLocation.value = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
        },
        (error) => {
          console.error('위치 정보를 가져오는 데 실패했습니다:', error);
        }
      );
    } else {
      console.error('이 브라우저는 Geolocation을 지원하지 않습니다.');
    }

  })
  
  const recommendedProducts = ref([])

  const fetchRecommendation = () => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/interest/recommend_deposit_product/${store.loginUsername}`
    })
      .then((response) => {
        recommendedProducts.value = response.data
      })
      .catch((error) => {
        console.error('추천 상품 조회 실패:', error);
      });
  }
</script>

<style scoped>
.space {
  height: 10px;
}

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
  margin-bottom: 10px;
  margin-top: 10px;
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
  text-align: center;
}

.password {
  display: flex;
  flex-direction: column-reverse;
  background-color: transparent; /* 배경색 없음 */
  color: #007BFF; /* 파란색 글자 */
  border: none; /* 테두리 없음 */
  padding: 0 16px; /* 상하 8px, 좌우 16px 패딩 */
  text-decoration: none; /* 텍스트 밑줄 없음 */
  font-size: 100%; /* 글자 크기 */
  margin: 4px 2px; /* 마진 설정 */
  cursor: pointer; /* 마우스 오버시 커서 변경 */
  transition: color 0.3s, text-decoration 0.3s; /* 색상과 텍스트 장식 전환 효과 */
  margin-top: 5px;
  margin-bottom: 0;
}

.password:hover {
  text-decoration: underline; /* 호버 시 밑줄 */
}

.top-right {
  font-size: 70%;
  display: flex;
  flex-direction: column-reverse;
}

.mypage-body {
  display: flex;
  flex-direction: column;
}

.updateprofile {
  display: flex;
  flex-direction: row-reverse;
}

.good-container {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

.bankfind-container {
  width: 45%;
  height: 450px;
  border: 1px solid #eaeaea;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background: #fff;
  overflow: hidden;
  margin-top: 10px;
  margin-bottom: 10px; /* Space below each card */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for transform and shadow */
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
}

.recommend-container {
  width: 45%; 
  height: 450px;
  border: 1px solid #eaeaea;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background: #fff;
  overflow: hidden;
  margin-top: 10px;
  margin-bottom: 10px; /* Space below each card */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for transform and shadow */
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
}

.recommend-button {
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
  margin-bottom: 10px;
}

.recommend-button:hover {
  background-color: #111; /* 마우스 오버 시 배경색 변경 */
}

.each-product {
  border: 2px black;
  border-radius: 5px;
}
</style>