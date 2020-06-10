<template>
    <div>

        <ul class="nav nav-tabs bg-dark tab-container-style">
            <li class="nav-item ">
                <router-link class="nav-link" :to="{name: 'Todolist'}">Active Tasks</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'ArchivedTodolist' }">Archived Tasks</router-link>
            </li>
        </ul>
        <div class="container mother-container mt-4">
            <div class="container mt-5 ">
                <form class="card card-color form-border" @submit.prevent="createNewTask">
                    <div class="card-header px-3 mr-2">
                        Add new Task
                    </div>
                    <div class="card-block">
                        <textarea
                                class="form-control pull-left"
                                rows="3"
                                cols="2"
                                v-model="newTaskBody"
                                placeholder="Create new task!"
                                style="margin-left: 5px; margin-right: 5px"
                        ></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-secondary ml-2">Add task</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2 alert alert-danger"> {{ error }}</p>
            </div>

            <div class="container mt-5">
                <div v-for="task in tasks"
                     :key="task.id"
                >
                    <div v-if="!task.done" class="task-border mb-3">
                        <div class="d-flex">
                            <h5 class="mr-auto p-2">{{ task.name }}</h5>
                            <div class="p-2">
                                <small class="text-muted">Created at:</small> <small> {{ task.created_at|formatDate
                                }} </small>
                            </div>
                            <div class="p-2">
                                <Task
                                        :key="task.id"
                                        :task="task"
                                        @archive-task="archiveTask"
                                />
                            </div>
                        </div>
                    </div>
                </div>
                <div class="my-4">
                    <p v-show="loadingQuestions">...loading... </p>
                    <button
                            v-show="next"
                            @click="getTasks"
                            class="btn btn-sm btn-danger container">
                        Load More
                    </button>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
    import {apiService} from "../common/api.service";
    import Task from "../components/Task";
    import moment from "moment"

    export default {
        name: "Todolist",
        components: {Task},
        data() {
            return {
                tasks: [],
                next: null,
                error: null,
                showForm: false,
                loadingTasks: false
            }
        },
        methods: {
            getTasks() {
                let endpoint = '/api/tasks/';
                if (this.next) {
                    endpoint = this.next;
                }
                this.loadingTasks = true;
                apiService(endpoint)
                    .then(data => {
                        this.tasks.push(...data.results);
                        this.loadingTasks = false;
                        if (data.next) {
                            this.next = data.next;
                        } else {
                            this.next = null;
                        }
                    })
            },
            archiveTask(task) {
                let endpoint = `/api/tasks/${task.id}/`;
                try {
                    apiService(endpoint, 'PATCH', {done: true});
                    this.$set(task, 'done', true)
                } catch (err) {
                    console.log(err)
                }
            },
            createNewTask() {
                if (this.newTaskBody) {
                    let endpoint = `/api/tasks/`;
                    apiService(endpoint, 'POST', {name: this.newTaskBody})
                        .then(data => {
                            this.tasks.unshift(data)
                        });
                    this.newTaskBody = null;
                    this.showForm = false;
                    if (this.error) {
                        this.error = null;
                    }
                } else {
                    this.error = 'You can\'t add an empty task!'
                }
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

    .card-color {
        background-color: #333a41;
    }


    .mother-container {
        border-style: solid;
        border-color: #383838;
        background-color: #383838;
        margin: auto;
        padding: 8px;
        border-radius: 15px;
    }

    .form-border {
        border-style: solid;
        border-color: #888
    }

    .tab-container-style {
        border-top: solid 1px #888;

    }
    .nav-tabs {
        border-bottom: none;
    }
</style>