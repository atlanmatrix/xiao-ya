import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/note',
      name: 'note',
      component: () => import('../views/NoteView.vue')
    },
    {
      path: '/note/editor/rich-text',
      name: 'rich-note-editor',
      component: () => import('../views/note/RTEditorView.vue')
    },
    {
      path: '/note/editor/markdown',
      name: 'md-note-editor',
      component: () => import('../views/note/MDEditorView.vue')
    },
    {
      path: '/function',
      name: 'function',
      component: () => import('../views/FunctionView.vue')
    },
    {
      path: '/flow',
      name: 'flow',
      component: () => import('../views/FlowView.vue')
    },
    {
      path: '/media',
      name: 'media',
      component: () => import('../views/MediaView.vue')
    }
  ]
})

export default router
