//npm install vue-router
import { createRouter, createWebHistory } from 'vue-router';

// Import your components (screens)
import HomeScreen from '../components/HomeScreen.vue';
import SandboxScreen from '../components/SandboxScreen.vue';
import PracticeProblemScreen from '../components/PracticeProblemScreen.vue';

const routes = [
    { path: '/', name: 'Home', component: HomeScreen },
    { path: '/sandbox', name: 'Sandbox', component: SandboxScreen },
    { path: '/practice', name: 'Practice', component: PracticeProblemScreen },
];

const router = createRouter({
    history: createWebHistory(), // Enables clean URLs without hash (#)
    routes,
});

export default router;
