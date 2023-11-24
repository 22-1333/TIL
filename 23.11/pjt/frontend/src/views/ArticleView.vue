<template>
  <div class="article-page">
    <div class="article-header">
      <h1>Article Page</h1>
      <RouterLink class="create-link" :to="{ name: 'CreateView' }">글 작성</RouterLink>
    </div>
    <div v-for="article in articleList" :key="article.id" class="article">
      <div>
        <h5>{{ article.id }}</h5>
        <p>작성자: <span class="username">{{ article.username }}</span></p>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <RouterLink class="detail-link" :to="{ name: 'DetailView', params: { id: article.id }}">Detail</RouterLink>
      </div>
    </div>
    <hr class="view-hr">
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
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
    .then((response) => {
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
  /* Article 페이지 스타일 */
  .article-page {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  .article-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .article-header h1 {
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }

  .create-link {
    text-decoration: none;
    background-color: #0071e3;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
    transition: background-color 0.2s;
  }

  .create-link:hover {
    background-color: #0054aa;
  }

  .article {
    background-color: #f8f8f8;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  }

  .article h5 {
    font-size: 18px;
    margin-bottom: 10px;
    color: #555;
  }

  .article p {
    margin-bottom: 10px;
  }

  .article .username {
    font-weight: bold;
  }

  .detail-link {
    text-decoration: none;
    background-color: #0071e3;
    color: #fff;
    padding: 5px 10px;
    border-radius: 3px;
    font-size: 14px;
    transition: background-color 0.2s;
  }

  .detail-link:hover {
    background-color: #0054aa;
  }

  .view-hr {
    border: none;
    border-top: 1px solid #ccc;
    margin-top: 20px;
  }
</style>