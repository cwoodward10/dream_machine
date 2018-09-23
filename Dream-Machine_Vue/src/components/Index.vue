<template>
  <div style='height: 100vh; overflow:hidden'>

    <transition name='fade' v-if='showSplash'>
    <section id='splash-page' class='flex flex-column'>

      <div id='splash-loading'>
        <img src="@/assets/SVG/outer.svg" class='splash-animation rotator-outer'>
        <img src="@/assets/SVG/middle.svg" class='splash-animation rotator-middle'>
        <img src="@/assets/SVG/inner.svg" class='splash-animation rotator-inner'>
      </div>

      <article class='caption flex-column item-center'>
        <h1 id='splash-title' class='flex'>Do You Dream of Digital Picnics?</h1>
        <h3 id='splash-close' class='flex' v-on:click="toggleSplash()">Start Dreaming</h3>
      </article>

    </section>
    </transition>

    <nav class='nav'>
      <h3 class='nav-hero'>An Empathic Futures Lab Production</h3>

      <div class='hamburger' v-on:click="toggleHamburger()">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
      </div>
      <transition name="slide-down">
        <div class='hamburger-menu' v-if='showHamburger'>
          <div class='hamburger' v-on:click="toggleHamburger()">
            <h1>X</h1>
          </div>
          <ul>
            <li class='ham-item'>Home</li>
            <li class='ham-item'>About</li>
          </ul>
        </div>
      </transition>
    </nav>

    <div class='snap-container'>
      <section class='full-screen flex flex-column' v-vpshow>
        <article class='content-container'>

          <img src='@/assets/picnic1.jpg' class='main-image item-center'>
          <div class='flex caption'>
            <h3 class='caption-title'>I<br class='title-break'> Dream<br class='title-break'> of a<br class='title-break'> Digital Picnic</h3>
            <p class='flex caption-text'>
              The physical tradition of dining is rich in social and sensorial interactions with the surrounding environment. That being said, our “environment” is no longer just the physical world - man made, natural or otherwise - but instead now includes non-physical artifacts such as those in the digital realm. I Dream of a Digital Picnic seeks to enhance the tradition of dining through the layering of responsive environmental elements, both physical and digital, with human thoughts and emotions. This would be done through use of “Dreams”: digital artifacts that, when created by a restaurant patron, would be embedded with a user-defined narrative and set of commands to be translated to the physical installation’s lights and speakers. These augmentations would work in concert with the physical elements of the restaurant in order to construct an environment more fully reflective of those dining within it.
            </p>
          </div>

        </article>
      </section>

      <section class='full-screen flex' v-vpshow>
        <article class='content-container'>

          <img src='@/assets/picnic2.jpg' class='main-image item-center'>
          <div class='flex caption caption-text center'>
            The physical tradition of dining is rich in social and sensorial interactions with the surrounding environment.That being said, our “environment” is no longer just the physical world - man made, natural or otherwise - but instead now includes non-physical artifacts such as those in the digital realm. I Dream of a Digital Picnic (IDoaDP) seeks to enhance the tradition of dining through the layering of responsive environmental elements, both physical and digital, with human thoughts and emotions. This will be done by creating a micro-environment around a restaurant table through the use of a suspended thermo-plastic armature with controllable lights and speakers. A kiosk on the table will use a web-application to translate user-created digital artifacts, what we call “Dreams”, into environmental factors thus allowing the user to craft an experience fitting their current emotions, food choices, and other factors influencing their current disposition. Where traditionally the restaurant is responsible for the entire dining experience, this proposal allows the patrons and restaurant to work together in concert.
          </div>

        </article>
      </section>

      <section class='full-screen flex' v-vpshow>
        <article class='content-container'>

          <img src='@/assets/picnic3.jpg' class='main-image item-center'>
          <div class='flex caption caption-text center'>
            The physical tradition of dining is rich in social and sensorial interactions with the surrounding environment.That being said, our “environment” is no longer just the physical world - man made, natural or otherwise - but instead now includes non-physical artifacts such as those in the digital realm. I Dream of a Digital Picnic (IDoaDP) seeks to enhance the tradition of dining through the layering of responsive environmental elements, both physical and digital, with human thoughts and emotions. This will be done by creating a micro-environment around a restaurant table through the use of a suspended thermo-plastic armature with controllable lights and speakers. A kiosk on the table will use a web-application to translate user-created digital artifacts, what we call “Dreams”, into environmental factors thus allowing the user to craft an experience fitting their current emotions, food choices, and other factors influencing their current disposition. Where traditionally the restaurant is responsible for the entire dining experience, this proposal allows the patrons and restaurant to work together in concert.
          </div>

        </article>
      </section>

      <section class='full-screen flex' v-vpshow>

        <article class='content-container' style='width:80%;'>
          <h1 class='item-center'>Coming Soon</h1>
          <div class='flex caption caption-text center'>Keep checking back for more information</div>
        </article>

      </section>
    </div>
  </div>
</template>

