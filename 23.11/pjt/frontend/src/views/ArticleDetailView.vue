<template>
  <div class="article-detail">
    <!-- 뒤로가기 -->
    <button @click="router.push({ name: 'article' })">뒤로 가기</button>
    
    <h1>Article Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ new Date(article.created_at).toLocaleString() }} | 수정일 : {{ new Date(article.updated_at).toLocaleString() }}</p>
    </div>
    <!-- 글 수정 -->
    <RouterLink v-if="isArticleAuthor" :to="{ name: 'ArticleEdit', params: { id: article.id }}">글 수정</RouterLink>
    <!-- 글 삭제 -->
    <button v-if="isArticleAuthor" @click="articleDelete">글 삭제</button>
    <br>
    <hr>
    <!-- 댓글 조회 -->
    <div v-if="comments">
      <h2>댓글 목록</h2>
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <!-- 댓글 수정 폼-->
          <div v-if="editingCommentId === comment.id">
            <textarea v-model="editingContent"></textarea>
            <button @click="updateComment(comment.id)">저장</button>
            <button @click="cancelEdit">취소</button>
          </div>
          <div v-else>
            <!-- 댓글 내용 -->
            <p>{{ comment.username }}</p>
            <p>{{ comment.content }}</p>
            <p>{{ new Date(comment.updated_at).toLocaleString() }}</p>
            <!-- 수정 버튼 -->
            <button v-if="isCommentAuthor(comment)" @click="editComment(comment.id, comment.content)">수정</button>
            <!-- 삭제 버튼 -->
            <button v-if="isCommentAuthor(comment)" @click="deleteComment(comment.id)">삭제</button>
          </div>
        </li>
      </ul>
    </div>
    <br>
    <hr>
    <!-- 댓글 작성 폼 -->
    <form @submit.prevent="createComment">
      <h2>댓글 작성</h2>
      <div>
        <label for="commentContent">댓글 내용:</label>
        <textarea v-model.trim="commentContent" id="commentContent"></textarea>
      </div>
      <input type="submit" value="댓글 작성">
    </form>
    
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const comments = ref('');
const commentContent = ref('');

// 글 delete(삭제)
const articleDelete = function () {
  axios({
    method: 'delete',
    url: `${store.DRF_URL}/article/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then((response) => {
    router.push({ name: 'article' });
  })
  .catch((error) => {
    console.log(error);
  });
};

// 댓글 read(조회)
const getComments = function () {
  axios({
    method: 'get',
    url: `${store.DRF_URL}/article/articles/${route.params.id}/getcomments/`
  })
  .then((response) => {
    comments.value = response.data;
  })
  .catch((error) => {
    console.log(error);
  });
};

// 댓글 create(생성)
const createComment = function () {
  axios({
    method: 'post',
    url: `${store.DRF_URL}/article/articles/${route.params.id}/comments/`,
    data: {
      content: commentContent.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then((response) => {
    commentContent.value = '';
    getComments();
  })  
  .catch((error) => {
    console.log(error);
  });
};

// 수정/삭제를 위한 isAuthor
const isArticleAuthor = computed(() => {
  return article.value && article.value.user && store.loginUsername === article.value.username;
});

const isCommentAuthor = (comment) => {
  return store.loginUsername === comment.username;
};

// 댓글 delete(삭제)
const deleteComment = (commentId) => {
  axios({
    method: 'delete',
    url: `${store.DRF_URL}/article/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then(() => {
    getComments(); 
  })
  .catch((error) => {
    console.log(error);
  });
};

// 댓글 update(수정)
const editingCommentId = ref(null);
const editingContent = ref('');

// 댓글 수정 - 댓글 수정 버튼 클릭 시
const editComment = (commentId, content) => {
  editingCommentId.value = commentId;
  editingContent.value = content;
};

// 댓글 수정 - 수정 취소
const cancelEdit = () => {
  editingCommentId.value = null;
  editingContent.value = '';
};

// 댓글 수정 - 댓글 업데이트 요청
const updateComment = (commentId) => {
  axios({
    method: 'put',
    url: `${store.DRF_URL}/article/comments/${commentId}/`,
    data: { content: editingContent.value },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then(() => {
    getComments();
    cancelEdit();
  })
  .catch((error) => {
    console.log(error);
  });
};

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.DRF_URL}/article/articles/${route.params.id}/`
  })
  .then((response) => {
    article.value = response.data;
    comments.value = response.data.comments;
  })
  .catch((error) => {
    console.log(error);
  });
  
  getComments()
});
</script>

<style scoped>
  .article-detail {
    width: 60%;
    margin: auto;
  }
  /* 글로벌 스타일 */
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    color: #333;
    background-color: #f7f8fa;
  }

  /* 컨테이너 스타일 */
  .container {
    max-width: 740px;
    margin: 30px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  /* 제목 스타일 */
  h1, h2 {
    color: #333;
    font-weight: normal;
    text-align: left;
    border-bottom: 2px solid #e1e1e1;
    padding-bottom: 5px;
    margin-bottom: 20px;
  }

  /* 텍스트 스타일 */
  p {
    line-height: 1.6;
    color: #666;
    margin-bottom: 10px;
  }

  /* 링크 및 버튼 스타일 */
  a, button {
    display: inline-block;
    text-decoration: none;
    color: #007aff;
    border: none;
    background-color: transparent;
    cursor: pointer;
    padding: 10px 15px;
    border-radius: 8px;
    transition: all 0.3s ease;
  }

  /* 버튼 호버 및 포커스 상태 */
  button:hover, button:focus, a:hover, a:focus {
    background-color: #f0f0f7;
  }

  /* 댓글 및 폼 스타일 */
  textarea, input[type='submit'] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #e1e1e1;
    border-radius: 8px;
    box-sizing: border-box;
  }

  /* 제출 버튼 스타일 */
  input[type='submit'] {
    background-color: #007aff;
    color: white;
    font-weight: bold;
    text-transform: uppercase;
  }

  /* 댓글 목록 스타일 */
  ul {
    list-style: none;
    padding: 0;
  }

  li {
    margin-bottom: 10px;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 8px;
  }

  /* 댓글 작성자 및 시간 스타일 */
  .comment-author, .comment-time {
    font-size: 0.9em;
    color: #007aff;
  }
</style>


