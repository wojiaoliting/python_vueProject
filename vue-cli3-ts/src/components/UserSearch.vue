<template>
  <div class="">
    <div class="m-3 d-flex justify-content-between">
      <div>
        <b-button pill variant="outline-light" v-b-modal.modal-multi-1>
            <b-icon icon="search" aria-hidden="true" ></b-icon>
            成员查询
        </b-button>
        <b-modal id="modal-multi-1" size="lg" title="查找范围" ok-only @hidden="resetModal">
          <div class="my-1">
            <b-form  class="mb-4" inline>
                <b-form-checkbox class="mb-2 mr-sm-2 mb-sm-0">用户名</b-form-checkbox>
                <b-form-checkbox class="mb-2 mr-sm-2 mb-sm-0">邮箱名</b-form-checkbox>
                <b-form-checkbox class="mb-2 mr-sm-2 mb-sm-0">手机号</b-form-checkbox>
                <label class="mr-sm-2" for="inline-form-custom-select-pref">性别</label>
                <b-form-select
                id="inline-form-custom-select-pref"
                class="mb-2 mr-sm-2 mb-sm-0"
                :options="['不限', '男', '女']"
                value="不限"
                size="sm"
                ></b-form-select>
            </b-form>
            <b-form  class="mb-4" inline>
                <label class="mr-sm-2" for="example-datepicker1">起始时间</label>
                <b-form-datepicker id="example-datepicker1" size='sm'></b-form-datepicker>
                <label class="mr-sm-2 ml-sm-4" for="example-datepicker2">结束时间</label>
                <b-form-datepicker id="example-datepicker2"  class="" size='sm'></b-form-datepicker>
            </b-form>  
          </div>
          <template v-slot:modal-footer>
              <b-input-group class="mb-3">
                <b-form-input v-model="search" @keydown.enter="getSearch"></b-form-input>
                <b-input-group-append>
                <b-button text="Button"  @click="getSearch" variant="success">ヾ(✿ﾟ▽ﾟ)ノ搜一搜</b-button>
                </b-input-group-append>
              </b-input-group>
          </template>
        </b-modal>
        <b-modal id="modal-multi-2" title="搜索结果" size="lg" ok-only>
          <user-table :inputtext="searchContent" idName="2"></user-table>
        </b-modal>
      </div>

      <b-button pill variant="outline-light" v-b-modal.modal-prevent-closing>
          <b-icon icon="person-plus" aria-hidden="true" ></b-icon>
          成员添加
      </b-button>
        <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="管理员账号添加"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <b-form ref="form1">
        <b-form-group label-cols="3" label-cols-lg="2" :state="usernameState" label="用户名" label-size="sm" label-for="name-input" :invalid-feedback="invaUsername" valid-feedback="">
          <!-- <template slot="prepend"> -->
          <b-form-input size='sm' id="name-input" v-model="username" :state="usernameState" required trim autofocus placeholder="(必填￣ω￣=)">
          </b-form-input>
        </b-form-group>
      </b-form>
      <b-form ref="form2">
        <b-form-group label-cols="3" label-cols-lg="2" label-size="sm" :state="emailState" label="邮箱名" label-for="email-input" :invalid-feedback="invaEmail" valid-feedback="">
          <b-form-input size='sm' id="email-input" v-model="email" :state="emailState" placeholder="请输入正确的邮箱名（づ￣3￣）づ╭❤～" required trim type="email">
          </b-form-input>
        </b-form-group>
      </b-form>
      <b-form ref="form3">
        <b-form-group label-cols="3" label-cols-lg="2" label-size="sm" :state="passState" label="密码" label-for="pass-input" :invalid-feedback="invaPass" valid-feedback="">
          <b-form-input size="sm" id="pass-input" v-model="pass" :state="passState" required placeholder="(〃'▽'〃)密码不得少于8位哦" type="password" min="8">
          </b-form-input>
        </b-form-group>
      </b-form>
      <b-form ref="form4">
        <b-form-group label-cols="3" label-cols-lg="2" label-size="sm" :state="repassState" label="确认密码" label-for="repass-input" :invalid-feedback="invaRepass" valid-feedback="">
          <b-form-input size="sm" id="repass-input" v-model="repass" :state="repassState" placeholder="两次密码输入需要一致(灬°ω°灬) " required type="password">
          </b-form-input>
        </b-form-group>
      </b-form>
    </b-modal>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue , Inject } from 'vue-property-decorator';
import axios from 'axios';
import UserTable from '@/components/UserTable.vue';
import { Action, State, namespace, Mutation } from 'vuex-class';
interface User {
          username: string;
          password: string;
          email: string;
        }
