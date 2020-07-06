<template>
    <div>
        <button class="btn btn-sm btn-secondary ml-2" @click="triggerArchiveTask">Done</button>
    </div>
</template>

<script>
    export default {
        name: "Task",
        props: {
            task: {
                type: Object,
                required: true
            }
        },
        methods: {
            triggerArchiveTask() {
                this.$emit('archive-task', this.task)
            }
        }
    }
</script>

<style scoped>

</style>