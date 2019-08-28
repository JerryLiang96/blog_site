<template>
  <carousel></carousel>
</template>

<script>
import Carousel from '@/components/home/Carousel'
import NavMenu from '@/components/common/NavMenu'

export default {
  name: 'Home',
  components: {
    'navmenu': NavMenu,
    'carousel': Carousel
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
</style>
