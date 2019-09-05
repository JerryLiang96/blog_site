<template>
  <div>
    <header>
      <navmenu></navmenu>
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <myfooter></myfooter>
    </footer>
  </div>
</template>

<script>
import NavMenu from '@/components/common/NavMenu'
import MyFooter from '@/components/common/MyFooter'

export default {
  name: 'Main',
  components: {
    'navmenu': NavMenu,
    'myfooter': MyFooter
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
</style>
