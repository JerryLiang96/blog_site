<template>
  <div>
    <jumbotron></jumbotron>
  </div>
</template>

<script>
import Jumbotron from '@/components/home/Jumbotron'

export default {
  name: 'Home',
  components: {
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
