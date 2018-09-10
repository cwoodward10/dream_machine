<template>
  <div>

    <section id='splash page' class='full-page'>

      <article id='splash-intro' class='center test-container'>
        <h3>I dream of Digital Picnics</h3>
        <p>
         Some texting giving a short description
         on what is going on here.
        </p>
        <button>How it Works</button>
      </article>

    </section>

    <section id='dreams-home' class='full-page'>

      <nav class='main-nav'>
        <h1 class='main-title center test-container'>DO YOU DREAM OF DIGITAL PICNICS?</h1>
        <button v-on:click="toggleColor()"> Button</button>
      </nav>

      <article id='create-dream' class='test-container'>
        <svg viewBox="0 0 10 10" class='create-hero one center'>
          <rect class="vert" height="8" width="2" y="1" x="4" />
          <rect height="2" width="8" y="4" x="1" />
        </svg>
        <button v-on:click="toggleColor()" class='create-button one center'>Create Your Own Dream</button>
      </article>

    </section>



    <nav class='dreams-nav one flex test-container'>
      <p>other nav stuff here</p>
    </nav>

    <section class='dream-container flex full-page bkg-white'>

      <article class="dream-item flex one-third">
        <p>Hello World</p>
      </article>

      <article class="dream-item flex one-third">
        <p>Hello World</p>
      </article>

      <article class="dream-item flex one-third">
        <p>Hello World</p>
      </article>

    </section>

  </div>
</template>

<script>
import axios from 'axios';
import jsHue from 'jshue';

export default {
  data() {
    return {
      hueBridges: [],
      hueUser: "",
      activeBridge: [],
    }
  },
  methods: {
    initBridge() {
      console.log('initBridge')
      var hue = jsHue();
      hue.discover().then(bridges => {
        if(bridges.length === 0) {
            console.log('No bridges found. :(');
        }
        else {
            bridges.forEach(b => this.hueBridges.push(b.internalipaddress));

            console.log(this.hueBridges);

            this.activeBridge = hue.bridge(this.hueBridges[0]);

            this.checkHueUsername();
        };
      }).catch(e => console.log('Error finding bridges', e));
    },
    checkHueUsername() {
      console.log('checkHueUsername')
      if (!localStorage.hueUsername) {
        this.initUser();
        console.log('run initUser')
      } else {
        console.log(localStorage.hueUsername)
        const parsedUsername = localStorage.hueUsername;
        this.hueUser = this.activeBridge.user(parsedUsername);
        this.hueUser.setLightState(2, { on: false }).then(data => {
          // process response data, do other things
          console.log(data);
        });
      }
    },
    initUser() {
      // create user account (requires link button to be pressed)
      this.activeBridge.createUser('dream_machine').then(data => {
          // extract bridge-generated username from returned data
          var username = data[0].success.username;

          console.log('New username:', username);

          localStorage.hueUsername = username;

          // instantiate user object with username
          this.hueUser = this.activeBridge.user(username);

          this.hueUser.setLightState(2, { on: true }).then(data => {
            // process response data, do other things
            console.log(data);
          });
      })
    },
    toggleColor() {
      this.hueUser.setLightState(2, { on: true, bri: 128, hue: Math.round(Math.random() * 65000) }).then(data => {
        // process response data, do other things
        console.log(data);
      });
    },
  },
  created() {
    this.initBridge()
  },
}


</script>
