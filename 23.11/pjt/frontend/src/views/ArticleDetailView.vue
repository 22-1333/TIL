<template>
  <div>
    <h1>Article Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
    </div>
    <button @click="articleDelete">삭제</button>
  </div>
</template>
  
<script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute, useRouter } from 'vue-router'
  
  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()
  const article = ref(null)

  const articleDelete = function () {
    axios({
      method: 'delete',
      url: `${store.DRF_URL}/article/articles/${route.params.id}/`
    })
    .then((response) => {
      router.push({name: 'article'})
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/article/articles/${route.params.id}/`
    })
      .then((response) => {
        article.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  })
</script>
  
<style>

</style>
  