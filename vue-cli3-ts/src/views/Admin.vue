<template>
  <div>
    <b-breadcrumb class="mt-2 bg-light white">
      <b-breadcrumb-item href="#home" class="text-pink">
        <b-icon icon="person-fill"  scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
        首页
      </b-breadcrumb-item>
      <b-breadcrumb-item href="#foo" active>管理员列表</b-breadcrumb-item>  
    </b-breadcrumb>
    <user-search></user-search>
    <b-table hover :items="listItems" class="bg-white dash"></b-table>
    <div class="mt-3 d-flex justify-content-end">
      <b-pagination v-model="currentPage" pills :total-rows="rows"></b-pagination>
    </div>
    <div class="mb-3 d-flex justify-content-end">
      <b-badge pill variant="light">共{{pageNum}}页/共{{totle}}条记录</b-badge>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import UserSearch from '@/components/UserSearch.vue';
import axios from 'axios';
@Component({
  components: {
    UserSearch,
  }
})
export default class Admin extends Vue {
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
  public listItems: any[] = [];
  public totle: number = 0;
  public pageNum: number = 1;
  public currentPage: number = 1;
  public rows: number = 1;
  public page: number = 1;
  public title: string = '';
  public created(): void {
    const linkParam = {
      page: this.page,
      title: this.title,
    };
    axios.get('/admins/', {
      params: {
      page: this.page,
    },
    }).then((res) => {
      console.log(res);
      if (res.status === 200) {
        const data = res.data.results;
        const item: any = [];
        data.forEach((val: any, index: any) => {
          const obj: any = {};
          const id = 'id';
          const username = '管理员名称';
          const email = '邮箱地址';
          const lastLogin = '最近登录';
          const rowVariant = '_rowVariant';
          obj[id] = val[id];
          obj[username] = val['username'];
          obj[email] = val['email'] ? val['email'] : '空';
          obj[lastLogin] = val['last_login'] ? new Date (val['last_login']) : '未登录过';
          if (!val['email'] && !val['last_login']) {
            obj[rowVariant] = 'danger';
          }
          item.push(obj);
        });
        this.totle = res.data.count ;
        this.listItems = item;

      }
    }, (erro) => {
      console.log(erro);
    });
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
