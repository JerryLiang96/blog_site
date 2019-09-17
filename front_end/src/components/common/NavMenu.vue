<template>
  <div>
    <b-navbar toggleable="lg" type="dark" class="j-bar fixed-top shadow-sm">
      <div class="container">
        <b-navbar-brand class="j-brand" to="/">Jerry</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse class="j-cpllapse" id="nav-collapse" is-nav>
          <b-navbar-nav class="j-nav ml-auto">
            <b-nav-item v-for="(item, index) in items" :key="index" :to="item.path">
              {{ item.meta.title }}
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: this.$router.options.routes[0].children.slice(1)
    }
  }
}
</script>

<style>
.j-brand {
  font-style: italic;
}

.j-bar:after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.9);
  z-index: -1;
  filter: blur(5px);
}
</style>
