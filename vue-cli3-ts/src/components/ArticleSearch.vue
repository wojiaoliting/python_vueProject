<template>
  <div class="">
      <!-- <edit ref="editors" v-model="body" id="body-input"></edit> -->
    <div class="m-3 d-flex justify-content-between">
      <div>
        <b-button pill variant="outline-light" v-b-modal.modal-multi-1>
            <b-icon icon="search" aria-hidden="true" ></b-icon>
            查询文章
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
        <b-modal id="modal-multi-2" title="搜索结果" scrollable size="lg" ok-only>
          <article-table :inputtext="searchContent" idName="2"></article-table>
        </b-modal>
      </div>
      <b-button pill variant="outline-light" v-b-modal.modal-prevent-closing>
          <b-icon icon="plus" aria-hidden="true" ></b-icon>
          文章添加
      </b-button>
        <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="文章添加"
      size="lg"
      cancel-title="取消"
      ok-title="保存"
      no-enforce-focus
      @hidden="resetModal"
      @ok="handleOk"
    >
    <b-overlay variant="dark" :show="addLoadshow" rounded="sm">
      <b-form ref="form1">
        <b-form-group class="position-relative mb-4" label-cols="2" label-cols-lg="2" :state="titleState" label="标题名称" label-size="sm" label-for="title-input" :invalid-feedback="invaTitle" valid-feedback="">
          <!-- <template slot="prepend"> -->
          <b-form-input size='sm' id="title-input" v-model="title" :state="titleState" required trim max='50' autofocus placeholder="(必填￣ω￣=,不得超出50个字符)">
          </b-form-input>
          <div class="text-right position-absolute r-charNumber">
              {{title.length}}/50
          </div>
        </b-form-group>
      </b-form>
      <b-form ref="form3">
        <b-form-group label-cols="12" label-cols-lg="12" label-size="sm" :state="bodyState" label="内容" label-for="body-input" :invalid-feedback="invaBody" valid-feedback="">
                <!-- <b-form-input size="sm" id="body-input" v-model="body" :state="bodyState" required placeholder="(〃'▽'〃)内容不能为空哦">
                </b-form-input> -->
            <edit ref="editors" v-model="body" id="body-input"></edit>
        </b-form-group>
      </b-form>
      <b-row>
        <b-col>
            <b-form ref="form4">
                <b-form-group label-cols="4" label-cols-lg="4" label-size="sm" :state="fileState" label="标题图片" label-for="file-input" :invalid-feedback="invaFile" valid-feedback="">
                    <div class="uploads_elebox position-relative">
                        <b-img class="w-100" :src="coverImg"></b-img>
                        <b-form-file
                            class="position-absolute opacity0 w-100 h-100" 
                            id="file-input"
                            v-model="file"
                            :state="fileState"
                            placeholder=""
                            @change="fileChange"
                            accept="image/*"
                            drop-placeholder="Drop file here..."
                        ></b-form-file>
                    </div>
                    <b-badge variant="success">图片最佳比例为4 ：3</b-badge>
                </b-form-group>
            </b-form>
        </b-col>
        <b-col>
            <b-form ref="form2">
                <b-form-group class="position-relative mb-4" label-cols="2" label-cols-lg="2" label-size="sm" :state="summaryState" label="摘要" label-for="summary-input" :invalid-feedback="invaSummary" valid-feedback="">
                    <b-form-textarea size='sm' id="summary-input" max="200" v-model="summary" :state="summaryState" placeholder="(必填￣ω￣=,千万不要超过200个字符)" rows="7" required trim>
                    </b-form-textarea>
                    <div class="text-right position-absolute r-charNumber">
                        {{summary.length}}/200
                    </div>
                </b-form-group>
            </b-form>
        </b-col>
      </b-row>
    </b-overlay>
    </b-modal>
    </div>
  </div>
</template>

<script lang="ts">

import { Component, Prop, Vue , Inject } from 'vue-property-decorator';
import axios from 'axios';
import ArticleTable from '@/components/ArticleTable.vue';
import Edit from '@/components/Edit.vue';

import { Action, State, namespace, Mutation } from 'vuex-class';
interface Article {
          title: string;
          summary: string;
          body: string;
          title_icon: any;
          user: string;
        }
