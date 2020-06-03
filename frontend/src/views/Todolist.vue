<template>
    <div>
        <div class="container mt-5" v-if="tasks.done">
            <div class="task-border mb-3" v-for="task in tasks"
                 :key="task.id">
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
        <div>
            <div class="form-group mt-4">
                <label for="exampleTextarea">Add new task</label>
                <textarea class="form-control" id="exampleTextarea" rows="3"></textarea>
            </div>
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
            async archiveTask(task) {
                let endpoint = `/api/tasks/${task.id}`;
                var task_index;
                try {
                    await apiService(endpoint);
                    task_index = this.tasks.indexOf(task);
                    Object.assign(this.tasks[task_index], {done: true})
                } catch (err) {
                    console.log(err)
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
</style>