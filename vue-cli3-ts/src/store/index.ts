import Vue from 'vue';
import Vuex from 'vuex';
import loginStore from '@/store/modules/loginStore';

Vue.use(Vuex);
export default new Vuex.Store({
  modules: {
    loginStore: loginStore as any,
  },
});
