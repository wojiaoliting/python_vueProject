import { Commit } from 'vuex';
import axios from 'axios';
import route from '@/router';
// 定义的 state 数据
class VuexState {
    public username: string = '';
}

const state: VuexState = new VuexState();
const mutations: any = {
    setUserName(stat: VuexState, userName: string) {
        (stat as any).username  = userName;
        // axios.defaults.headers.common[username] = userName;
        window.sessionStorage.username = userName;
    },
    AUTHORIZATION_TOKEN_SET(stat: VuexState, jwtToken: string[]): void {
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + jwtToken[0];
        // axios.defaults.headers.common['refresh'] = jwtToken[0];
        window.sessionStorage.Authorization = jwtToken[0] ? 'Bearer ' + jwtToken[0] : '';
        window.sessionStorage.refresh = jwtToken[1] ? jwtToken[1] : '';
    },
    logout(stat: VuexState): void {
        (stat as any).userName = '';
        delete axios.defaults.headers['Authorization'];
        // delete axios.defaults.headers.common['refresh'];
        // delete window.sessionStorage.Authorization;
        // delete window.sessionStorage.refresh;
        window.sessionStorage.clear();
        route.replace('/login');
    },
};
const actions: any = {
    // loginAction(context: { commit: Commit }, params: object) {
    //     context.commit('AUTHORIZATION_TOKEN_SET', params);
    // },
};
export default {
    namespaced: true, // 必须要开放
    state: () => ( state ),
    mutations,
    actions,
};

