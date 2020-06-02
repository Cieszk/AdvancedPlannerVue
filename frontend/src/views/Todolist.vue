<template>
    <div class="container mt-5">
        <div class="task-border mb-3" v-for="task in tasks"
             :key="task.pk">
            <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">{{ task.name }}</h5>
                <small class="text-muted">{{ task.created_at }}<button type="button" class="btn btn-sm btn-secondary ml-2">Done</button></small>
            </div>
            <small class="text-muted">{{ task.description}}</small>
        </div>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "Todolist",
        data() {
            return {
                tasks: []
            }
        },
        methods: {
            getTasks() {
                let endpoint = '/api/tasks/';
                apiService(endpoint)
                    .then(data => {
                        this.tasks.push(...data.results);
                    })
            }
        },
        created() {
            this.getTasks()
        }
    }
</script>

<style scoped>
    .task-border {
        border-style: solid;
        border-color: #888;
        margin: auto;
        border-radius: 10px;
        padding: 8px;
        background-color: #333a41;
    }
</style>