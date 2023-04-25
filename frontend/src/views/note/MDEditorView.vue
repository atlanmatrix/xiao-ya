<template>
    <div class="note-page">
        <v-md-editor v-model="text" height="600px"></v-md-editor>

    </div>
</template>

<style>
    .note-page {
        padding-top: 48px;
        max-width: 980px;
        margin: 0 auto;
    }
</style>

<script>
    export default {
        data() {
            return {
                text: '',
            };
        },
    };
</script>