<template>
  <div class="top">
    <div v-if="isRegistered">
      현재 가입한 상품의 상세 정보를 확인하고 있습니다. 빼먹은 정보는 없는지 꼼꼼하게 확인해보세요!
    </div>
    <div v-else>
      <div v-if="isDeposit">
        현재 예금 상품의 상세 정보를 확인하고 있습니다. 목돈이 생기셨다면 예금을 활용해 굴려보세요!
      </div>
      <div v-else>
        현재 적금 상품의 상세 정보를 확인하고 있습니다. 조금씩 아껴서 목돈을 만들어보세요!
      </div>
    </div>
  </div>
  <div v-if="product" class="interest-detail-page">
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="name-container">
      <div class="product-name">
        {{ product.fin_prdt_nm }}
      </div>
      <div class="bank-name">
        <div>
          {{ product.kor_co_nm }},
        </div>
        <div class="register-button" @click="register">
          <div v-if="isRegistered">Home을 통해 탈퇴하기 <i class="fas fa-chevron-right blue-icon"></i></div>
          <div v-else>Home과 함께 가입하기 <i class="fas fa-chevron-right blue-icon"></i></div>
        </div>
      </div>
    </div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="result-detail">
      <div class="result-card-container">
        <div class="result-card">
          <div class="result-name">공시 제출월</div>
          <div class="result-contents">{{ product.dcls_month.slice(0, 4) }}년 {{ product.dcls_month.slice(4, 6) }}월</div>
        </div>
        <div class="result-card">
          <div class="result-name">가입 방법</div>
          <div class="result-contents">{{ product.join_way }}</div>
        </div>
        <div class="result-card">
          <div class="result-name">가입 대상</div>
          <div class="result-contents">
            {{ joinDeny[product.join_deny] }}
            <br>
            {{ product.join_member }}
          </div>
          <div></div>
        </div>
        <div class="result-card">
          <div class="result-name">최고 한도</div>
          <div class="result-contents" v-if="product.max_limit">{{ product.max_limit.toLocaleString() }}원</div>
          <div class="result-contents" v-else>최고 한도 제한 없음</div>
        </div>
        <div class="result-card">
          <div class="result-name">공시 날짜</div>
          <div v-if="product.dcls_strt_day && product.dcls_end_day" class="result-contents">
            <div>
              {{ product.dcls_strt_day.slice(0, 4) }}년 {{ product.dcls_strt_day.slice(4, 6) }}월 {{ product.dcls_strt_day.slice(6, 8) }}일 부터
            </div>
            <div>
              {{ product.dcls_end_day.slice(0, 4) }}년 {{ product.dcls_end_day.slice(4, 6) }}월 {{ product.dcls_end_day.slice(6, 8) }}일 까지
            </div>
          </div>
          <div v-else class="result-contents">-</div>
        </div>
      </div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="result-special-container">
        <div class="space"></div>
        <div v-if="product.etc_note">
          ※{{ product.etc_note }}
        </div>
        <div v-if="product.mtrt_int">
          <div class="detail-space"></div>
          ※{{ product.mtrt_int }}
        </div>
        <div v-if="product.spcl_cnd">
          <div class="detail-space"></div>
          ※{{ product.spcl_cnd }}
        </div>
        <div class="detail-space"></div>
      </div>
    </div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="option-container">
      <hr>
      <div class="option-box">
        <div class="option-content six">
          <div class="option-month">6개월</div>
          <div class="option-circle">{{ options["6"] }}</div>
        </div>
        <div class="option-content twelve">
          <div class="option-month">12개월</div>
          <div class="option-circle">{{ options["12"] }}</div>
        </div>
        <div class="option-content twentyfour">
          <div class="option-month">24개월</div>
          <div class="option-circle">{{ options["24"] }}</div>
        </div>
        <div class="option-content thirtysix">
          <div class="option-month">36개월</div>
          <div class="option-circle">{{ options["36"] }}</div>
        </div>
      </div>
      <hr>
    </div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
    <div class="space"></div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { onMounted, ref, computed } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router'

  const store = useCounterStore()
  const route = useRoute()
  const product = ref(null)
  const option = ref(null)
  const options = ref({"6": "-", "12": "-", "24": "-", "36": "-"})
  const joinDeny = ref({1: "제한없음", 2: "서민전용", 3: "일부제한"})

  const register = () => {
    axios({
      method: 'post',
      url: `${store.DRF_URL}/interest/register/${product.value.fin_prdt_cd}/${store.loginUsername}/`
    })
      .then((response) => {
        store.getRegisteredDepositList()
        store.getRegisteredInstallmentSavingList()
      })
      .catch((error) => {
        console.error(error)
      })
  }

  const isRegistered = computed(() => {
    const inList = ref(false)
    if (product.value && product.value.product_type === 0) {
      for (const registeredDeposit of store.registeredDepositList) {
        if (registeredDeposit === product.value.fin_prdt_cd) {
          inList.value = true
          break
        }
      }
      return inList.value
    }

    if (product.value && product.value.product_type === 1) {
      for (const registeredInstallmentSaving of store.registeredInstallmentSavingList) {
        if (registeredInstallmentSaving === product.value.fin_prdt_cd) {
          inList.value = true
          break
        }
      }
    }
    
    return inList.value
    
  })

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/interest/${route.params.fin_prdt_cd}`
    })
      .then((response) => {
        product.value = response.data.product
        option.value = response.data.option
      })
      .then((response) => {
        for (const optionInfo of option.value) {
          options.value[optionInfo.save_trm] = optionInfo.intr_rate2
        }
      })
      .catch((error) => {
        console.error(error)
      })
  })

  const isDeposit = computed(() => {
    if (product.value && product.value.product_type === 0) {
      return true
    }
    return false
  })
</script>

<style>
.space {
  height: 10px;
}

.detail-space {
  height: 3px;
}

.top {
  height: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12px;
  color: #6E6E73;
}

.interest-detail-page {
  display: flex;
  flex-direction: column;
  background-color:  #f8f9fa;
  align-items: center;
}

.name-container {
  width: 70%;
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}

.product-name {
  font-size: 40px;
}

.bank-name {
  display: flex;
  flex-direction: column;
  font-size: 20px;
}

.result-detail {
  width: 80%;
  display: flex;
  flex-direction: column;
}

.result-card-container {
  display: flex;
  justify-content: space-between;
}

.result-card {
  width: 230px;
  height: 230px;
  border: 1px solid #eaeaea;
  border-radius: 40px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background: #fff;
  overflow: hidden;
  margin-top: 10px;
  margin-bottom: 10px; /* Space below each card */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for transform and shadow */
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.result-name {
  margin-top: 10px;
  margin-bottom: 10px;
  font-weight: bold;
}

.result-contents {
  margin: auto;
  text-align: center;
}

.option-container {
  width: 50%;
}

.option-container hr {
  margin: 0;
}

.option-box {
  display: flex;
  justify-content: space-around;
}

.option-circle {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background-color: white;
  margin-bottom: 15px;
  color: #999;
}

.option-content {
  display: flex;
  flex-direction: column;
}

.option-month {
  text-align: center;
  margin-top: 15px;
  margin-bottom: 15px;
  color: #333;
}

.result-special-container {
  font-size: 12px;
}

.register-button:hover {
  cursor: pointer;
}
</style>
