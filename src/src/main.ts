import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'

import './index.css'

import App from './App.vue'
import AddView from './views/AddView.vue'
import CardsView from './views/CardsView.vue'
import EditView from './views/EditView.vue'

const router = createRouter({
  routes: [{
    path: '/',
    component: AddView
  },
  {
    path: '/cards',
    component: CardsView
  },
  {
    path: '/edit/:id',
    component: EditView
  } // ,
  // {
  //   path: '/login',
  //   component: EditView
  // }
  ],
  history: createWebHistory()
})

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
