<template>
    <div>
        <ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" data-toggle="tab" href="#home">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" data-toggle="tab" href="#profile">Archived</a>
  </li>
</ul>
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
                <div v-else-if="task.done" class="task-border mb-3">
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
        <div class="container mt-5">
            <form class="card card-color" @submit.prevent="createNewTask">
                <div class="card-header px-3">
                    Add new Task
                </div>
                <div class="card-block">
                <textarea
                        class="form-control"
                        rows="3"
                        cols="3"
                        v-model="newTaskBody"
                        placeholder="Create new task!"
                >

                </textarea>
                </div>
                <div class="card-footer px-3">
                    <button type="submit" class="btn btn-sm btn-secondary ml-2">Add task</button>
                </div>
            </form>
            <p v-if="error" class="error mt-2 alert alert-danger"> {{ error }}</p>
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
                newTaskBody: null,
                error: null,
                showForm: false,
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
</style>