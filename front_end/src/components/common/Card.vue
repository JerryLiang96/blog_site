<template>
  <div class="card">
    <img src="" class="card-img-top" alt="">
    <div class="card-body">
      <h5 class="card-title">
        {{ title }}
      </h5>
      <p class="card-text">
        {{ body }}
      </p>
      <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ['id', 'title', 'body']
}
</script>
