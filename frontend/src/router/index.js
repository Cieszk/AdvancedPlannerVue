import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Todolist from "../views/Todolist";
import ArchivedTasks from "../components/ArchivedTasks";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: '/todo-list/',
    name: 'Todolist',
    component: Todolist
  },
  {
    path: '/todo-list/archived/',
    name: 'ArchivedTodolist',
    component: ArchivedTasks
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
