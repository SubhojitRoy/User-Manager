
import { createRouter, createWebHistory } from 'vue-router'
import UsersView from '../views/UsersView.vue'
import GroupsView from '../views/GroupsView.vue'
import NasView from '../views/NasView.vue'
import PoliciesView from '../views/PoliciesView.vue'
const routes = [
  { path: '/', component: UsersView },
  { path: '/groups', component: GroupsView },
  { path: '/nas', component: NasView },
  { path: '/policies', component: PoliciesView },
]
const router = createRouter({ history: createWebHistory(), routes })
export default router
