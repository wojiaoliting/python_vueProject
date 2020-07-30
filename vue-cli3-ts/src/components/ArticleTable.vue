<template>
  <div>
    <b-table striped dark small head-variant="white" :fields="fields" table-variant="dark" hover :items="items" key="id" class="text-light dash">
      <template v-slot:cell(title_icon)="data">
            <b-img size="sm" :src="data.value" alt="封面图片" style="width:200px;height:150px"></b-img>
      </template>
      <template v-slot:cell(operation)="data">
          <div>
            <b-button-group size="sm">
              <b-button variant="outline-success" @click="showArticle(data.value)">
                <b-icon icon="person-lines-fill"></b-icon> 详细信息
              </b-button>
              <b-button variant="outline-light" @click="getDelUserId(data.value)">
                <b-icon icon="trash2"></b-icon> 删除
              </b-button>
            </b-button-group>
          </div>
      </template>
    </b-table>
    <div class="mt-3 d-flex justify-content-end">
      <b-pagination @change="showArticleList" v-model="currentPage" pills :total-rows="rows" :per-page="perPage"></b-pagination>
    </div>
    <div class="mb-3 d-flex justify-content-end">
      <b-badge pill variant="light">共{{pageNum}}页/共{{totle}}条记录</b-badge>
    </div>
    <b-modal :id="showModelId" size="lg" :body-bg-variant="editBtn?'white':'dark'" :body-text-variant="editBtn?'dark':'white'" title="文章编辑" no-enforce-focus @hidden="resetEdit">
          <b-overlay variant="dark" :show="editLoadshow" rounded="sm">
            <b-form ref="form1">
              <b-form-group class="position-relative mb-4" label-cols="2" label-cols-lg="2" :state="titleState" label="标题名称" label-size="sm" label-for="title-input" :invalid-feedback="invaTitle" valid-feedback="">
                <!-- <template slot="prepend"> -->
                <b-form-input size='sm' id="title-input" :disabled="editBtn" v-model="articleInfo.title" :state="titleState" required trim max='50' autofocus placeholder="(必填￣ω￣=,不得超出50个字符)">
                </b-form-input>
                <div class="text-right position-absolute r-charNumber">
                    {{articleInfo.title.length}}/50
                </div>
              </b-form-group>
            </b-form>
            <b-form ref="form3">
              <b-form-group label-cols="12" label-cols-lg="12" label-size="sm" :state="bodyState" label="内容" label-for="body-input" :invalid-feedback="invaBody" valid-feedback="">
                      <!-- <b-form-input size="sm" id="body-input" v-model="body" :state="bodyState" required placeholder="(〃'▽'〃)内容不能为空哦">
                      </b-form-input> -->
                  <edit ref="editore" v-model="articleInfo.body" :disabled="editBtn" id="body-input"></edit>
              </b-form-group>
            </b-form>
            <b-row>
              <b-col>
                  <b-form ref="form4">
                      <b-form-group label-cols="4" label-cols-lg="4" label-size="sm" :state="fileState" label="标题图片" label-for="file-input" :invalid-feedback="invaFile" valid-feedback="">
                          <div class="uploads_elebox position-relative">
                              <b-img class="w-100" :src="coverImg" alt="封面图片"></b-img>
                              <b-form-file
                                  class="position-absolute opacity0 w-100 h-100" 
                                  id="file-input"
                                  v-model="articleInfo.title_icon"
                                  :state="fileState"
                                  :disabled="editBtn"
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
                      <b-form-group class="position-relative mb-4" label-cols="3" label-cols-lg="2" label-size="sm" :state="summaryState" label="摘要" label-for="summary-input" :invalid-feedback="invaSummary" valid-feedback="">
                          <b-form-textarea size='sm' id="summary-input" :disabled="editBtn" max="200" v-model="articleInfo.summary" :state="summaryState" placeholder="(必填￣ω￣=,千万不要超过200个字符)" rows="7" required trim>
                          </b-form-textarea>
                          <div class="text-right position-absolute r-charNumber">
                              {{articleInfo.summary.length}}/200
                          </div>
                      </b-form-group>
                  </b-form>
              </b-col>
            </b-row>
          </b-overlay>
        <template v-slot:modal-footer>
              <b-button text="Button" @click="preArticle" variant="success">内容预览</b-button>
              <b-button text="Button" @click="editArticle" variant="success">{{editBtnText}}</b-button>
              <b-button text="Button" @click="$bvModal.hide(showModelId)" variant="dark">退出</b-button>
        </template>
    </b-modal>
    <b-modal :id="delModelId" okVariant="danger" cancelTitle="取消" okTitle="确定" size="sm" title="警告" @ok="delUserProfile">
          <p class="my-1">您确定要删除您辛苦写的文章吗(╯°Д°)╯？</p>
    </b-modal>
  </div>
