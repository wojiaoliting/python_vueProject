<template>
  <div>
    <b-table striped dark small head-variant="light" table-variant="dark" hover :items="items" class="text-light dash">
      <template v-slot:cell(操作)="data">
          <div>
            <b-button-group size="sm">
              <b-button variant="outline-success" @click="showUserProfile(data.value)">
                <b-icon icon="person-lines-fill"></b-icon> 详细信息
              </b-button>
              <b-button variant="outline-info" @click="editUserProfile(data.value)">
                <b-icon icon="file-earmark-text"></b-icon> 信息编辑
              </b-button>
              <b-button variant="outline-light" @click="delUserProfile(data.value)">
                <b-icon icon="trash2"></b-icon> 删除
              </b-button>
            </b-button-group>
          </div>

      </template>
    </b-table>
    <div class="mt-3 d-flex justify-content-end">
      <b-pagination @change="showUserList" v-model="currentPage" pills :total-rows="rows" :per-page="perPage"></b-pagination>
    </div>
    <div class="mb-3 d-flex justify-content-end">
      <b-badge pill variant="light">共{{pageNum}}页/共{{totle}}条记录</b-badge>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Watch, Vue } from 'vue-property-decorator';
import axios from 'axios';
import dayjs from 'dayjs';
import { Action, State, namespace, Mutation } from 'vuex-class';
const userStore = namespace('userStore');

@Component
export default class UserTable extends Vue {
  @userStore.State('pageSize') public perPage: any;
  @Prop(String) public inputtext !: string ;
  // @Prop() public small: boolean = false;
  public items: any[] = [];
  public totle: number = 0;
  public pageNum: number = 1;
  public currentPage: number = 1;
  public page: number = 1;
  get rows(): number {
        return this.totle;
  }
  public created(): void {
    console.log(this.inputtext);
    this.showUserList(1);
  }
  public showUserList(pageN: number = 1): void {
    const params: any = {
        page: pageN,
        search: this.inputtext,
    };
    axios.get('/admins/', { params }).then((res) => {
      if (res.status === 200) {
        const data = res.data.results;
        const item: any = [];
        data.forEach((val: any, index: any) => {
            const obj: any = {};
            obj['id'] = val['id'];
            obj['名称'] = val['username'];
            obj['邮箱地址'] = val['email'] ? val['email'] : '空';
            obj['最近登录'] = val['last_login'] ? dayjs(val['last_login']).format('	YYYY/M/D h:mm A') : '未登录过';
            if (!val['email'] && !val['last_login']) {
              obj['_rowVariant'] = 'danger';
            }
            obj['操作'] = '';
            item.push(obj);
        });
        this.totle = res.data.count;
        const nums = Math.ceil(res.data.count / this.perPage);
        this.pageNum = nums;
        this.items = item;
      }
    }, (erro) => {});
  }
  public showUserProfile(id: number): void {

  }
  public editUserProfile(id: number): void {

  }
  public delUserProfile(id: number): void {

  }
}
</script>

<style scoped lang="scss">

</style>
