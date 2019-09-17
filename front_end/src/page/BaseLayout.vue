<template>
  <div class="j-body d-flex flex-column">
    <header>
      <navmenu></navmenu>
    </header>
    <main class="j-main">
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
  name: 'BaseLayout',
  components: {
    'navmenu': NavMenu,
    'myfooter': MyFooter
  },
  data () {
    return {
    }
  }
}
</script>

<style>
.j-main {
  flex-shrink: 0 !important;
}

.j-body {
  height: 100%;
}
</style>
