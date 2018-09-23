import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
//  import HomeIndex from '@/components/HomeIndex';
import DreamsApp from '@/components/DreamsApp';
import Index from '@/components/Index.vue'

Vue.use(Router);

export default new Router({
  routes: [
    //  {
    //    path: '/HomeIndex',
    //    name: 'HomeIndex',
    //    component: HomeIndex,
    //  },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/Dreams',
      name: 'DreamsApp',
      component: DreamsApp,
    },
    {
      path: '/',
      name: 'Index',
      component: Index,
    },
  ],
  mode: 'hash',
});
