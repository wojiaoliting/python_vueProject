import Vue from 'vue';
import App from './App.vue';
import Constants from './constants';
import './registerServiceWorker';
import router from './router';
import store from './store';
import axios from 'axios';
import { BootstrapVue, IconsPlugin, FormInputPlugin, FormPlugin} from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import './assets/scss/custom.scss';

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(FormPlugin);
Vue.use(FormInputPlugin);

Vue.config.productionTip = false;

// 设置axios的请求Host（作用在axios.get()或者axios.post()方法上）
axios.defaults.baseURL = Constants.REQUEST_HOST;
router.beforeEach((to, from, next) => {
  if (to.name === 'Login') {
    return next();
  }
  const user = window.sessionStorage.username;
  if (to.name !== 'Login' && !user) {
    return next({
      path: '/login',
      query: { needToLogin: 'true' },
    });
  } else {
    return next();
  }

  // if (to.matched.some((record) => record.meta.requiresAuth)) {
  //     // store不写成(store as any)会报错

  // } else {
  //     next();
  // }
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
