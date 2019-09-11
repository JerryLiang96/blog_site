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
html {
  background-image: url('../static/image/background.jpg');
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

body {
  height: 100%;
  background-color: rgba(0, 0, 0, 0);
}

#app {
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
