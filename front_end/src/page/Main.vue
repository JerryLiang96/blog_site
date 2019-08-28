<template>
  <el-container>
    <el-header>
      <navmenu></navmenu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
import NavMenu from '@/components/common/NavMenu'

export default {
  name: 'Main',
  components: {
    'navmenu': NavMenu
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
</style>
