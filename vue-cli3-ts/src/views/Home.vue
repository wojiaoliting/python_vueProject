<template>
    <b-container fluid>
      <top-nav msg="❤ »» 后台管理系统" :userName="username" class="m-3"></top-nav>
      <b-row>
        <b-col class=" pl-3" cols="2">
          <left-nav></left-nav>
        </b-col>
        <b-col class="bg-dark pr-3" cols="10">
          <keep-alive>
            <router-view>
            </router-view>
          </keep-alive>
          
        </b-col>
      </b-row>
      <b-row class="footer">
          
      </b-row>
    </b-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TopNav from '@/components/TopNav.vue';
import LeftNav from '@/components/LeftNav.vue';
import { Action, State, namespace, Mutation } from 'vuex-class';
const loginModule = namespace('loginStore');
@Component({
  components: {
    TopNav,
    LeftNav,
  },
})
export default class App extends Vue {
    // state
    public username: string = window.sessionStorage.username;
}
</script>

<style lang="scss">
.container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
