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
    <b-modal :id="showModelId" size="lg" title="档案袋" ok-only @hidden="resetModal">
        <b-media right-align vertical-align="top">
          <template v-slot:aside>
            <b-img blank blank-color="#ccc" width="80" alt="placeholder"></b-img>
          </template>
          <h5 class="mt-0 mb-1">{{userinfo.username}}</h5>
          <p class="mb-0">
            <b-form @submit.stop.prevent>
                <b-row class="my-1">
                  <b-col sm="2">
                    <label for="input-default">昵称:</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input ref="nameFocus" required :disabled="editBtn" v-model="infoParam.nickname"  id="input-default" :placeholder="infoParam.nickname" :state="nicknameState"></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="my-1">
                  <b-col sm="2">
                    <label for="input-default">性别:</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-select :disabled="editBtn" v-model="infoParam.gender" class="mb-3" name="gender">
                      <!-- This slot appears above the options from 'options' prop -->
                      <template v-slot:first>
                        <b-form-select-option value="" disabled>未填写</b-form-select-option>
                      </template>

                      <!-- These options will appear after the ones from 'options' prop -->
                      <b-form-select-option value="male">男</b-form-select-option>
                      <b-form-select-option value="female">女</b-form-select-option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row class="my-1">
                  <b-col sm="2">
                    <label for="input-default">出生日期:</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input :disabled="editBtn" type="date" v-model="infoParam.birthday" id="input-default" :placeholder="userinfo.profile_of.birthday" name="birthday"></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="my-1">
                  <b-col sm="2">
                    <label for="input-default">手机号码:</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input type="tel" ref="mobileFocus" :state="mobileState"  :disabled="editBtn" id="input-default"  v-model="infoParam.mobile" :placeholder="infoParam.mobile" name="mobile"></b-form-input>
                  </b-col>
                </b-row>
            </b-form>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <div class="row">
                <div class="col col-2">
                  邮箱
                </div>
                <div class="col col-8">
                  {{userinfo.email}}
                </div>
                </div>
              </li>
              <li class="list-group-item">
                <div class="row">
                <div class="col col-2">
                  创建日期
                </div>
                <div class="col col-8">
                  {{ userinfo.profile_of.created}}
                </div>
                </div>
              </li>
              <li class="list-group-item">
                <div class="row">
                <div class="col col-2">
                  修改日期
                </div>
                <div class="col col-8">
                  {{userinfo.profile_of.updated}}
                </div>
                </div>
              </li>
            </ul>
          </p>
        </b-media>
        <template v-slot:modal-footer>
              <b-button text="Button"  @click="toEdit" variant="success">{{editBtnText}}</b-button>
        </template>
    </b-modal>
    <b-modal id="editIsOk" size="sm" title="提示" ok-only>
          <p class="my-1">编辑</p>
    </b-modal>
    <b-modal :id="delModelId" okVariant="danger" cancelTitle="取消" okTitle="确定" size="sm" title="警告" >
          <p class="my-1">您确定要删除这位管理员吗(╯°Д°)╯？</p>
    </b-modal>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Watch, Vue } from 'vue-property-decorator';
