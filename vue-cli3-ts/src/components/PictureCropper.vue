<template>
    <form id="avatarForm">
        <div class="avatar-body">
            <div class="row">
                <div class="col-md-9">
                    <div class="avatar-wrapper">
                        <vueCropper
                            ref="cropper"
                            :img="option.img"
                            :autoCropWidth="option.autoCropWidth"
                            :aytoCropHeight="option.autoCropHeight"
                            :outputSize="option.size"
                            :outputType="option.outputType"
                            :info="true"
                            :full="option.full"
                            :canMove="option.canMove"
                            :canMoveBox="option.canMoveBox"
                            :original="option.original"
                            :autoCrop="option.autoCrop"
                            :fixed="option.fixed"
                            :fixedNumber="option.fixedNumber"
                            :centerBox="option.centerBox"
                            :infoTrue="option.infoTrue"
                            :fixedBox="option.fixedBox"
                            @realTime="preLook"
                        ></vueCropper>
                    </div>
                </div>
                <div class="col-md-3">
                    小图预览
                    <div class="ml-4 avatar-preview preview-md">
                        <b-img :src="preImg" title="头像预览" alt="头像预览"></b-img>
                    </div>
                    <div class="mt-5 upload_elebox btn btn-success btn-block position-relative">
                        添加本地图片
                        <input class="position-absolute" type="file" id="upload_ele" multiple="false" accept="image/*" @change="fileChange" />
                    </div>
                </div>
            </div>
        </div>
    </form>
</template>

<script lang="ts">
    import {Component, Vue, Emit} from 'vue-property-decorator';
    import axios from 'axios';
    import { CreateElement } from 'vue';

    @Component({})
    export default class PictureCropper extends Vue {
        private active: boolean = false;
        private pictureDataUri: string = '';
        private imageWidth: number = 0;
        private imageHeight: number = 0;
        private preImg: any = '/logo.png';
        private option: any = {
            img: '', // 裁剪图片的地址
            info: true, // 裁剪框的大小信息
            outputSize: 0.8, // 裁剪生成图片的质量
            outputType: 'jpeg', // 裁剪生成图片的格式
            canScale: false, // 图片是否允许滚轮缩放
            autoCrop: true, // 是否默认生成截图框
            autoCropWidth: 100, // 默认生成截图框宽度
            autoCropHeight: 100, // 默认生成截图框高度
            fixedBox: true, // 固定截图框大小 不允许改变
            fixed: true, // 是否开启截图框宽高固定比例
            fixedNumber: [1, 1], // 截图框的宽高比例
            full: true, // 是否输出原图比例的截图
            canMoveBox: false, // 截图框能否拖动
            original: false, // 上传图片按照原始比例渲染
            centerBox: true, // 截图框是否被限制在图片里面
            infoTrue: false, // true 为展示真实输出图片宽高 false 展示看到的截图框宽高
        };
        private mounted(): void {}
        // 异步上传封面图片
        private fileChange(e: any): any {
            const oFile = e.target.files[0];
            this.imgCompress(oFile);
            // this.imageWidth = e.target.width;
            // this.imageHeight = e.target.height;
            // if ((oFile.size / 1024) > 1024) {
            //     // 图片压缩
            //     this.imgCompress(oFile, (base64Codes) => {
            //         const blob = this.convertBase64UrlToBlob(base64Codes);
            //         this.getImgBlob(blob);
            //     });
            // } else {
            //     this.getImgBlob(e.target.files[0]);
            // }
        }
        private imgCompress(file: File, callBack?: (base64Codes: any) => void): void {
            const ready: FileReader = new FileReader();
            const imgType: string = file.type;
            ready.readAsDataURL(file);
            ready.onload = () => {
                // 将打开的文件转化成base64位
                if (callBack) {
                    this.canvasDataURL(ready.result, callBack, imgType);
                } else {
                    this.option.img = ready.result;
                }
            };
        }
        private convertBase64UrlToBlob(base64Codes: any): Blob {
            const arr: any[] = base64Codes.split(',');
            const mime: string = arr[0].match(/:(.*?);/)[1];
            const bstr: any = window.atob(arr[1]);
            let n: number = bstr.length;
            const u8arr: Uint8Array = new Uint8Array(n);
            while ( n-- ) {
                u8arr[n] = bstr.charCodeAt(n);
            }
            return new Blob([u8arr], { type: mime });
        }
        private canvasDataURL(path: any, callBack: (base64Codes: any) => void, imgType: string): void {
            const img = new Image();
            img.src = path;
            img.onload = () => {
                const quality: number = 0.7; // 默认图片质量为0.7
                const w: number = this.imageWidth * quality;
                const h: number = this.imageHeight * quality;
                // 生成canvas
                const canvas: HTMLCanvasElement = document.createElement('canvas');
                const ctx: any = canvas.getContext('2d');
                // 创建属性节点
                const anw: Attr = document.createAttribute('width');
                anw.nodeValue = this.imageWidth.toString();
                const anh: Attr = document.createAttribute('height');
                anh.nodeValue = this.imageHeight.toString();
                canvas.setAttributeNode(anw);
                canvas.setAttributeNode(anh);
                ctx.drawImage(img, 0, 0, w, h);
                // quality值越小，所绘制出的图像越模糊
                const base64: any = canvas.toDataURL(`image/${imgType}`, quality);
                // 回调函数返回 base64 的值
                callBack(base64);
            };
        }
        @Emit() private getImgBlob(e: any): any {}
        private preLook(data: any): void {
            // 获取截图的base64 数据
            (this as any).$refs.cropper.getCropData((basedata: any) => {
            // do something
                this.preImg = basedata;
                const blob = this.convertBase64UrlToBlob(basedata);
                const file = new File([blob], 'uploadImg.jpeg', {type: 'jpeg'});
                this.getImgBlob({ file, basedata });
            });
        }
    }
</script>

<style lang="scss">
    .cropper-content {
        .cropper {
            width: auto;
            height: 300px;
        }
    }
    .upload_elebox{
        overflow: hidden;
    }
    .upload_elebox input  {
        opacity: 0;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
    }
    .avatar-body {
        padding-right: 15px;
        padding-left: 15px;
    }
    .avatar-wrapper {
        height: 364px;
        width: 100%;
        margin-top: 15px;
        box-shadow: inset 0 0 5px rgba(0,0,0,.25);
        background-color: #fcfcfc;
        overflow: hidden;
    }
    .avatar-wrapper img {
        display: block;
        height: auto;
        max-width: 100%;
    }
    .avatar-preview {
        float: left;
        margin-top: 15px;
        margin-right: 15px;
        border: 1px solid #eee;
        border-radius: 4px;
        background-color: #fff;
        overflow: hidden;
    }
    .avatar-preview:hover {
        border-color: #ccf;
        box-shadow: 0 0 5px rgba(0,0,0,.15);
    }
    .avatar-preview img {
        width: 100%;
    }
    .preview-lg {
        height: 184px;
        width: 184px;
        margin-top: 15px;
    }
    .preview-md {
        height: 100px;
        width: 100px;
    }
    .preview-sm {
        height: 50px;
        width: 50px;
    }
    @media (min-width: 992px) {
        .avatar-preview {
            float: none;
        }
    }
    .avatar-btns {
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .avatar-btns .btn-group {
        margin-right: 5px;
    }
    .loading {
        display: none;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        opacity: .75;
        filter: alpha(opacity=75);
        z-index: 20140628;
    }
</style>
