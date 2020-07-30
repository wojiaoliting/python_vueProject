import { Commit } from 'vuex';
import axios from 'axios';
import route from '@/router';
// 定义的 state 数据
class VuexState {
    public pageSize: number = 10;
    public imgUrl: string = 'http://localhost:8001';
}

const state: VuexState = new VuexState();
const mutations: any = {
    // getPageSizeList(stat: VuexState, request: object): void {
    //     interface request {
    //         page: number,
    //     }
    //     axios.get('admins/')
    // },
};
const actions: any = {
    // getPageSizeList(context: { commit: Commit }, params: object) {
    //     context.commit('getPageSizeList', params);
    // },
};
export default {
    namespaced: true, // 必须要开放
    state: () => ( state ),
    mutations,
    actions,
};

