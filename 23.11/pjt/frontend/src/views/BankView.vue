<template>
  <div class="top-container">
    <div class="top-space"></div>
    <div class="top">
      <div><strong>은행 검색</strong></div>
      <div class="top-right">내 주변 은행 찾기</div>
    </div>
  </div>
  <hr>
  <div class="body-space"></div>
  <div class="body-space"></div>
  <div class="body-space"></div>
  <div class="body-space"></div>
  <div class="body-space"></div>
  <div class="body-space"></div>
  <div class="body">
    <div><strong>원하는 위치</strong>로부터,</div>
    <div><strong>가까운 은행</strong>을 탐색해보세요.</div>
    <div class="body-space"></div>
    <div class="body-space"></div>
    <div class="map-body">
      <div class="tablet">
        <div class="status-bar">
        </div>
        <div class="screen">
          <Map :si="si" :gu="gu" :bank="bank"></Map>
          <div class="home-button"></div>
        </div>
      </div>
      <div class="map-space"></div>
      <div class="choose">
        <div class="choose-detail">장소를 선택하세요.</div>
        <select v-model="si" @change="selectSi">
          <option v-for="siInfo in siList" :key="siInfo.code" :value="siInfo.name">{{ siInfo.name }}</option>
        </select>
        <select v-model="gu">
          <option v-if="!guList" value="">시를 선택해주세요.</option>
          <option v-for="guInfo in guList" :key="guInfo.code" :value="guInfo.name">{{ guInfo.name }}</option>
        </select>
        <select v-model="bank" @change="search">
          <option value="우리은행">우리은행</option>
          <option value="신한은행">신한은행</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import Map from '@/components/Map.vue'
  import axios from 'axios'

  const si = ref()
  const gu = ref()
  const bank = ref()

  const siList = ref([])
  const guList = ref()
  const bankList = ref()

  onMounted(() => {
    axios({
      method: 'get',
      url: "https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000",
    })
      .then((response) => {
        siList.value = response.data.regcodes
      })
      .catch((error) => {
        console.log(error)
      })
  })

  
  const selectSi = () => {
    const guUrl = ref()
    // axios({
    //   method: 'get',
    //   url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${}*`
    // })
  }
  
</script>

<style scoped>
hr {
  margin: 0;
}

.top-container {
  display: flex;
  background-color: #f8f9fa;
  flex-direction: column;
  align-items: center;
}

.top-space {
  height: 10px;
}

.top {
  margin-bottom: 20px;
  width: 60%;
  display: flex;
  justify-content: space-between;
}

.body-space {
  height: 20px;
}

.body {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 50px;
}

.map-body {
  display: flex;
}

.map-space {
  width: 50px;
}

.tablet {
  width: 700px; /* 태블릿의 너비 */
  height: 500px; /* 태블릿의 높이 */
  background-color: transparent; /* 태블릿의 배경색 */
  border: 15px solid black;
  border-radius: 25px; /* 라운드 코너 */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); /* 그림자 효과 */
  overflow: hidden; /* 내부 요소가 코너를 넘어가지 않게 */
  position: relative; /* 내부 절대 포지션 요소의 기준 */
}

.status-bar {
  height: 0x; /* 상태 표시줄의 높이 */
  background-color: transparent; /* 상태 표시줄의 배경색 */
  display: flex;
  align-items: center;
  padding: 0 10px; /* 내부 여백 */
  border-top-left-radius: 50px; /* 상단 좌측 라운드 코너 */
  border-top-right-radius: 50px; /* 상단 우측 라운드 코너 */
}

.screen {
  width: 100%;
  height: 100%;
}

.home-button {
  position: absolute;
  bottom: 7px; /* 하단에서의 위치 */
  left: 50%; /* 중앙 정렬 */
  transform: translateX(-50%); /* 중앙 정렬 보정 */
  width: 250px; /* 홈 버튼의 너비 */
  height: 4px; /* 홈 버튼의 높이 */
  background-color: #222; /* 홈 버튼의 배경색 */
  border-radius: 30px;
  z-index: 10;
}

.top-right {
  font-size: 70%;
  display: flex;
  flex-direction: column-reverse;
}

.choose {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.choose-detail {
  font-size: 20px;
  margin: 5px auto;
}

</style>