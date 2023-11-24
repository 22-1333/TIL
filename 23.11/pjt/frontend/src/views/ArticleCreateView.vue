<template>
  <div class="apple-style">
    <h1 class="apple-title">게시글 작성</h1>
    <form @submit.prevent="createArticle" class="apple-form">
      <div class="form-group">
        <label for="title" class="form-label">제목:</label>
        <input type="text" v-model.trim="title" id="title" class="form-input">
      </div>
      <div class="form-group">
        <label for="content" class="form-label">내용:</label>
        <textarea v-model.trim="content" id="content" class="form-textarea"></textarea>
      </div>
      <div class="article-bottom">
        <input type="submit" value="게시글 작성" class="submit-button">
        <button @click="router.push({ name: 'article' })" class="back-button">뒤로 가기</button>
      </div>
    </form>
  </div>
</template>


<script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router'

  const title = ref(null)
  const content = ref(null)
  const store = useCounterStore()
  const router = useRouter()

  const createArticle = function () {
    axios({
      method: 'post',
      url: `${store.DRF_URL}/article/articles/`,
      data: {
        title: title.value,
        content: content.value,
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((response) => {
        router.push({ name: 'article' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
</script>

<style scoped>
.apple-style {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.apple-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

.apple-form {
  background-color: #f8f8f8;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
  text-align: left;
}

.form-label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.form-textarea {
  resize: vertical;
  min-height: 150px;
}

.submit-button {
  background-color: #0071e3;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-button:hover {
  background-color: #0054aa;
}

.back-button {
  background-color: #ccc;
  color: #333;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.back-button:hover {
  background-color: #999;
}

.article-bottom {
  display: flex;
  justify-content: space-between;
}
</style>
