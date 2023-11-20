<template>
  <div>
    <h1>사이트명</h1>
  </div>

  <!-- <div class="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="image1.jpg" alt="Image 1">
      </div>
      <div class="carousel-item">
        <img src="image2.jpg" alt="Image 2">
      </div>
      <div class="carousel-item">
        <img src="image3.jpg" alt="Image 3">
      </div>
    </div>
    <a class="carousel-control-prev" onclick="moveSlide(-1)">&#10094;</a>
    <a class="carousel-control-next" onclick="moveSlide(1)">&#10095;</a>
  </div> -->

</template>

<script setup>
  import { ref, onMounted } from 'vue'

  // const slideIndex = ref(0)
  
  // const showSlides = (n) => {
  //   const i = ref(0)
  //   const slides = document.getElementsByClassName("carousel-item");
  //   if (n > slides.length - 1) {
  //     slideIndex = 0
  //   }    
  //   if (n < 0) {
  //     slideIndex = slides.length - 1
  //   }
  //   for (i = 0; i < slides.length; i++) {
  //     slides[i].style.display = "none";  
  //   }
  //   slides[slideIndex].style.display = "block";  
  // }

  // const moveSlide = (n) => {
  //   showSlides(slideIndex += n);
  // }
  
  // onMounted(() => {
  //   showSlides(slideIndex)
  // })
</script>

<style scoped>

</style>