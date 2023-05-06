<template>
    <div id="layout-header">
        <div class="logo-ctn" @click="">
            <img id="logo" src="../../../public/favicon.ico">
        </div>
        <div class="flex-grow"/>

        <div class="menu-ctn">
            <div class="menu-item"  v-for="item in menuList" @click="$router.push(item.route)">
                <el-icon>
                    <component :is="item.icon" class="icon"></component>
                </el-icon>
                {{ item.text }}
            </div>
            <!-- <div class="menu-item">
                <el-link href="https://github.com/login/oauth/authorize?client_id=24197283515faf4e8795" target="self">
                    <el-icon><User /></el-icon>
                    Login
                </el-link>
            </div> -->
        </div>
    </div>
</template>
<style>
#layout-header {
    top: 0;
    height: 64px;
    position: sticky;
    display: flex;
    background-color: rgb(255 255 255 / 0.85);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 10px rgba(0,0,0,.05);
}

.logo-ctn {
    height: 64px;
    line-height: 64px;
    vertical-align: middle;
}

#logo {
    width: 32px;
    height: 32px;
    line-height: 58px;
    vertical-align: middle;
    padding: 12px;
}

.menu-ctn {
    display: flex;
    padding-right: 24px;
    padding: 12px 0;
}

.menu-item {
    border-radius: 6px;
    height: 40px;
    line-height: 40px;
    margin: 0 6px;
    padding: 0 14px;
    cursor: pointer;
    transition: color .3s, background-color .3s;
}

.menu-item-selected, .menu-item:hover {
    color: white;
    background-color: #fa6407;
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
