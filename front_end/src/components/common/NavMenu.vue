<template>
  <div>
    <b-navbar toggleable="lg" type="dark" class="fixed-top shadow-sm">
      <div class=" container">
        <b-navbar-brand to="/">Jerry</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
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
  },
  methods: {
  }
}
</script>

<style>
</style>
