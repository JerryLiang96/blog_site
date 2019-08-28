<template>
  <el-menu :default-active="isActive" class="el-menu" mode="horizontal" @select="handleSelect" router>
    <el-menu-item v-for="(item, index) in items" :key="index" :index="item.path" :class="{'nav-home':!index}">
      {{ item.meta.title }}
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data () {
    return {
      isActive: this.$route.path,
      items: this.$router.options.routes[0].children
    }
  },
  methods: {
    handleSelect (key, path) {
    }
  }
}
</script>

<style>
.nav-home {
  font-size: 150%;
}
</style>
