import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/page/Main'
import Home from '@/page/Home'
import Book from '@/page/Book'
import Photography from '@/page/Photography'
import Movie from '@/page/Movie'
import Music from '@/page/Music'
import Paint from '@/page/Paint'
import About from '@/page/About'

Vue.use(Router)
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Main,
      children: [
        {
          path: '/',
          name: 'Home',
          component: Home,
          meta: {
            title: '主页'
          }
        },
        {
          path: '/book',
          name: 'Book',
          component: Book,
          meta: {
            title: '书籍'
          }
        },
        {
          path: '/photography',
          name: 'Photography',
          component: Photography,
          meta: {
            title: '摄影'
          }
        },
        {
          path: '/music',
          name: 'Music',
          component: Music,
          meta: {
            title: '音乐'
          }
        },
        {
          path: '/movie',
          name: 'Movie',
          component: Movie,
          meta: {
            title: '影视'
          }
        },
        {
          path: '/paint',
          name: 'Paint',
          component: Paint,
          meta: {
            title: '绘画'
          }
        },
        {
          path: '/about',
          name: 'About',
          component: About,
          meta: {
            title: '关于'
          }
        }
      ]
    }
  ]
})
