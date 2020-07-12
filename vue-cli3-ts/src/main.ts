import Vue from 'vue';
import App from './App.vue';
import Constants from './constants';
import './registerServiceWorker';
import router from './router';
import store from './store';
import axios from 'axios';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import './assets/scss/custom.scss';
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.config.productionTip = false;

// 设置axios的请求Host（作用在axios.get()或者axios.post()方法上）
axios.defaults.baseURL = Constants.REQUEST_HOST;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
