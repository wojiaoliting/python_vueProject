<template>
  <div>
      <editor v-model="myValue" :init="init" :disabled="disabled" @onClick="onClick"></editor>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
import tinymce from 'tinymce/tinymce';
import Editor from '@tinymce/tinymce-vue';
import 'tinymce/icons/default/icons.min.js';
import 'tinymce/themes/silver/theme';
import 'tinymce/plugins/advlist';
import 'tinymce/plugins/anchor';
import 'tinymce/plugins/autolink';
import 'tinymce/plugins/autoresize';
import 'tinymce/plugins/autosave';
import 'tinymce/plugins/bbcode';
import 'tinymce/plugins/contextmenu';
import 'tinymce/plugins/charmap';
import 'tinymce/plugins/code';
import 'tinymce/plugins/codesample';
import 'tinymce/plugins/colorpicker';
import 'tinymce/plugins/directionality';
import 'tinymce/plugins/emoticons';
import 'tinymce/plugins/fullpage';
import 'tinymce/plugins/fullscreen';
import 'tinymce/plugins/help';
import 'tinymce/plugins/hr';
import 'tinymce/plugins/image';
import 'tinymce/plugins/imagetools';
import 'tinymce/plugins/importcss';
import 'tinymce/plugins/insertdatetime';
import 'tinymce/plugins/legacyoutput';
import 'tinymce/plugins/link';
import 'tinymce/plugins/lists';
import 'tinymce/plugins/media';
import 'tinymce/plugins/nonbreaking';
import 'tinymce/plugins/noneditable';
import 'tinymce/plugins/pagebreak';
import 'tinymce/plugins/paste';
import 'tinymce/plugins/preview';
import 'tinymce/plugins/print';
import 'tinymce/plugins/quickbars';
import 'tinymce/plugins/save';
import 'tinymce/plugins/tabfocus';
import 'tinymce/plugins/table';
import 'tinymce/plugins/template';
import 'tinymce/plugins/textcolor';
import 'tinymce/plugins/textpattern';
import 'tinymce/plugins/toc';
import 'tinymce/plugins/visualblocks';
import 'tinymce/plugins/visualchars';
import 'tinymce/plugins/wordcount';

@Component({
    components: {
        Editor,
    },
})
export default class Edit extends Vue {
  @Prop({type: String, default: ''}) public value!: string ;
  @Prop({type: Boolean, default: false}) public disabled!: boolean;
  @Prop({type: [String, Array], default: 'print preview autolink directionality visualblocks visualchars fullscreen image link media template code codesample table hr pagebreak nonbreaking anchor insertdatetime advlist lists wordcount imagetools textpattern help emoticons autosave  autoresize'}) public plugins!: [] | string;
  @Prop({type: [String, Array], default: 'code codesample undo redo restoredraft | cut copy pastetext | forecolor backcolor bold italic underline strikethrough link anchor | alignleft aligncenter alignright alignjustify outdent indent | \
                     styleselect formatselect fontselect fontsizeselect | bullist numlist | blockquote subscript superscript removeformat | \
                     table image media charmap emoticons hr pagebreak insertdatetime print preview | fullscreen | bdmap indent2em lineheight formatpainter axupimgs'}) public toolbar!: [] | string;
  public init: any = {
      selector: 'textarea',
      valid_elements: '*[*]',
      content_style: `
        body{
          background-color:#fff;
        }
        pre{
          overflow-x:auto;
        }
        p,code,span,tspan{
          font-size:14px;
        }
        img{
          max-width:100%;
        }
        *{
          font-size:0;
        }
      `,
      placeholder: '请输入文章主体内容',
      language_url: '/tinymce/langs/zh_CN.js', // 语言包的路径
      language: 'zh_CN', // 语言
      skin_url: '/tinymce/skins/ui/oxide-dark', // skin路径
      powerpaste_word_import: 'merge', // 是否保留word粘贴样式'clean'|'merge'
      emoticons_database_url: '/tinymce/plugins/emoticons/js/emojis.js',
      // image_advtab: true,
      height: 500, // 编辑器高度
      max_height: 500,
      plugins: this.plugins,
      toolbar: this.toolbar,
      image_uploadtab: true,
      fontsize_formats: '12px 14px 16px 18px 24px 36px 48px 56px 72px',
      font_formats: '微软雅黑=Microsoft YaHei,Helvetica Neue,PingFang SC,sans-serif;苹果苹方=PingFang SC,Microsoft YaHei,sans-serif;宋体=simsun,serif;仿宋体=FangSong,serif;黑体=SimHei,sans-serif;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats;知乎配置=BlinkMacSystemFont, Helvetica Neue, PingFang SC, Microsoft YaHei, Source Han Sans SC, Noto Sans CJK SC, WenQuanYi Micro Hei, sans-serif;小米配置=Helvetica Neue,Helvetica,Arial,Microsoft Yahei,Hiragino Sans GB,Heiti SC,WenQuanYi Micro Hei,sans-serif',
      branding: false, // 是否禁用“Powered by TinyMCE”
      menubar: true, // 顶部菜单栏显示
      toolbar_mode : 'wrap',
      end_container_on_empty_block: true, // enter键 分块
      images_upload_handler: (blobInfo: any, success: any, failure: any) => {
          const img = 'data:image/jpeg;base64,' + blobInfo.base64();
          success(img);
      },
      // paste_enable_default_filters: false,
      // paste_filter_drop: false,
      // paste_webkit_styles: 'all',
      // paste_preprocess : (plugin: any, args: any) => {
      //   console.log(args);
      //   // args.node.setAttribute('id', 'hello');
      // },
      // paste_postprocess : (plugin: any, args: any) => {
        // function getBase64Image(img: any) { // 用canvas 生成base64图片
        //         const canvas: any = document.createElement('canvas');
        //         canvas.width = img.width;
        //         canvas.height = img.height;
        //         const ctx = canvas.getContext('2d');
        //         ctx.drawImage(img, 0, 0, img.width, img.height);
        //         // var ext = img.src.substring(img.src.lastIndexOf(".")+1).toLowerCase();
        //         const dataURL = canvas.toDataURL('image/jpeg');
        //         return dataURL;
        // }
        // let count=0;
        // args.node.querySelectorAll('img').forEach((element: any, index: number) => {
        //     (function(e,i){
        //         const img: any = new Image();
        //         img.setAttribute('crossOrigin', 'Anonymous'); // 必须在开头
        //         img.src = e.src;
        //         img.onload = () => {
        //             e.src=getBase64Image(img)
        //             if (count === args.node.querySelectorAll('img').length - 1) {
        //               tinymce.activeEditor.setContent(args.node.innerHTML);
        //               console.log(tinymce.activeEditor.getContent());
        //             }
        //             count++;
        //         };
        //     })(element,index)
        // });
      // },
  };
  public myValue: string = this.value;
  public mounted(): void {
      tinymce.init({
        // plugin_preview_width: 375, // 预览宽度 plugin_preview_height: 668,
        // paste_data_images: true, // 设置为“true”将允许粘贴图像，而将其设置为“false”将不允许粘贴图像。
      });
  }
  public onClick(e: any): void {
      this.$emit('onClick', e, tinymce);
  }
  public clear(): void {
        this.myValue = '';
  }
  public preShow(): void {
    tinymce.activeEditor.execCommand('mcePreview');
  }
  @Watch('value')
  public onChangeValue(newValue: any): void {
    this.myValue = newValue;
  }
  @Watch('myValue')
  public onChangeMyValue(newValue: any): void {
    this.$emit('input', newValue);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
