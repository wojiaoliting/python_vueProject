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
        (stat as any).state.username  = userName;
        const username: string = 'username';
        axios.defaults.headers.common[username] = userName;
        window.sessionStorage.username = userName;
    },
    AUTHORIZATION_TOKEN_SET(stat: VuexState, jwtToken: string): void {
        const authorizationHeader: string = 'JWT ' + jwtToken;
        const Authorization: string = 'Authorization';
        axios.defaults.headers.common[Authorization] = authorizationHeader;
        window.sessionStorage.AuthorizationHeader = authorizationHeader;
    },
    logout(stat: VuexState): void {
        delete window.sessionStorage.AuthorizationHeader;
        const Authorization: string = 'Authorization';
        delete axios.defaults.headers.common[Authorization];
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
    state: () => ({ state }),
    mutations,
    actions,
};

