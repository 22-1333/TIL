<template>
  <div class="home-page">
    <div class="home-title">
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div>{{ typedText1 }}</div>
      <div class="typing-title">{{ typedText }}</div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
      <div class="space"></div>
    </div>
    <img src="/browser.png" alt="">
  </div>
</template>

<script setup>
  import { onMounted, ref } from "vue"

  const title = "편하게 이용하실 수 있으셨나요?"
  const typedText = ref("")
  let index = 0

  const typeTitle = () => {
    if (index < title.length) {
      typedText.value += title.charAt(index)
      index++
      setTimeout(typeTitle, 100)
    }
  }

  const title1 = '복잡한 요즘 사이트들,'
  const typedText1 = ref('')
  let index1 = 0

  const typeFirst = () => {
    if (index1 < title1.length) {
      typedText1.value += title1.charAt(index1)
      index1++
      setTimeout(typeFirst, 100)
    }
  }

  onMounted(() => {
    typeFirst()
    setTimeout(typeTitle, 1800)
  })
</script>

<style scoped>
.space {
  height: 10px;
}

.home-title {
  text-align: center;
  font-size: 100px;
  color: white;
  font-weight: bold;
}

.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: black;
}


</style>
