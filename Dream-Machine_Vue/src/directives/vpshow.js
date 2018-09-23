import Vue from 'vue';

// from https://stackoverflow.com/questions/45257308/how-to-display-and-transition-when-scroll-position-reaches-element-position-in-t
export const vpshow = {
  inViewport (el) {
    var rect = el.getBoundingClientRect()
    return !(rect.bottom < 0 || rect.right < 0 ||
             rect.left > window.innerWidth ||
             rect.top > window.innerHeight)
  },

  bind(el, binding) {
    el.classList.add('before-enter');
    el.$onScroll = function() {
      if (binding.def.inViewport(el)) {
        el.classList.add('enter');
        el.classList.remove('before-enter');
        binding.def.unbind(el, binding);
      };
    };
  },

  inserted(el, binding) {
    document.addEventListener('scroll', el.$onScroll);
    el.$onScroll()
  },

  unbind(el, binding) {
    document.removeEventListener('scroll', el.$onScroll)
    delete el.$onScroll
  }
};

Vue.directive('vpshow', vpshow)
