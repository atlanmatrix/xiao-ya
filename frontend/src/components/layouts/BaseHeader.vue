<script lang="ts" setup>
import {toggleDark} from "~/composables";
</script>

<template>
    <el-menu class="el-menu-demo" mode="horizontal" :ellipsis="false" router :default-active="$route.path">
        <div style="height: 58px;line-height: 58px; vertical-align: middle" @click="goToHome">
            <img id="logo" src="../../../public/favicon.ico">
        </div>
        <div class="flex-grow"/>
        <el-menu-item v-for="item in menuList" :index="item.route">
            <el-icon>
                <component :is="item.icon" class="icon"></component>
            </el-icon>
            {{ item.text }}
        </el-menu-item>
        <el-menu-item>
            <el-link href="https://github.com/login/oauth/authorize?client_id=24197283515faf4e8795" target="self">
                <el-icon><User /></el-icon>
                Login
            </el-link>
        </el-menu-item>
<!--        <el-menu-item h="full" @click="toggleDark()">-->
<!--            <button-->
<!--                    class="border-none w-full bg-transparent cursor-pointer"-->
<!--                    style="height: var(&#45;&#45;ep-menu-item-height)"-->
<!--            >-->
<!--                <i inline-flex i="dark:ep-moon ep-sunny"/>-->
<!--            </button>-->
<!--        </el-menu-item>-->
    </el-menu>
</template>

<style>
    #logo {
        width: 32px;
        height: 32px;
        line-height: 58px;
        vertical-align: middle;
        padding: 12px;
    }
</style>

<script lang="ts">
export default {
    data() {
        return {
            activeIndex: '/',
            menuList: [{
                route: '/note',
                text: 'Note',
                icon: 'Notebook'
            }, {
                route: '/flow',
                text: 'Flow',
                icon: 'Guide'
            }, {
                route: '/function',
                text: 'Function',
                icon: 'MagicStick'
            }, {
                route: '/media',
                text: 'Media',
                icon: 'Headset'
            }]
        }
    },
    created() {
    },
    methods: {
        goToHome() {
            this.$router.push({name: 'home', query: {id: 1}})
        }
    }
}
</script>
