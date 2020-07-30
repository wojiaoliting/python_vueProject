<template>
  <div>
    <b-breadcrumb class="mt-2 bg-light white">
      <b-breadcrumb-item href="#home" class="text-pink">
        <b-icon icon="person-fill"  scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
        首页
      </b-breadcrumb-item>
      <b-breadcrumb-item href="#foo" active>文章列表</b-breadcrumb-item>  
    </b-breadcrumb>
    <article-search></article-search>
    <article-table small="false" idName="1"></article-table>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import ArticleSearch from '@/components/ArticleSearch.vue';
import ArticleTable from '@/components/ArticleTable.vue';
import axios from 'axios';
import { Action, State, namespace, Mutation } from 'vuex-class';
const userStore = namespace('userStore');
@Component({
  components: {
    ArticleSearch,
    ArticleTable,
  },
})
export default class Article extends Vue {
  public items: any[] = [
    {
      text: '用户管理',
      href: '#',
    },
    {
      text: '用户列表',
      href: '#',
      active: true,
    },
  ];
  public title: string = '';
  public created(): void {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .text-pink a{
    color: #be2454;
  }
  .dash{
    border:2px dashed #c46d88;
  }
</style>
