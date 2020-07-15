<template>
  <div class="">
    <div class="m-3 d-flex justify-content-between">
      <div>
        <b-button pill variant="outline-light" v-b-modal.modal-multi-1>
            <b-icon icon="search" aria-hidden="true" ></b-icon>
            成员查询
        </b-button>

        <b-modal id="modal-multi-1" size="lg" title="查找范围" ok-only no-stacking>
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
            <b-input-group class="mb-3">
                <b-form-input></b-form-input>
                <b-input-group-append>
                <b-button text="Button" variant="success" v-b-modal.modal-multi-2>ヾ(✿ﾟ▽ﾟ)ノ搜一搜</b-button>
                </b-input-group-append>
            </b-input-group>
          </div>
        </b-modal>

        <b-modal id="modal-multi-2" title="Second Modal" ok-only>
          <p class="my-2">Second Modal</p>
          <b-button v-b-modal.modal-multi-3 size="sm">Open Third Modal</b-button>
        </b-modal>

        <b-modal id="modal-multi-3" size="sm" title="Third Modal" ok-only>
          <p class="my-1">Third Modal</p>
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
      <!-- <form>
  <div class="form-row">
    <div class="col-md-4 mb-3">
      <label for="validationServerUsername">Username</label>
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text" id="inputGroupPrepend3">@</span>
        </div>
        <input type="text" class="form-control is-invalid" id="validationServerUsername" aria-describedby="inputGroupPrepend3" required>
        <div class="invalid-feedback">
          Please choose a username.
        </div>
      </div>
    </div>
  </div>
  <button class="btn btn-primary" type="submit">Submit form</button>
</form> -->
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
import { Component, Prop, Vue ,Inject } from 'vue-property-decorator';
import axios from 'axios'
interface User {
          username: string ,
          password: string ,
          email: string ,
        };
@Component({
  components: {

  }
})
export default class UserSearch extends Vue {
//   @Prop() private msg!: string;
    @Inject('reloads') reload :any;
    $inject: string[] = ['reload'];
    public selected: any = null;
    public options: any[] = [
        { value: null, text: 'Please select an option' },
        { value: 'a', text: 'This is First option' },
        { value: 'b', text: 'Selected Option' },
        { value: { C: '3PO' }, text: 'This is an option with object value' },
        { value: 'd', text: 'This one is disabled', disabled: true },
    ];
    public username: string ='';
    public usernameState: any = null;
    public email: string ='';
    public emailState: any = null;
    public pass: string ='';
    public passState: any = null;
    public repass: string ='';
    public repassState: any = null;
    public submittedNames: any[] = [];
    public invaUsername: string = '';
    public invaEmail: string = '';
    public invaPass: string = '';
    public invaRepass: string = '';
    // get usernameState(){
    //     //computed name
    //     return this.username.length >1;
    // }
    // get emailState(){
    //     //computed name
    //     return this.email.length >1;
    // }
    // get passState(){
    //     //computed name
    //     return this.pass.length >= 8;
    // }
    // get repassState(){
    //     //computed name
    //     return this.repass.length >= 8;
    // }
    mounted() {
    }
    checkFormValidity() {
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
    resetModal() {
        this.username = ''
        this.usernameState = null
    }
    handleOk(bvModalEvt: any) {
        // Prevent modal from closing
        bvModalEvt.preventDefault()
        // Trigger submit handler
        this.handleSubmit()
    }
    handleSubmit() {
        // Exit when the form isn't valid
        if (!this.checkFormValidity()) {
            return
        }
        // Push the name to submitted names
        
        let postData: User = {
          username : this.username,
          password : this.pass,
          email : this.email,
        }
        axios.post('/admins/',postData).then((res) => {
          // 等待dom渲染后执行的方法
          this.$nextTick(() => {
            this.$bvModal.hide('modal-prevent-closing');
            this.reload();
          })
        }, (erro) => {

        })
        // Hide the modal manually
        
    }

}
</script>

<style scoped lang="scss">

</style>