import axios from 'axios';
import dayjs from 'dayjs';
import { Action, State, namespace, Mutation } from 'vuex-class';
const userStore = namespace('userStore');
interface ProfileOf {
  nickname: string;
  gender: string;
  birthday: string;
  mobile: string;
  created: string;
  updated: string;
}
interface UserInfo {
  username: string;
  email: string;
  profile_of: ProfileOf;
}
@Component
export default class UserTable extends Vue {
  @userStore.State('pageSize') private perPage: any;
  @Prop(String) private inputtext !: string ;
  @Prop(String) private idName !: number ;
  // @Prop(String) private EditModelId !: string ;
  // @Prop(String) private delUserModelId !: string ;
  // @Prop() public small: boolean = false;
  private showModelId = `modal-multi-show${this.idName}`;
  private editModelId = `modal-multi-edit${this.idName}`;
  private delModelId = `modal-multi-del${this.idName}`;
  private items: any[] = [];
  private nicknameState: any = null;
  private mobileState: any = null;
  private userinfo: UserInfo = {
    username: '',
    email: '',
    profile_of: {
      nickname: '',
      gender: '',
      birthday: '',
      mobile: '',
      created: '',
      updated: '',
    },
  };
  private infoParam: any = {
    nickname : '',
    birthday : '',
    gender : '',
    mobile : '',
    user : '',
  };
  private editBtn: boolean = true;
  private editBtnText: string = '编辑(๑*◡*๑)';
  private hasInfo: boolean = false;
  private totle: number = 0;
  private pageNum: number = 1;
  private currentPage: number = 1;
  private page: number = 1;
  get rows(): number {
    return this.totle;
  }
  private created(): void {
    this.showUserList(1);
  }
  private showUserList(pageN: number = 1): void {
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
            obj['操作'] = val['id'];
            item.push(obj);
        });
        this.totle = res.data.count;
        const nums = Math.ceil(res.data.count / this.perPage);
        this.pageNum = nums;
        this.items = item;
      }
    }, (erro) => {});
  }
  private showUserProfile(id: number): void {
    this.$bvModal.show(this.showModelId);
    axios.get(`/admins/${id}/`).then((res) => {
      if (res.status === 200) {
        this.hasInfo = res.data.profile_of ? true : false;
        const info: any = res.data;
        this.infoParam.user = info.id;
        this.infoParam.id = info.profile_of ? info.profile_of.id : '';
        info.profile_of = info.profile_of ? info.profile_of : {};
        this.infoParam.nickname = info.profile_of.nickname ? info.profile_of.nickname : '';
        this.infoParam.gender = info.profile_of.gender ? info.profile_of.gender : '';
        info.profile_of.gender = info.profile_of.gender ? (info.profile_of.gender === 'male' ? '男' : '女') : '';
        this.infoParam.birthday = info.profile_of.birthday ? info.profile_of.birthday : '';
        this.infoParam.mobile = info.profile_of.mobile ? info.profile_of.mobile : '';
        info.profile_of.created = dayjs(info.profile_of.created).format('YYYY/M/D h:mm A');
        info.profile_of.updated = dayjs(info.profile_of.updated).format('YYYY/M/D h:mm A');
        this.userinfo = info;
        // this.hasInfo = this.infoParam;
      }
    }, (erro) => {});
  }
  private toEdit(): void {
    const list: any= {};
    for (const key in this.infoParam) {
      if (key === "gender" || key === "birthday") {
        if (this.infoParam[key] !== '') {
          list[key] = this.infoParam[key];
        }
      } else {
        list[key] = this.infoParam[key];
      }
    }
    if (this.editBtn) {
      this.editBtn = false;
      this.editBtnText = '保存(๑´ㅂ`๑) ';
      this.$nextTick(() => {
          this.$nextTick(() => {
            (this as any).$refs['nameFocus'].focus();
          });
      });
    } else {
      const valid1 = (this as any).$refs['nameFocus'].checkValidity();
      const valid2 = /^[1][3,4,5,7,8][0-9]{9}$/.test(this.infoParam.mobile);
      if (valid1) {
        this.nicknameState = true;
        if (this.infoParam.mobile !== '') {
          if (valid2) {
            this.mobileState = true;
            if (this.hasInfo) {
              this.editPutUserProfile(list);
            } else {
              this.editPostUserProfile(list);
            }
          } else {
            this.mobileState = false;
          }
        } else {
            if (this.hasInfo) {
              this.editPutUserProfile(list);
            } else {
              this.editPostUserProfile(list);
            }
        }
      } else {
        this.nicknameState = false;
        if (this.infoParam.mobile !== '') {
          if (valid2) {
            this.mobileState = true;
          } else {
            this.mobileState = false;
          }
        }
      }
    }
  }
  private resetEdit(): void{
    this.nicknameState = null;
    this.mobileState = null;
    this.editBtn = true;
    this.editBtnText ='编辑(๑*◡*๑)';
  }
  private resetModal(): void {
    this.hasInfo = false;
    const list = this.infoParam;
    for (const key in list) {
      list[key] = '';
    }
    this.infoParam = list;
    this.resetEdit();
  }
  private editPostUserProfile(list: any): void {
    axios.post(`/profile/`, list).then((res) => {
      console.log(res);
      this.infoParam.id = res.data.id;
      this.$bvToast.toast(`用户档案修改成功喽ヾ(๑╹◡╹)ﾉ"`, {
            title: `提示`,
            toaster: 'b-toaster-top-center',
            solid: true,
            appendToast: false,
            variant: 'success',
        });
        this.resetEdit();
        this.hasInfo = true;
      }, (erro) => {
        this.$bvToast.toast(`用户档案修改失败，请稍后再试吧~"`, {
            title: `提示`,
            toaster: 'b-toaster-top-center',
            solid: true,
            appendToast: false,
            variant: 'dark',
        });
      });
  }
  private editPutUserProfile(list: any): void {
    axios.put(`/profile/${this.infoParam.id}/`, list).then((res) => {
        this.$bvToast.toast(`用户档案修改成功喽ヾ(๑╹◡╹)ﾉ"`, {
              title: `提示`,
              toaster: 'b-toaster-top-center',
              solid: true,
              appendToast: true,
              variant: 'success',
            });
            this.resetEdit();
    }, (erro) => {
          this.$bvToast.toast(`用户档案修改失败，请稍后再试吧~"`, {
              title: `提示`,
              toaster: 'b-toaster-top-center',
              solid: true,
              appendToast: false,
              variant: 'dark',
        });
    });
  }
  private delUserProfile(id: number): void {
    this.$bvModal.show(this.delModelId);
  }
}
</script>

<style scoped lang="scss">

</style>
