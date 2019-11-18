<template>
  <button class="shadow card">
    <img v-if="image[0]" :src="image[0].img" class="card-img-top">
    <div class="card-body">
      <h5 class="card-title">
        {{ title }}
      </h5>
      <b-badge pill v-for="t in tag" :key="t.id" class="label label-info">{{ t.name }}<span></span></b-badge>
      <p class="card-text"><small class="text-muted">{{ time }}</small></p>
    </div>
  </button>
</template>

<script>
export default {
  name: 'Card',
  props: ['id', 'title', 'body', 'tag', 'image', 'm-time'],
  data () {
    return {
      time: this.$props.mTime.slice(0, 10)
    }
  }
}

</script>