</template>

<script lang="ts">
import Constants from '@/constants';
import { Component, Prop, Watch, Vue , Inject} from 'vue-property-decorator';
import axios from 'axios';
import dayjs from 'dayjs';
import Edit from '@/components/Edit.vue';
import { Action, State, namespace, Mutation } from 'vuex-class';
const userStore = namespace('userStore');
interface Article {
          id: string;
          title: string;
          summary: string;
          body: string;
          title_icon: any;
          user: string;
        }
@Component({
  components: {
    Edit,
  },
})
export default class ArticleTable extends Vue {
  @Inject('reloads') public reload: any;
  @userStore.State('pageSize') private perPage: any;
  @Prop(String) private inputtext !: string ;
  @Prop(String) private idName !: number ;
  // @Prop(String) private EditModelId !: string ;
  // @Prop(String) private delUserModelId !: string ;
  // @Prop() public small: boolean = false;
  private fields: any[] = [
    {
      key: 'id',
      label: '文章ID',
    },
    {
      key: 'title_icon',
      label: '封面',
    },
    {
      key: 'title',
      label: '文章标题',
    },
    {
      key: 'summary',
      label: '文章摘要',
    },
    {
      key: 'created',
      label: '发布时间',
      sortable: true,
    },
    {
      key: 'operation',
      label: '操作',
    },
  ];
  private showModelId = `modal-multi-show${this.idName}`;
  private editModelId = `modal-multi-edit${this.idName}`;
  private delModelId = `modal-multi-del${this.idName}`;
  private items: object[] = [];
  private articleInfo: Article = {
    id: '',
    title: '',
    summary: '',
    body: '',
    title_icon: null,
    user: '',
  };
  private editLoadshow: boolean = false;
  private editBtn: boolean = true;
  private editBtnText: string = '编辑(๑*◡*๑)';
  private coverImg: any = require('../assets/cover.jpg');
  private titleState: any = null;
  private summaryState: any = null;
  private bodyState: any = null;
  private fileState: any = null;
  private invaTitle: string = '';
  private invaSummary: string = '';
  private invaBody: string = '';
  private invaFile: string = '';
  private totle: number = 0;
  private pageNum: number = 1;
  private currentPage: number = 1;
  private page: number = 1;
  private delId: number | null = null;
  get rows(): number {
    return this.totle;
  }
  private created(): void {
    this.showArticleList(1);
  }
  private checkFormValidity(): boolean {
        let valid1: boolean = false;
        let valid2: boolean = false;
        let valid3: boolean = false;
        let valid4: boolean = false;
        if (this.articleInfo.title.length <= 0) {
            this.titleState = false;
            this.invaTitle = '标题不能为空！';
        } else if (this.articleInfo.title.length > 50) {
            this.titleState = false;
            this.invaTitle = '标题字符超过了50个字符';
        } else {
            this.titleState = true;
            valid1 = true;
        }

        if (this.articleInfo.summary.length <= 0) {
            this.summaryState = false;
            this.invaSummary = '摘要不能为空！';
        } else if (this.articleInfo.summary.length > 200) {
            this.summaryState = false;
            this.invaSummary = '摘要的字符超过了200个字符';
        } else {
            this.summaryState = true;
            valid2 = true;
        }

        if (this.articleInfo.body.length <= 0) {
            this.bodyState = false;
            this.invaBody = '内容不能为空！';
        } else {
            this.bodyState = true;
            valid3 = true;
        }
        // if (!this.articleInfo.title_icon) {
        //     this.fileState = false;
        //     this.invaFile = '图片不能为空！';
        // } else {
        //     this.fileState = true;
        //     valid4 = true;
        // }
        this.fileState = true;
        valid4 = true;
        this.fileState = valid4;
        return valid1 && valid2 && valid3 && valid4;
  }
  private fileChange(e: any): void {
        const ready: FileReader = new FileReader();
        ready.readAsDataURL(e.target.files[0]);
        ready.onload = () => {
            this.coverImg = ready.result;
        };
  }
  private showArticleList(pageN: number = 1): void {
    const params: any = {
        page: pageN,
        search: this.inputtext,
    };
    axios.get('/article/', { params }).then((res) => {
      if (res.status === 200) {
        const data = res.data.results;
        const item: any = [];
        data.forEach((val: any, index: number) => {
            const obj: any = {};
            obj['id'] = val['id'];
            obj['title_icon'] = val['title_icon'];
            obj['title'] = val['title'];
            obj['summary'] = val['summary'] ? val['summary'] : '空';
            obj['created'] = val['created'] ? dayjs(val['created']).format('	YYYY/M/D h:mm A') : '?';
            obj['operation'] = val['id'];
            item.push(obj);
        });
        this.totle = res.data.count;
        const nums = Math.ceil(res.data.count / this.perPage);
        this.pageNum = nums;
        this.items = item;
      }
    }, (erro) => {}).then(() => {
      this.editLoadshow = false;
    });
  }
  private showArticle(value: any): void {
    this.$bvModal.show(this.showModelId);
    axios.get(`/article/${value}/`).then((res: any) => {
      this.articleInfo.id = res.data.id;
      this.articleInfo.title = res.data.title;
      this.articleInfo.summary = res.data.summary;
      this.coverImg = res.data.title_icon;
      this.articleInfo.body = Constants.ChangeImgURLTorellView(res.data.body);
    }, (erro) => {
      this.$bvToast.toast('文章获取失败！强稍后再试！', {
              title: `提示`,
              toaster: 'b-toaster-top-center',
              solid: true,
              appendToast: false,
              variant: 'dark',
      });
    });
  }
  private resetEdit(): void {
    // 编辑用户信息属性
    this.articleInfo = {
      id: '',
      title: '',
      summary: '',
      body: '',
      title_icon: null,
      user: '',
    };
    this.titleState = null;
    this.summaryState = null;
    this.bodyState = null;
    this.fileState = null;
    this.invaTitle = '';
    this.invaSummary = '';
    this.invaBody = '';
    this.invaFile = '';
    this.coverImg = require('../assets/cover.jpg');
    this.editBtn = true;
    this.editBtnText = '编辑(๑*◡*๑)';
  }
  private editArticle(list: any, text: string, callback?: (isOk: boolean) => void): void {
    if (this.editLoadshow) {
      return;
    }
    if (this.editBtn) {
      this.editBtn = false;
      this.editBtnText = '保存(๑´ㅂ`๑) ';
    } else {
      if (!this.checkFormValidity()) {
            return;
      }
      this.editLoadshow = true;
      const postData: FormData = new FormData();
      postData.append('title', this.articleInfo.title);
      postData.append('summary', this.articleInfo.summary);
      postData.append('body', this.articleInfo.body);
      if (this.articleInfo.title_icon) {
          postData.append('title_icon', this.articleInfo.title_icon);
      }
      postData.append('user', window.sessionStorage.Id);
      axios.put(`/article/${this.articleInfo.id}/`, postData).then((res) => {
          const lists: object[] = this.items;
          for (let i = 0; i < this.items.length; i++) {
            if ((lists as any)[i].id === res.data.id) {
              (lists as any)[i].title_icon = res.data.title_icon;
              (lists as any)[i].title = res.data.title;
              (lists as any)[i].summary = res.data.summary;
              (lists as any)[i].created = res.data.created;
              break;
            }
          }
          this.items = lists;
          this.$bvToast.toast(`文章修改成功喽ヾ(๑╹◡╹)ﾉ"`, {
                title: `提示`,
                toaster: 'b-toaster-top-center',
                solid: true,
                appendToast: true,
                variant: 'success',
          });
          this.editBtn = true;
          this.editBtnText = '编辑(๑*◡*๑)';
        }, (erro) => {
            this.$bvToast.toast(`文章修改失败，请稍后再试吧~"`, {
                  title: `提示`,
                  toaster: 'b-toaster-top-center',
                  solid: true,
                  appendToast: false,
                  variant: 'dark',
            });
        }).then(() => {
            this.editLoadshow = false;
        });
    }
  }
  private getDelUserId(id: number): void {
    this.$bvModal.show(this.delModelId);
    this.delId = id;
  }
  private delUserProfile(): void {
    axios.delete(`/article/${this.delId}/`).then((res) => {
      this.$bvToast.toast(`文章删除成功喽ヾ(๑╹◡╹)ﾉ"`, {
            title: `提示`,
            toaster: 'b-toaster-top-center',
            solid: true,
            appendToast: true,
            variant: 'success',
      });
      if (this.delId) {
        let count = 0;
        const news: any[] = [];
        for (let index = 0 ; index < this.items.length; index++) {
          if ((this as any).items[index].id === this.delId) {
            continue;
          }
          news[ count++ ] = this.items[index];
        }
        this.items = news;
      }
    }, (erro) => {
      this.$bvToast.toast(`文章删除失败，请稍后再试吧~"`, {
              title: `提示`,
              toaster: 'b-toaster-top-center',
              solid: true,
              appendToast: false,
              variant: 'dark',
      });
    }).then(() => {
        this.$bvModal.hide(this.delModelId);
        this.delId = 0;
    });
  }
  private preArticle(): void {
    (this as any).$refs.editore.preShow();
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
