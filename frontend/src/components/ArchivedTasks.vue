<template>
    <div>
        <ul class="nav">
            <li class="nav-item">
                <router-link class="nav-link active" :to="{name: 'Todolist'}">Active Tasks</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'ArchivedTodolist' }">Archived Tasks</router-link>
            </li>
        </ul>
        <div class="container mt-5">
            <div
                    v-for="task in tasks"
                    :key="task.id"
            >
                <div v-if="task.done" class="task-border mb-3">
                    <div class="d-flex">
                        <h5 class="mr-auto p-2">
                            <del>{{ task.name }}</del>
                        </h5>
                        <div class="p-2">
                            <small class="text-muted">Created at:</small> <small> {{ task.created_at|formatDate
                            }} </small>
                        </div>
                        <div class="p-2">
                            <div class="alert alert-success">
                                Task Archived
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";
    import moment from "moment";

    export default {
        name: "ArchivedTasks",
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
            },
        },
        created() {
            this.getTasks()
        },
        filters: {
            formatDate: function (value) {
                if (value) {
                    return moment(String(value)).format('DD/MM/YYYY hh:mm')
                }
            }
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