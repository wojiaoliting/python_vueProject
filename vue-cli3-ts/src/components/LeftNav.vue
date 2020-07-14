<template>
  <div role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" @click="toggleDown" class="p-1 d-flex justify-content-between align-items-center" role="tab">
            <b-button block variant="dark"  right v-b-toggle.index-a.index-b class="d-flex justify-content-between align-items-center">
                <div>
                    <b-icon icon="house-fill" aria-hidden="true" ></b-icon>
                    首页
                </div>
                <b-icon icon="caret-right" aria-hidden="true" :rotate="deg"></b-icon>
            </b-button>
        </b-card-header>
        <b-collapse id="index-a" class="mt-1">
            <b-button block variant="light">首页1</b-button>
        </b-collapse>
        <b-collapse id="index-b" class="mt-1">
            <b-button block variant="light">首页2</b-button>
        </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block variant="dark" class="d-flex justify-content-between align-items-center">
                <div>
                    <b-icon icon="award" aria-hidden="true"></b-icon>
                    <b-link to="/admin" class="text-white">
                    用户管理
                    </b-link>
                </div>
            
            </b-button>
        </b-card-header>
    </b-card>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component({})
export default class LeftNav extends Vue {
    // private slideIconNameList: string[] = ['right', 'down'];
    private toggleStatu: boolean = false;
    private deg: string = '0';
    // @Prop(String) private listName!: string;
    // @Prop({type: String, default: ' '}) private userName!: string;
    private toggleDown(): void {
        let str: string = '0';
        this.toggleStatu = !this.toggleStatu;
        str = this.toggleStatu ? '90' : '0';
        this.deg = str;
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

    
</style>
