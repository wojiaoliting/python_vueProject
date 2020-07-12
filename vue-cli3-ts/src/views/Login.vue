<template>
    <b-container class="d-flex justify-content-center align-items-cente">
        <div class="card margin-top shadow-lg opacity-bg text-white" style="width: 18rem;">
            <div class="card-body pt-5">
                <h5 class="card-title text-center">管理员登录</h5>
                <h6 class="card-subtitle mb-2 text-muted"></h6>
                <p class="card-text">
                    <form>
                        <div class="form-group">
                            <label for="exampleInputEmail1">
                                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-award" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M9.669.864L8 0 6.331.864l-1.858.282-.842 1.68-1.337 1.32L2.6 6l-.306 1.854 1.337 1.32.842 1.68 1.858.282L8 12l1.669-.864 1.858-.282.842-1.68 1.337-1.32L13.4 6l.306-1.854-1.337-1.32-.842-1.68L9.669.864zm1.196 1.193l-1.51-.229L8 1.126l-1.355.702-1.51.229-.684 1.365-1.086 1.072L3.614 6l-.25 1.506 1.087 1.072.684 1.365 1.51.229L8 10.874l1.356-.702 1.509-.229.684-1.365 1.086-1.072L12.387 6l.248-1.506-1.086-1.072-.684-1.365z"/>
                                    <path d="M4 11.794V16l4-1 4 1v-4.206l-2.018.306L8 13.126 6.018 12.1 4 11.794z"/>
                                </svg>
                                账号名
                            </label>
                            <input type="text" v-model="username" class="form-control" id="exampleInputText" name="username">
                            
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">
                                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-lock" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M11.5 8h-7a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1zm-7-1a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h7a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-7zm0-3a3.5 3.5 0 1 1 7 0v3h-1V4a2.5 2.5 0 0 0-5 0v3h-1V4z"/>
                                </svg>
                                密码
                            </label>
                            <input type="password" v-model="password" class="form-control" id="exampleInputPassword" name="password">
                        </div>
                        <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="exampleCheck1">
                            <label class="form-check-label" for="exampleCheck1">Check me out</label>
                        </div>
                        <small class="form-text text-danger d-inline-block mb-1 h-40">{{tips}}</small>
                        <small class="form-text text-white text-center mb-1 h-40" :class="loading.loadImg">
                            <b-icon icon="arrow-counterclockwise" animation="spin-reverse-pulse" font-scale="2"></b-icon>
                        </small>
                        <button type="button" @click="submit" class="d-block w-100 btn btn-light" :disabled="loading.btnClickStuta">登录</button>
                    </form>
                </p>
                <a href="#" class="card-link text-white" style="font-size:14px;">欢迎登录后台管理系统</a>
            </div>
        </div>
    </b-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import axios from 'axios';
interface Lode {
        btnClickStuta: boolean;
        loadImg: string;
}
@Component({
  components: {},
})
export default class Login extends Vue {
    private tips: string = '';
    private username: string = '';
    private password: string = '';
    private loading: Lode = {
        btnClickStuta: false,
        loadImg: 'd-none',
    };
    public mounted(): void {
        console.log(this.$route);
    }
    private submit(): void {
        const correvtTips: string[] = ['用户名或密码为空', '用户名或密码错误，请重试'];
        if (this.username.length <= 0 || this.password.length <= 0) {
            this.tips = correvtTips[0];
        } else {
            this.loading.btnClickStuta = true;
            this.loading.loadImg = 'd-block';
            this.tips = '';
            const postData = {
                username: this.username,
                password: this.password,
            };
            axios.post('login/', postData).then((res) => {
                this.$router.replace({
                    path: '/',
                });
            }, (err) => {
                console.log('请求失败！');
                this.tips = correvtTips[1];
                this.loading.btnClickStuta = false;
                this.loading.loadImg = 'd-none';
            });
        }
    }
}
</script>

<style lang="scss">
.container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  .margin-top{
      margin-top:10rem ;
  }
  .opacity-bg{
      background-color:rgba(0,0,0,.5 );
      
  } 
}
</style>
