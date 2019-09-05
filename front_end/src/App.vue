<template>
  <div id="app">
    <router-view v-wechat-title="this.$route.meta.title"></router-view>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url('../static/image/background.jpg');
  background-repeat: no-repeat;
  background-size: 100%;
}
</style>
