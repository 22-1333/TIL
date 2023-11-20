<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">CREATE</RouterLink>
    <ArticleList :articleList="articleList"/>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  import ArticleList from '@/components/ArticleList.vue'
  import axios from 'axios'

  const store = useCounterStore()
  
  const articleList = ref([])
  const getArticles = () => {
    axios({
      method: 'get',
      url: `${store.DRF_URL}/article/articles/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) =>{
        articleList.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  onMounted(() => {
    getArticles()
  })
</script>

<style>

</style>