@Component({
  components: {
    ArticleTable,
    Edit,
  },
})
export default class ArticleSearch extends Vue {
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
    public title: string = '';
    public titleState: any = null;
    public summary: string = '';
    public summaryState: any = null;
    public coverImg: any = require('../assets/cover.jpg');
    public body: string = '';
    public bodyState: any = null;
    public file: any = null;
    public fileState: any = null;
    public submittedNames: any[] = [];
    public invaTitle: string = '';
    public invaSummary: string = '';
    public invaBody: string = '';
    public invaFile: string = '';
    public search: string = '';
    public searchContent: string = '';
    public addLoadshow: boolean = false;
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
            h('strong', '恭喜你！'),
            ` ${msg} `,
            h('b-spinner', { props: { type: 'grow', small: true } }),
          ],
        );
        // Create the title
        const vNodesTitle = h(
          'div',
          { class: ['d-flex', 'flex-grow-1', 'align-items-baseline', 'mr-2'] },
          [
            h('strong', { class: 'mr-2' }, '提示'),
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
        let valid1: boolean = false;
        let valid2: boolean = false;
        let valid3: boolean = false;
        let valid4: boolean = false;
        if (this.title.length <= 0) {
            this.titleState = false;
            this.invaTitle = '标题不能为空！';
        } else if (this.title.length > 50) {
            this.titleState = false;
            this.invaTitle = '标题字符超过了50个字符';
        } else {
            this.titleState = true;
            valid1 = true;
        }

        if (this.summary.length <= 0) {
            this.summaryState = false;
            this.invaSummary = '摘要不能为空！';
        } else if (this.summary.length > 200) {
            this.summaryState = false;
            this.invaSummary = '摘要的字符超过了200个字符';
        } else {
            this.summaryState = true;
            valid2 = true;
        }

        if (this.body.length <= 0) {
            this.bodyState = false;
            this.invaBody = '内容不能为空！';
        } else {
            this.bodyState = true;
            valid3 = true;
        }
        if (!this.file) {
            this.fileState = false;
            this.invaFile = '图片不能为空！';
        } else {
            this.fileState = true;
            valid4 = true;
        }
        this.fileState = valid4;
        return valid1 && valid2 && valid3 && valid4;
    }
    public fileChange(e: any): void {
        const ready: FileReader = new FileReader();
        ready.readAsDataURL(e.target.files[0]);
        ready.onload = () => {
            this.coverImg = ready.result;
        };
    }
    public resetModal(): void {
        this.title = '';
        this.titleState = null;
        this.summary = '';
        this.summaryState = null;
        this.body = '';
        this.bodyState = null;
        this.file = null;
        this.coverImg = require('../assets/cover.jpg');
        this.fileState = null;
        this.search = '';
        this.searchContent = '';
        // (this as any).$refs.editors.clear();
    }
    public handleOk(bvModalEvt: any): void {
        // Prevent modal from closing
        bvModalEvt.preventDefault();
        // Trigger submit handler
        this.handleSubmit();
    }
    public handleSubmit(): void {
        if (this.addLoadshow) {
          return;
        }
        // Exit when the form isn't valid
        if (!this.checkFormValidity()) {
            return;
        }
        this.addLoadshow = true;
        const postData: FormData = new FormData();
        postData.append('title', this.title);
        postData.append('summary', this.summary);
        postData.append('body', this.body);
        postData.append('title_icon', this.file);
        postData.append('user', window.sessionStorage.Id);
        axios.post('/article/', postData).then((res) => {
          // console.log(res);
          // 等待dom渲染后执行的方法
          this.$nextTick(() => {
            this.$bvModal.hide('modal-prevent-closing');
            this.reload(() => {
              this.popToast('文章添加成功', 'success');
            });
          });
        }, (erro) => {
          this.popToast('文章添加失败!请稍后再试', 'info');
          console.log(erro);
        }).then(() => {
          this.addLoadshow = false;
        });
    }
}
</script>

<style scoped lang="scss">
.uploads_elebox{
    overflow: hidden;
    background: darkkhaki;
    width: 200px;
    height:150px;
}
.opacity0 {
    vertical-align: top;
    opacity: 0;
    left: 0;
    top: 0;
    height: 100%;
}
.r-charNumber{
    right:0; 
}
.imgWidth{
    width: 70%;
}

</style>
