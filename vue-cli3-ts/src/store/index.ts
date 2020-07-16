import Vue from 'vue';
import Vuex from 'vuex';
import loginStore from '@/store/modules/loginStore';
import usrtStore from '@/store/modules/userStore';

Vue.use(Vuex);
export default new Vuex.Store({
  modules: {
    loginStore: loginStore as any,
    userStore: usrtStore as any,
  },
});
