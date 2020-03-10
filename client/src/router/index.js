import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Shakespeare from "../views/Shakespeare.vue";
import Sherlock from "../views/Sherlock.vue";
import Wilde from "../views/Wilde.vue";
import Austen from "../views/Austen.vue";
import Custom_generator from "../views/Generator.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/shakespeare",
    name: "Shakespeare",
    component: Shakespeare
  },
  {
    path: "/sherlock",
    name: "Sherlock",
    component: Sherlock
  },
  {
    path: "/wilde",
    name: "Wilde",
    component: Wilde
  },
  {
    path: "/austen",
    name: "Austen",
    component: Austen
  },
  {
    path: "/generator",
    name: "Generator",
    component: Custom_generator
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
