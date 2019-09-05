<template>
  <div>
    <jumbotron></jumbotron>
  </div>
</template>

<script>
import Jumbotron from '@/components/home/Jumbotron'
import NavMenu from '@/components/common/NavMenu'

export default {
  name: 'Home',
  components: {
    'navmenu': NavMenu,
    'jumbotron': Jumbotron
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
</style>
