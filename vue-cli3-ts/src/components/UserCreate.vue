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
      <b-button pill variant="outline-light">
          <b-icon icon="person-plus" aria-hidden="true" ></b-icon>
          成员添加
      </b-button>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class UserCreate extends Vue {
//   @Prop() private msg!: string;
    public selected: any = null;
    public options: any[] = [
        { value: null, text: 'Please select an option' },
        { value: 'a', text: 'This is First option' },
        { value: 'b', text: 'Selected Option' },
        { value: { C: '3PO' }, text: 'This is an option with object value' },
        { value: 'd', text: 'This one is disabled', disabled: true }
    ]

}
</script>

<style scoped lang="scss">

</style>
