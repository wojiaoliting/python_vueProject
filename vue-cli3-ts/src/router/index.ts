import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import App from '../App.vue';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Admin from '../views/Admin.vue';
import Article from '../views/Article.vue';
import { LayoutPlugin } from 'bootstrap-vue';


Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '/admin',
        name: 'Admin',
        component: Admin,
      },
      {
        path: '/article',
        name: 'Article',
        component: Article,
      },
      {
        path: '/about',
        name: 'About',
        component: () => import('../views/About.vue'),
      },
    ],
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
