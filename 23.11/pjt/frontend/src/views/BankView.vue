<template>
  <div class="top-container">
    <div class="top-space"></div>
    <div class="bank-top">
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
    <div class="body-space"></div>
    <div class="map-body">
      <div class="tablet">
        <div class="status-bar"></div>
        <div class="screen">
          <Map :si="si" :gu="gu" :bank="bank"></Map>
          <div class="home-button"></div>
        </div>
      </div>
      <div class="map-space"></div>
      <div class="iphone">
        <div class="notch"></div>
        <div class="notifications">
          <div class="notification">
            <div class="notification-content">
              <p class="app-name">시를 선택하세요.</p>
              <select class="option-box" v-model="si" @change="selectSi">
                <option class="option" v-for="siInfo in siList" :key="siInfo.code" :value="siInfo.name">{{ siInfo.name }}</option>
              </select>
            </div>
          </div>
          <div class="notification">
            <div class="notification-content">
              <p class="app-name">구를 선택하세요.</p>
              <select class="option-box" v-model="gu">
                <option class="option" v-if="!si" value="">시를 선택해주세요.</option>
                <option class="option" v-for="guInfo, index in guList" :key="guInfo.code" :value="guInfo.name.split(' ')[1]">
                  <p v-if="index">
                    {{ guInfo.name.split(' ')[1] }}
                  </p>
                </option>
              </select>
            </div>
          </div>
          <div class="notification">
            <div class="notification-content">
              <p class="app-name">은행을 선택하세요.</p>
              <select class="option-box" v-model="bank">
                <option class="option" v-for="bankname in store.depositBankList" :value="bankname">{{ bankname }}</option>
              </select>
            </div>
          </div>
        </div>
        <div class="iphone-home-button"></div>
      </div>
    </div>
  </div>
  <br>
  <br>
  <br>
  <br>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import Map from '@/components/Map.vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()

  const si = ref()
  const gu = ref()
  const bank = ref()

  const siList = ref([])
  const guList = ref([])

  onMounted(() => {
    store.getDepositList()

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
    gu.value = ""

    const guUrl = ref()
    const siCode = ref()

    for (const siIndex in siList.value) {
      if (siList.value[siIndex].name === si.value) {
        siCode.value = siList.value[siIndex].code
        break
      }
    }

    guUrl.value = siCode.value.substring(0, 2)

    axios({
      method: 'get',
      url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${guUrl.value}*000000`
    })
      .then((response) => {
        guList.value = response.data.regcodes
      })
      .catch((error) => {
        console.log(error)
      })
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

.bank-top {
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
  align-items: flex-end;
}

.map-space {
  width: 50px;
}

.tablet {
  width: 800px; /* 태블릿의 너비 */
  height: 600px; /* 태블릿의 높이 */
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

.iphone {
  width: 300px;
  height: 500px;
  background-size: cover;
  color: black;
  border-radius: 38px;
  padding: 20px;
  box-sizing: border-box;
  position: relative;
  border: 10px solid black;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); /* 그림자 효과 */
}

.notch {
  width: 130px; /* 타원의 가로 길이 */
  height: 30px; /* 타원의 세로 길이 */
  background-color: black;
  position: absolute;
  top: 5px; /* 노치의 상단 위치를 조정 */
  left: 50%;
  transform: translateX(-50%);
  border-radius: 15px;
}

.notifications {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: transparent;
  z-index: 2;
}

.notification {
  width: 80%;
  display: flex;
  padding: 10px;
  border-radius: 10px;
  z-index: 50;
  background-color: rgba(0, 0, 0, 0.6);
  margin: 5px;
}

.app-icon {
  width: 40px;
  height: 40px;
  background: white;
  border-radius: 8px;
  margin-right: 10px;
  text-align: center;
  font-size: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.notification-content {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  margin: 10px;
}

.app-name {
  font-weight: 100;
  font-size: 13px;
  margin-bottom: 5px;
  color: white;
}

.notification-text {
  font-size: 14px;
}

/* Include more styles as needed */

/* Use a font awesome icon for the battery */
.fa-battery-three-quarters {
  color: #fff;
}

/* ...other styles for lock screen elements... */

.option-box {
  height: 40px;
  width: 100%;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.1);
  font-size: 15px;
  padding-left: 10px;
  margin-top: 0; /* 상단 마진 제거 */
}

.option {
  font-size: 15px;
}

.iphone-home-button {
  position: absolute;
  bottom: 7px; /* 하단에서의 위치 */
  left: 50%; /* 중앙 정렬 */
  transform: translateX(-50%); /* 중앙 정렬 보정 */
  width: 100px; /* 홈 버튼의 너비 */
  height: 4px; /* 홈 버튼의 높이 */
  background-color: #222; /* 홈 버튼의 배경색 */
  border-radius: 30px;
  z-index: 10;
}

</style>