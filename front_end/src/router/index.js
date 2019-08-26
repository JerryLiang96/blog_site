import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/apps/base/page/Home'
import BlogList from '@/apps/blog/page/BlogList'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/blog_list',
      name: 'BlogList',
      component: BlogList
    }
  ]
})
