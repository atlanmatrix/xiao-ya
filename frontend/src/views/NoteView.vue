<template>
    <div class="note-page">
       <el-row justify="end">
            <el-button type="primary" :icon="Plus" >
                新建
            </el-button>
       </el-row>
        <el-row v-for="line of tableData">
            <div class="note-card">
                <div class="note-title">{{ line['title'] }}</div>
                <div class="note-create-time">{{ line['create_time'] }}</div>
            </div>
       </el-row>
    </div>
</template>

<style>
    .note-card {
        width: 100%;
        max-width: 980px;
        height: 120px;
        margin-top: 24px;
        border-radius: 32px;
        border: 0;
        outline: 0;
        font-size: 16px;
        border-radius: 32px;
        padding: 16px;
        background-color: #EBECF0;
        text-shadow: 1px 1px 0 #FFF;

        margin-top: 24px;
        margin-right: 8px;
        box-shadow: inset 1px 1px 2px #babecc, inset -1px -1px 2px #fff;
        width: 100%;
        box-sizing: border-box;
        transition: all 0.2s ease-in-out;
    }

    .note-title {
        font-weight: 600;
    }

    .note-create-time {
        color: #aaa;
        font-size: 12px;
    }
.note-page {
    padding-top: 48px;
    max-width: 980px;
    margin: 0 auto;
}

.el-table {
  border: none;
}

.ql-container.ql-snow {
    height: 600px;
}

@media (min-width: 1024px) {

}
</style>
<script setup lang="ts">
    import {ref} from 'vue'
    import { Delete, Edit, Search, Share, Upload, Plus } from '@element-plus/icons-vue'
    import {vGet, vPost, vSuccessAlert, vErrorAlert, getFooterRef} from "../components/utils"

    let tableData = ref([])

    vGet(`/xiaoya/note`, {}, (res) => {
        console.log(res, res.data)
        if (res.code == 0) {
            tableData.value = res.data;
            tableData.value = [];
        } else {
        }
    })
</script>
