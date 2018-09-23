import Vue from 'vue';

// from https://stackoverflow.com/questions/45257308/how-to-display-and-transition-when-scroll-position-reaches-element-position-in-t
export const onScrollLeft = {
  bind(el, binding) {
    el.$onScroll = function() {
      el.classList.add('scroll-left');
      el.classList.remove('scroll-left-start');
      binding.def.unbind(el, binding);
    };
  },

  inserted(el, binding) {
    el.classList.add('scroll-left-start');
    document.addEventListener('scroll', el.$onScroll);
  },

  unbind(el, binding) {
    document.removeEventListener('scroll', el.$onScroll)
    delete el.$onScroll
  }
};

Vue.directive('onScrollLeft', onScrollLeft)
