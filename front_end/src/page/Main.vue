<template>
  <div class="j-body d-flex flex-column">
    <header>
      <navmenu></navmenu>
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer class="mt-auto py-3">
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

<style>
.j-body {
  height: 100%;
}
</style>
