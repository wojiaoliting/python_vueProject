<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="dark"  class="shadow">
            
            <b-navbar-brand href="#">{{msg}}</b-navbar-brand>

            <b-navbar-toggle  target = "nav-collapse" > </b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    

                    <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                        <template v-slot:button-content >
                            <!-- <b-icon icon="exclamation-circle-fill"></b-icon> -->
                            <em>{{userName}}</em>
                        </template>
                        <b-dropdown-item href="#" >档案员信息</b-dropdown-item>
                        <b-dropdown-item href="#" class="dropdown-text">注销</b-dropdown-item>
                    </b-nav-item-dropdown>
                    <b-nav-item-dropdown :text="userName" right variant="info">
                        
                        <b-dropdown-item href="#" class="dropdown-text">dsfs</b-dropdown-item>
                        <b-dropdown-item href="#" class="dropdown-text">dsfds</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>

        </b-navbar>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class TopNav extends Vue {
  @Prop(String) private msg!: string;
  @Prop({type: String, default: ' '}) private userName!: string;
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    .navbar-brand{
        // color: #ffe7e7 !important;
        // font-weight: 600;
    }
    .dropdown-bg{

        background-color: #ca3a3a9d;
        // color: #ffe7e7!important;
    }
    .dropdown-text{
        // background-color: #ca3a3a9d;
        color: #ffe7e7!important;
    }
    
</style>
