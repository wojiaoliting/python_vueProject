<template>
  <div>
    <b-breadcrumb class="mt-2">
      <b-breadcrumb-item href="#home">
        <b-icon icon="person-fill" scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
        管理员
      </b-breadcrumb-item>
      <b-breadcrumb-item href="#foo" active>管理员列表</b-breadcrumb-item>  
    </b-breadcrumb>
    <div>
      <b-table hover :items="listItems" class="bg-white"></b-table>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios';
@Component({})
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
  public listItems: any[] = [
    { age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
    { age: 21, first_name: 'Larsen', last_name: 'Shaw'},
    {
      age: 89,
      first_name: 'Geneva',
      last_name: 'Wilson',
      _rowVariant: 'danger',
    },
    {
      age: 40,
      first_name: 'Thor',
      last_name: 'MacDonald',
      _cellVariants: { age: 'info', first_name: 'warning'},
    },
    { age: 29, first_name: 'Dick', last_name: 'Dunlap'},
  ];
  public mounted(): void {
    axios.get('/users/').then((res) => {
      console.log(res);
      if (res.status === 200) {
        const data = res.data.results;
        const item: any= [];
        data.forEach((val: any, index: any) => {
          const obj: any = {};
          const id = 'id';
          const username = '管理员名称';
          const email = '邮箱地址';
          const lastLogin = '最近登录';
          const _rowVariant = '_rowVariant';
          obj[id] = val[id];
          obj[username] = val['username'];
          obj[email] = val['email'] ? val['email'] : '空';
          obj[lastLogin] = val['last_login'] ? new Date (val['last_login']) : '未登录过';
          if (!val['email'] && !val['last_login']) {
            obj[_rowVariant] = 'danger';
          }
          item.push(obj);
        });
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

</style>
