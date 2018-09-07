import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
//  import HomeIndex from '@/components/HomeIndex';
import DreamsApp from '@/components/DreamsApp';

Vue.use(Router);

export default new Router({
  routes: [
    //  {
    //    path: '/',
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
  ],
  mode: 'hash',
});
