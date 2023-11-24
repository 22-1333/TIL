<template>
  <div class="update-article">
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div class="form-group">
        <label for="title">제목:</label>
        <input v-model.trim="article.title" id="title" type="text" class="form-control">
      </div>
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea v-model.trim="article.content" id="content" class="form-control"></textarea>
      </div>
      <div class="button-group">
        <button type="submit" class="submit-button">수정 완료</button>
        <!-- 뒤로가기 -->
        <button @click="router.push({ name: 'DetailView', params: { id: route.params.id } })" class="back-button">뒤로 가기</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref({ title: '', content: '' })

const loadArticle = () => {
  axios({
    method: 'get',
    url: `${store.DRF_URL}/article/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    article.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

const updateArticle = () => {
  axios({
    method: 'put',
    url: `${store.DRF_URL}/article/articles/${route.params.id}/`,
    data: article.value,
    headers: {
      Authorization: `Token ${store.token}`
  }
  })
  .then(() => {
    router.push({ name: 'DetailView' })
  })
  .catch((error) => {
    console.log(error)
  })
}

onMounted(() => {
  loadArticle()
})
</script>

<style scoped>
.update-article {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.update-article h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

.update-article form {
  background-color: #f8f8f8;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.update-article .form-group {
  margin-bottom: 15px;
}

.update-article label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

.update-article .form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.update-article textarea {
  resize: vertical;
  min-height: 150px;
}

.update-article .button-group {
  text-align: right;
}

.update-article .submit-button,
.update-article .back-button {
  background-color: #0071e3;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-left: 10px;
}

.update-article .submit-button:hover,
.update-article .back-button:hover {
  background-color: #0054aa;
}

.update-article .back-button {
  background-color: #ccc;
  color: #333;
  margin-left: 0;
}
</style>
