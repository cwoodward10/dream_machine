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

      <button v-on:click="toggleCreateDreamModel()" id='create-dream' class='test-container'>
        <svg viewBox="0 0 10 10" class='create-hero one center'>
          <rect class="vert" height="8" width="2" y="1" x="4" />
          <rect height="2" width="8" y="4" x="1" />
        </svg>
        <p class='one center'>Create Your Own Dream</p>
      </button>

      <CreateDreamModal
      v-show="showCreateDreamModal"
      v-on:close="toggleCreateDreamModel"
      >
        <h3 slot='header'>
          Testing this out
          <button
            type="button"
            class="btn-close"
            v-on:click="toggleCreateDreamModel"
            aria-label="Close modal"
          >
          x
          </button>
        </h3>

        <form slot='body' id='CreateDreamForm'
              v-on:submit.prevent='createNewDream();'>

          <div v-for='light in lightControlModal'>

            <h1>{{ light.id }}</h1>

            <label class="switch">
              <h1>on?</h1>
              <input type="checkbox"
                     :name="'lightswitch'+light.id"
                     v-model="light.on">
              <span class="slider round"></span>
            </label>

            <div class="newslidecontainer">
              <label>{{ light.id }}</label>
              <input type="range" min="0" max="254"
                     class="newslider" id="lightbright"
                     v-model.number="light.bri">
              <span></span>
            </div>

          </div>

          <button type='submit'><h1>Submit</h1></button>
        </form>

        <h3 slot='footer'>
          <button
          type="button"
          class="btn-close"
          v-on:click="toggleCreateDreamModel"
          aria-label="Close modal"
          >
          Finish
          </button>
        </h3>
      </CreateDreamModal>

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

import CreateDreamModal from '@/components/CreateDreamModal';

export default {
  data() {
    return {
      hueBridges: [],
      hueUser: "",
      activeBridge: [],
      hueLights: {},
      lightControlModal: [],
      showCreateDreamModal: false,
      dreamsList: [],
    }
  },
  components: {
    CreateDreamModal,
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

            this.initUser();
        };
      }).catch(e => console.log('Error finding bridges', e));
    },
    createLightList() {
      this.hueUser.getLights().then(lights => {
        console.log('getting lights');
        for (var light in lights) {
          this.hueLights[light] = lights[light];
          this.lightControlModal.push(
            {id: light, on: false, bri: 0, color: ''}
          )
        };
      });
    },
    createNewUser() {
      // create user account (requires link button to be pressed)
      this.activeBridge.createUser('dream_machine').then(data => {
        // extract bridge-generated username from returned data
        var username = data[0].success.username;

        console.log('New username:', username);

        localStorage.hueUsername = username;

        // instantiate user object with username
        this.hueUser = this.activeBridge.user(username);
      });
    },
    initUser() {
      console.log('initialize user')
      if (!localStorage.hueUsername) {
        this.createNewUser();
        console.log('new user created')
      } else {
        console.log(localStorage.hueUsername)
        const parsedUsername = localStorage.hueUsername;
        this.hueUser = this.activeBridge.user(parsedUsername);
        this.createLightList();
      }
    },
    toggleColor() {
      this.hueUser.setLightState(2, { on: true, bri: 128, hue: Math.round(Math.random() * 65000) }).then(data => {
        // process response data, do other things
        console.log(data);
      });
    },
    toggleCreateDreamModel() {
      this.showCreateDreamModal = !this.showCreateDreamModal;
    },
    createNewDream() {
      for (var i in this.lightControlModal) {
        var light = this.lightControlModal[i];
        this.hueUser.setLightState(light.id, {on: light.on, bri: light.bri});
      }
    }
  },
  created() {
    this.initBridge()
  },
}


</script>

<style>
/* The switch - the box around the slider */
.switch {
 position: relative;
 display: inline-block;
 width: 60px;
 height: 34px;
}

/* Hide default HTML checkbox */
.switch input {display:none;}

/* The slider */
.slider {
 position: absolute;
 cursor: pointer;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 background-color: #ccc;
 -webkit-transition: .4s;
 transition: .4s;
}

.slider:before {
 position: absolute;
 content: "";
 height: 26px;
 width: 26px;
 left: 4px;
 bottom: 4px;
 background-color: white;
 -webkit-transition: .4s;
 transition: .4s;
}

input:checked + .slider {
 background-color: #2196F3;
}

input:focus + .slider {
 box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
 -webkit-transform: translateX(26px);
 -ms-transform: translateX(26px);
 transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
 border-radius: 34px;
}

.slider.round:before {
 border-radius: 50%;
}

.newslidecontainer {
    width: 100%; /* Width of the outside container */
}

/* The slider itself */
.newslider {
    -webkit-appearance: none;  /* Override default CSS styles */
    appearance: none;
    width: 100%; /* Full-width */
    height: 25px; /* Specified height */
    background: #d3d3d3; /* Grey background */
    outline: none; /* Remove outline */
    opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
    -webkit-transition: .2s; /* 0.2 seconds transition on hover */
    transition: opacity .2s;
}

/* Mouse-over effects */
.newslider:hover {
    opacity: 1; /* Fully shown on mouse-over */
}

/* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
.newslider::-webkit-slider-thumb {
    -webkit-appearance: none; /* Override default look */
    appearance: none;
    width: 25px; /* Set a specific slider handle width */
    height: 25px; /* Slider handle height */
    background: #4CAF50; /* Green background */
    cursor: pointer; /* Cursor on hover */
}

.newslider::-moz-range-thumb {
    width: 25px; /* Set a specific slider handle width */
    height: 25px; /* Slider handle height */
    background: #4CAF50; /* Green background */
    cursor: pointer; /* Cursor on hover */
}
</style>
