<template>
  <div class="top-container">
    <div class="top-space">
      <span class="flag-icon flag-icon-ae"></span>
      <span class="flag-icon flag-icon-au"></span>
      <span class="flag-icon flag-icon-bh"></span>
      <span class="flag-icon flag-icon-bn"></span>
      <span class="flag-icon flag-icon-ca"></span>
      <span class="flag-icon flag-icon-ch"></span>
      <span class="flag-icon flag-icon-cn"></span>
      <span class="flag-icon flag-icon-dk"></span>
      <span class="flag-icon flag-icon-eu"></span>
      <span class="flag-icon flag-icon-gb"></span>
      <span class="flag-icon flag-icon-hk"></span>
      <span class="flag-icon flag-icon-id"></span>
      <span class="flag-icon flag-icon-jp"></span>
      <span class="flag-icon flag-icon-kr"></span>
      <span class="flag-icon flag-icon-my"></span>
      <span class="flag-icon flag-icon-no"></span>
      <span class="flag-icon flag-icon-nz"></span>
      <span class="flag-icon flag-icon-sa"></span>
      <span class="flag-icon flag-icon-se"></span>
      <span class="flag-icon flag-icon-sg"></span>
      <span class="flag-icon flag-icon-th"></span>
      <span class="flag-icon flag-icon-us"></span>
    </div>
    <br>
    <div class="title"><strong>환율 계산기</strong></div>
    <br>
    <p><strong>세계 여러 나라의 환율</strong>의 계산을 누구보다 <strong>간단</strong>하게 도와드릴게요.</p>
    <br>
  </div>
  <div class="body">
    <div class="calculator-container">
      <div class="calculator-space"></div>
      <div class="input">
        <p>보유하고 계신 통화량을 입력해주세요.</p>
        <div class="input-container">
          <input type="number" id="inputMoney" class="input-field" placeholder=" " v-model.trim="inputMoney">
          <label for="inputMoney" class="input-label">보유 통화량</label>
        </div>
      </div>
      <div class="calculator">
        <div class="left">
          <p>보유하고 계신 화폐를 선택해주세요.</p>
          <div class="custom-select-wrapper">
            <select v-model="selectedLeft" class="custom-select">
              <option v-for="exchangeInfo in exchangeInfos" :key="exchangeInfo.cur_unit" :value="exchangeInfo">
                {{ exchangeInfo.cur_nm }}
              </option>
            </select>
            <i class="fas fa-chevron-down select-chevron"></i>
          </div>
        </div>
        <div class="right">
          <p>변경하고자 하시는 화폐를 선택해주세요.</p>
          <div class="custom-select-wrapper">
            <select v-model="selectedRight" class="custom-select">
              <option v-for="exchangeInfo in exchangeInfos" :key="exchangeInfo.cur_unit" :value="exchangeInfo">
                {{ exchangeInfo.cur_nm }}
              </option>
            </select>
            <i class="fas fa-chevron-down select-chevron"></i>
          </div>
        </div>
      </div>
      <div v-if="calculate" class="result">
        입력하신 금액은 총 <span class="amount"><strong>{{ calculate }} {{ currencyUnit }}</strong></span>입니다.
        <div class="result-detail">
          ※ 계산된 결과는 십의 자리에서 반올림하여 표기됩니다.
        </div>
      </div>
    </div>
  </div>
  <br>
  <br>
  <br>
</template>

<script setup>
  import { ref, onMounted, computed, watch } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios'

  const store = useCounterStore()
  const exchangeInfos = ref()
  const selectedLeft = ref(null)
  const selectedRight = ref(null)
  const inputMoney = ref(null)
  const currencyUnit = ref()
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/exchange/`
    })
    .then((response) => {
      exchangeInfos.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  })
  
  const calculate = computed(() => {
    if (inputMoney.value && selectedLeft.value && selectedRight.value) {
      const roundedNum = Math.round(inputMoney.value * selectedLeft.value.bkpr / selectedRight.value.bkpr / 10) * 10
      currencyUnit.value = selectedRight.value.cur_nm.split(" ").slice(-1).join("")
      return roundedNum.toLocaleString()
    }
    else {
      return false
    }
  })

</script>

<style scoped>
.title {
  font-size: 60px;
}

.top-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: black;
  color: whitesmoke;
}

.top-space {
  height: 100px;
  display: flex;
  justify-content: center;
}

.left {
  width: 45%;
}

.right {
  width: 45%;
}

.calculator-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: transparent;
}

.input {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.calculator {
  display: flex;
  width: 50%;
  justify-content: space-between;
  margin-top: 50px;
}

.result {
  margin-top: 100px;
  font-size: 40px;
}

.custom-select-wrapper {
  position: relative;
  width: 100%; /* 필요에 따라 조정 */
}

.custom-select {
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  appearance: none; /* 기본 스타일 제거 */
  -webkit-appearance: none;
  -moz-appearance: none;
  background-color: white;
  width: 100%;
  font-size: 16px; /* 텍스트 크기 */
  cursor: pointer;
}

.select-chevron {
  position: absolute;
  top: 50%;
  right: 15px;
  transform: translateY(-50%); /* 세로 중앙 정렬 */
  color: #007bff; /* 아이콘 색상 */
  pointer-events: none; /* 클릭 이벤트 방지 */
}

.input-container {
  position: relative;
  width: 100%;
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

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.result-detail {
  margin-top: 40px;
  font-size: 10px;
  display: flex;
  flex-direction: row-reverse;
}

.amount {
  color: #dd572a;
}

.flag-icon {
  margin-left: 5px;
  margin-right: 5px;
}

.calculator-space {
  height: 150px;
}
</style>