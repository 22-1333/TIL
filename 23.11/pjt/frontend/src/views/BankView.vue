<template>
  <div>
    <Map></Map>
  </div>
</template>

<script setup>
  import Map from '@/components/Map.vue'
  import { onMounted } from 'vue'

  onMounted(() => {
    var container = document.getElementById('map')
		var options = {
			center: new kakao.maps.LatLng(33.450701, 126.570667),
			level: 3
		}

		var map = new kakao.maps.Map(container, options)

    var places = new kakao.maps.services.Places()

    var callback = function(result, status) {
        if (status === kakao.maps.services.Status.OK) {
            console.log(result)
        }
    };

    places.keywordSearch('역삼 은행', callback)
    var clusterer = new kakao.maps.MarkerClusterer({
    map: map,
    markers: markers,
    gridSize: 35,
    averageCenter: true,
    minLevel: 6,
    disableClickZoom: true,
    styles: [{
        width : '53px', height : '52px',
        background: 'url(cluster.png) no-repeat',
        color: '#fff',
        textAlign: 'center',
        lineHeight: '54px'
    }]
})


    var marker = new kakao.maps.Marker({
      position: new kakao.maps.LatLng( 37.23, 126.67 )
    });

    clusterer.addMarker(marker);

  })
</script>

<style scoped>

</style>