@Component({
  components: {
    UserTable,
  },
})
export default class UserSearch extends Vue {
//   @Prop() private msg!: string;
    @Inject('reloads') public reload: any;
    public selected: any = null;
    public options: any[] = [
        { value: null, text: 'Please select an option' },
        { value: 'a', text: 'This is First option' },
        { value: 'b', text: 'Selected Option' },
        { value: { C: '3PO' }, text: 'This is an option with object value' },
        { value: 'd', text: 'This one is disabled', disabled: true },
    ];
    public username: string = '';
    public usernameState: any = null;
    public email: string = '';
    public emailState: any = null;
    public pass: string = '';
    public passState: any = null;
    public repass: string = '';
    public repassState: any = null;
    public submittedNames: any[] = [];
    public invaUsername: string = '';
    public invaEmail: string = '';
    public invaPass: string = '';
    public invaRepass: string = '';
    public search: string = '';
    public searchContent: string = '';
    public getSearch(): void {
        this.$bvModal.show('modal-multi-2');
        this.searchContent = this.search;
    }
    public popToast(msg: string, typeStatu: string): void {
        // Use a shorter name for this.$createElement
        const h = this.$createElement;
        // Increment the toast count
        // Create the message
        const vNodesMsg = h(
          'p',
          { class: ['text-center', 'mb-0'] },
          [
            h('b-spinner', { props: { type: 'grow', small: true } }),
            ' Flashy ',
            h('strong', 'toast'),
            ` ${msg} `,
            h('b-spinner', { props: { type: 'grow', small: true } }),
          ],
        );
        // Create the title
        const vNodesTitle = h(
          'div',
          { class: ['d-flex', 'flex-grow-1', 'align-items-baseline', 'mr-2'] },
          [
            h('strong', { class: 'mr-2' }, 'The Title'),
            h('small', { class: 'ml-auto text-italics' }, '5 minutes ago'),
          ],
        );
        // Pass the VNodes as an array for message and title
        this.$bvToast.toast([vNodesMsg], {
          title: [vNodesTitle],
          solid: true,
          variant: typeStatu,
        });
    }
    public checkFormValidity(): boolean {
        const valid1 = (this as any).$refs.form1.checkValidity();
        const valid2 = (this as any).$refs.form2.checkValidity();
        const valid3 = (this as any).$refs.form3.checkValidity();
        let valid4 = (this as any).$refs.form4.checkValidity();
        this.usernameState = valid1;
        if (!valid1) {
          if (this.username.length <= 0) {
              this.invaUsername = '用户名不能为空！';
          }
        }
        this.emailState = valid2;
        if (!valid2) {
          if (this.email.length <= 0) {
              this.invaEmail = '邮箱不能为空！';
          } else {
              this.invaEmail = '邮箱格式不正确！';
          }
        }
        this.passState = valid3;
        if (!valid3) {
          if (this.pass.length < 8 && this.pass.length <= 0) {
              this.invaPass = '密码必须是8个字符以上';
          }
        }
        if (this.pass === this.repass && this.repass.length > 0) {
          valid4 = true ;
        } else {
          valid4 = false ;
          this.invaRepass = '密码不一致！';
        }
        this.repassState = valid4;
        return valid1 && valid2 && valid3 && valid4;
    }
    public resetModal(): void {
        this.username = '';
        this.usernameState = null;
        this.email = '';
        this.emailState = null;
        this.pass = '';
        this.passState = null;
        this.repass = '';
        this.repassState = null;
        this.search = '';
        this.searchContent = '';
    }
    public handleOk(bvModalEvt: any): void {
        // Prevent modal from closing
        bvModalEvt.preventDefault();
        // Trigger submit handler
        this.handleSubmit();
    }
    public handleSubmit(): void {
        // Exit when the form isn't valid
        if (!this.checkFormValidity()) {
            return;
        }
        // Push the name to submitted names
        const postData: User = {
          username : this.username,
          password : this.pass,
          email : this.email,
        };
        axios.post('/admins/', postData).then((res) => {
          // 等待dom渲染后执行的方法
          if (res.status === 201) {
            this.$nextTick(() => {
              this.$bvModal.hide('modal-prevent-closing');
              this.reload(() => {
                this.popToast('用户添加成功', 'success');
              });
            });
          }
        }, (erro) => {
          this.popToast('用户添加失败!用户名已经存在', 'info');
          console.log(erro);
        });
    }
}
</script>

<style scoped lang="scss">

</style>
