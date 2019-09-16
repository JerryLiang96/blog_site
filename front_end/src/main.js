// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import App from './App'
import settings from '../settings'
import router from './router/index'
import axios from 'axios'
import VueAxios from 'vue-axios'

// 自定义全局配置
Vue.prototype.$settings = settings

// 调用插件
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(require('vue-wechat-title'))
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
