<template>
    <b-container fluid>
      <top-nav msg="❤ »» 后台管理系统" userName="李心" class="m-3"></top-nav>
      <b-row>
        <b-col class="bg-white pl-3" cols="2">
          <left-nav listName="用户管理"></left-nav>
        </b-col>
        <b-col class="bg-dark pr-3" cols="10">2 of 3</b-col>
      </b-row>
      <b-row class="footer">
          
      </b-row>
    </b-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TopNav from '@/components/TopNav.vue';
import LeftNav from '@/components/LeftNav.vue';

@Component({
  components: {
    TopNav,
    LeftNav,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
.container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
