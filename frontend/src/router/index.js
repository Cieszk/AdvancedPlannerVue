import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Todolist from "../views/Todolist";

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
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
