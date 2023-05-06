<template>
    <el-config-provider namespace="ep">
        <!-- <BaseHeader/> -->
        <YaHeader />
        <RouterView/>
    </el-config-provider>
</template>

<style>
#app {
    text-align: center;
    color: var(--ep-text-color-primary);
    height: 100%;
}

.element-plus-logo {
    width: 50%;
}
</style>
<script type="ts">
import HomeView from "~/views/HomeView.vue";

export default {
    components: {HomeView},
    created() {
    }
}

</script>