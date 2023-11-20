<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem 
      v-for="article in articleList"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
  import ArticleListItem from '@/components/ArticleListItem.vue'

  defineProps({
    articleList: Object,
    a: Number
  })
</script>
  