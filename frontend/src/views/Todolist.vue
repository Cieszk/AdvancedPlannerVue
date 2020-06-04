<template>
    <div>
        <div class="container mt-5">
            <div v-for="task in tasks"
                 :key="task.id">
                <div v-if="!task.done" class="task-border mb-3">
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{ task.name }}</h5>
                        <div style="display: inline-block;">
                            <small class="text-muted">{{ task.created_at }}

                            </small>
                            <Task
                                    :key="task.id"
                                    :task="task"
                                    @archive-task="archiveTask"
                            />
                        </div>
                    </div>
                    <small class="text-muted">{{ task.description }}</small>
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
                <p v-if="error" class="error mt-2 alert alert-danger"> {{ error }}</p>
            </form>
        </div>
    </div>

</template>

<script>
    import {apiService} from "../common/api.service";
    import Task from "../components/Task";

    export default {
        name: "Todolist",
        components: {Task},
        data() {
            return {
                tasks: [],
                newTaskBody: null,
                error: null,
                showForm: false
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
                    apiService(endpoint, 'PATCH', {done: true})
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

    .card-color {
        background-color: #333a41;
    }
</style>