<script>
  import { vpshow } from '@/directives/vpshow.js';

  export default {
    data() {
      return {
        showSplash: false,
        showHamburger: false,
        current: 'Home',
        pages: {
          render1: false,
          render2: false,
          render3: false,
          contact: false,
        }
      }
    },
    directives: {
      vpshow,
    },
    methods: {
      toggleHamburger() {
        this.showHamburger = !this.showHamburger;
      },
      toggleSplash() {
        this.showSplash = !this.showSplash;
      },
    },
    mounted() {
      this.toggleSplash();
    }
  }
</script>

<style>

  @import url('https://fonts.googleapis.com/css?family=Cabin|Josefin+Sans');

  #splash-page {
    position: fixed;
    height: 105vh;
    width: 100%;
    z-index: 13;
    background: #654ea3;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #eaafc8, #654ea3);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to right, #eaafc8, #654ea3); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: white;
  }

  #splash-title {
    margin: auto;
    padding: 1em;
  }

  #splash-close {
    margin: auto;
    padding: 0;
  }
  #splash-close:hover {
    cursor: pointer;
    z-index: 20;
  }

  #splash-loading {
    width: 25%;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: -1;
  }

  .splash-animation {
    width: 100%;
    position: fixed;
    top: 50%;
    left: 50%;
    z-index: -1;
    opacity: 25%;
  }

  .rotator-outer {
    animation: spin 15s infinite linear;
    -webkit-animation: spin 15s infinite linear;
  }
  .rotator-middle {
    animation: spin-ccw 10s infinite linear;
    -webkit-animation: spin-ccw 10s infinite linear;
  }
  .rotator-inner {
    animation: spin 30s infinite linear;
    -webkit-animation: spin 30s infinite linear;
    display: none;
  }

  @keyframes spin {
      from{
          transform: translate(-50%,-50%) rotate(0deg);
      }
      to{
          transform: translate(-50%,-50%) rotate(360deg);
      }
  }

  @keyframes spin-ccw {
      from{
          transform: translate(-50%,-50%) rotate(0deg);
      }
      to{
          transform: translate(-50%,-50%) rotate(-360deg);
      }
  }

  h1 {
    padding: 0;
    margin: 0;
    font-family: 'Cabin', sans-serif;
  }

  .nav {
    position: fixed;
    width: 100%;
    background-color: rgba(0,0,0,0);
    color: #333;
    top: 0;
    vertical-align: middle;
    z-index: 15;
    font-family: 'Josefin Sans', sans-serif;
  }

  .flex {
    display: flex;
  }

  .flex-column {
    flex-direction: column;
  }

  h3.nav-hero {
    position: fixed;
    display: inline-block;
    top: 2%;
    left: 2%;
    padding: 0;
    margin: 0;
    width: fit-content;
  }

  .hamburger {
    display: inline-block;
    cursor: pointer;
    position: fixed;
    top: 2%;
    right: 2%;
    transform: translateX(-100%);
  }

  h1.exit-button {
    all: inherit;
  }

  .bar1, .bar2, .bar3 {
    display: static;
    width: 25px;
    height: 3px;
    background-color: #333;
    margin: 5px 0;
    transition: 0.4s;
  }

  .hamburger-menu {
    z-index: 10;
    background-color: white;
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    padding: 1em;
    text-align: center;
    margin: 0;
  }

  .ham-item {
    list-style-position: inside;
    list-style-type: none;
    padding: .25em 5em;
  }

  div.snap-container {
    height: 100vh;
    overflow: scroll;
    scroll-snap-type: y proximity;
  }

  .full-screen {
    padding: 0;
    margin: 0;
    height:105vh;
    width: 100%;
    scroll-snap-align: center;
  }

  .content-container {
    display: flex;
    flex-direction: column;
    max-height: 80vh;
    max-width: 75%;
  }

  .main-image {
    display: flex;
    max-height: 75%;
    width: 100%;
    padding-bottom: 2em;
    overflow: hidden;
  }

  .caption {
    margin: 0 auto;
    width: 80%;
  }

  .caption-title {
    width: fit-content;
    text-align: right;
    padding-right: 1em;
    font-family: 'Cabin', sans-serif;
  }

  @media only screen and (max-width: 767px) {
    .caption-title {
      padding-right: 0;
      text-align: center;
      width: 100%;
      padding-bottom: .5em;
    }
    br.title-break {
      display: none;
    }
  }

  .caption-text {
    font-size: .75em;
    text-align: justify;
    flex: 1;
    font-family: 'Cabin', sans-serif;
  }

  .item-center {
    display: flex;
    justify-content: center;
    text-align: center;
    vertical-align: middle;
    margin: auto;
  }

  .before-enter {
    opacity: 0;
  }

  .enter {
  transition: opacity 2s ease;
  }

  .slide-down-enter-active, .slide-down-leave-active {
    transition: transform .5s ease;
  }

  .slide-down-enter, .slide-down-leave-to {
    transform: translateY(-100%);
  }

  .slide-down-enter-to, .slide-down-leave {
  transform: translateX(0);
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity 2s ease;
  }

  .fade-enter, .fade-leave-to {
    opacity: 0;
  }

  .fade-enter-to, .fade-leave {
    opacity: 100%;
  }

</style>
