<template>
  <div class="min-vh-100 position-relative" style="margin-bottom:30rem">
    <b-container fluid style="min-height:100vh">
      <audio src="@/assets/audio/know.mp3" autoplay></audio>
      <top-nav class="topbar m-3" msg="❤ »» 后台管理系统" :userName="username"></top-nav>
      <b-row class="pr-3 pl-3" style="min-height:90vh">
        <b-col class="p-0" cols="2">
          <left-nav></left-nav>
        </b-col>
        <b-col class="bg-dark" cols="10">
          <!-- <keep-alive> -->
            <transition name="fade" mode="out-in">
              <router-view v-if="isRouterAlive">
              </router-view>
            </transition>
          <!-- </keep-alive> -->
        </b-col>
      </b-row>
    </b-container>
    <b-row class="footer position-absolute text-light bg-dark w-100 ml-0 mr-0 pt-4" style="min-height:30rem;bottom:-32rem;">
          <div class="container bg-dark"><div class="row justify-content-center  bg-dark">
            <div class="text-center text-sm-right col-sm order-sm-3 col-12">
              <a href="/" class="d-inline-block mx-auto nuxt-link-active" target="_self">
                <img class="border border-warning rounded-circle" style="width:20vw;" src="@/assets/logo.png" alt="" srcset="">
              </a>
            </div>
            <div class="text-left col-md-4 col-sm-4 col-auto">
              <h5 class="bd-text-purple-bright mb-1">Documentation</h5>
              <ul class="list-unstyled ml-3">
                <li data-v-1b3cf462=""><a href="/" class="" target="_self">Home</a></li>
                <li data-v-1b3cf462=""><a href="/docs" class="" target="_self">Getting started</a></li>
                <li data-v-1b3cf462=""><a href="/docs/components" class="" target="_self">Components</a></li>
                <li data-v-1b3cf462=""><a href="/docs/directives" class="" target="_self">Directives</a></li>
                <li data-v-1b3cf462=""><a href="/docs/icons" class="" target="_self">Icons</a></li>
                <li data-v-1b3cf462=""><a href="/docs/reference" class="" target="_self">Reference</a></li>
                <li data-v-1b3cf462=""><a href="/play" class="" target="_self">Playground</a></li>
              </ul>
            </div>
            <div class="text-left col-auto  bg-dark">
              <h5 class="bd-text-purple-bright mb-1">Community</h5>
              <ul class="list-unstyled ml-3">
                <li data-v-1b3cf462=""><a href="https://github.com/bootstrap-vue/bootstrap-vue" target="_blank">GitHub</a></li>
                <li data-v-1b3cf462=""><a href="https://discord.gg/j2Mtcny" target="_blank">Discord chat</a></li>
                <li data-v-1b3cf462=""><a href="https://twitter.com/BootstrapVue" target="_blank">Twitter</a></li>
                <li data-v-1b3cf462=""><a href="https://opencollective.com/bootstrap-vue/" target="_blank">Open Collective</a></li>
              </ul> <h5 class="bd-text-purple-bright mb-1 mt-3">Release notes</h5>
              <ul class="list-unstyled ml-3">
                <li data-v-1b3cf462=""><a href="/docs/reference/changelog" class="" target="_self">Changelog</a></li>
              </ul>
            </div>
          </div>
          <hr class="bg-light">
          <p class="mb-2 text-center bg-dark">
            Designed and built with all the love in the world. Maintained by the
            <a href="https://github.com/orgs/bootstrap-vue/people" target="_blank">core team</a>
            with the help of
            <a href="https://github.com/bootstrap-vue/bootstrap-vue/graphs/contributors" target="_blank">our contributors</a>.
          </p>
          <p class=" text-center">Currently v2.15.0. Code licensed
            <a href="https://github.com/bootstrap-vue/bootstrap-vue/blob/master/LICENSE" target="_blank">MIT</a>.
              Docs generated with
            <a href="https://nuxtjs.org/" target="_blank">Nuxt.js</a>. <!---->
            页面底部粘贴自vue-bootstrap官方页面，感谢亲爱的bootstrap！
          </p> <!---->
        </div>
      </b-row>  
  </div>
</template>

<script lang="ts">
import { Component, Vue, Provide } from 'vue-property-decorator';
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
    @Provide() public reloads: (callback: () => void) => void = this.reload;
    public isRouterAlive: boolean = true;
    public username: string = window.sessionStorage.username;
    public reload(callback: () => void): void {
      this.isRouterAlive = false;
      this.$nextTick(function() {
        this.isRouterAlive = true;
        callback();
      });
    }
}
</script>

<style scoped lang="scss">
.container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.topbar{
    position:sticky;
    top: 5px;
    z-index: 5;
    &:hover{
      cursor: pointer;
      box-shadow: 1px 1px 1px wheat;
    }
}
</style>
