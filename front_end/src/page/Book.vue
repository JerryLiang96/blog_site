<template>
  <div class="container pt-5">
    <div class="card-columns mt-5">
      <card v-for="book in books" :key="book.id" :title="book.title" :body="book.body"></card>
    </div>
  </div>
</template>

<script>
import Card from '@/components/common/Card'

export default {
  name: 'Book', 
  components: {
    'card': Card
  },
  data () {
    return {
      books: []
    }
  },
  mounted () {
    this.axios
      .get('/api/book/')
      .then((response) => {
        this.books = response.data
      })
      .catch((error) => { // 请求失败处理
        console.log(error)
      })
  }
}

</script>

<style>
</style>
