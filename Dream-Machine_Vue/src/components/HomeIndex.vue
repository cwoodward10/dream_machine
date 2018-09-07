<template>
  <div>
    <section id='home' class='full-page'>
      <img src='static/media/images/axon.JPG' class='background-image layer'>
      <article class='center section-title layer'>
        <div class='section-title-content title-font'>
          <p class='title-statement karla'>I dream of Digital Picnics</p>
          <a href='#/Dreams'>See the Dreams</a>
        </div>
      </article>
    </section>

    <section id='how-it-works' class='full-container bkg-white'>
      <article class='center section-title'>
        <div class='section-title-content karla'>

          <p class='title-statement'>How It Works</p>

          <ul class='horiz-menu'>
            <li class='menu-item flex'
                v-for='howTo in howTos'
                v-bind:class="{ active: howTo.active }"
                v-on:click="setActive(howTo)">
                <button>{{ howTo.title }}</button>
            </li>
          </ul>

          <div class='flex diagram-container'>
            <img v-bind:src="'/static/media/images/'+ currentHowTo.src" class='diagram-image one-third flex'>
            <article class='diagram row two-thirds'>
              <h4>{{ currentHowTo.title }}</h4>
              <p>{{ currentHowTo.content }}</p>
            </article>
          </div>

        </div>
      </article>
    </section>

    <section id='dreams-preview' class='full-container bkg-white'>
      <article class='center section-title'>
        <div class='section-title-content karla'>
          <p class='title-statement'>Recent dreams</p>
          <section class='flex'>

            <article class='flex one-third'>
              <p>What's in a dream?</p>
              <p>Dreams are about this stuff</p>
            </article>

            <article class='flex two-thirds dream-list'>

                <div v-for="user in users" class='flex dream-list-item'>
                  <h4>
                    <button v-on:click='user.isCollapsed=!user.isCollapsed'>
                      {{ user.name.first }}'s Dream
                      <svg viewBox="0 0 10 10" v-if="">
                        <rect v-show="user.isCollapsed" class="vert" height="8" width="2" y="1" x="4" />
                        <rect height="2" width="8" y="4" x="1" />
                      </svg>
                    </button>
                  </h4>
                  <p v-bind:class="{ collapsed: user.isCollapsed }">
                    Some contect about <em>{{ user.name.first }} {{ user.name.last }}'s</em>
                    dream should go here.
                    There should be something about the author and something
                    about their storyin the restaurant. What kind of food are
                    they looking for? Who are they with? Etc...
                  </p>
                </div>

            </article>

          </section>
        </div>

      </article>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      howTos: [
        {
          src: 'how-to-01.jpg',
          active: false,
          title: '1. We all have Dreams',
          content: 'Dreams can be complex but often they are as simple as how we want something to feel in a particular moment. Tell us how you want this meal to feel.',
        },
        {
          src: 'how-to-02.jpg',
          active: false,
          title: '2. Give us your story',
          content: 'Tell us about this meal. How do you want to feel? What do you want see or hear? What is the story here? Or, if you\'re feeling creative: what do you want the story to be?',
        },
        {
          src: 'how-to-03.jpg',
          active: false,
          title: '3. We bring it to life',
          content: 'Once you have the story, hit submit and wait for the world to changes around you. Even small changes can have big impacts on how we experience the world. Enjoy!',
        },
      ],
      currentHowTo: [],
      users: [],
    }
  },
  methods: {
    initHowTo() {
      this.currentHowTo = this.howTos[0];
    },
    initActive() {
      this.howTos[0].active = true;
    },
    setActive(current) {
      for (let i = 0; i < this.howTos.length; i += 1) {
        this.howTos[i].active = false;
      }
      current.active = true;
      this.currentHowTo = current;
    },
    getInitialUsers() {
      for (let i = 0; i < 5; i += 1) {
        axios.get(`https://randomuser.me/api/`)
          .then((response) => {
            const newUser = response.data.results[0];
            newUser.isCollapsed = true;
            this.users.push(newUser);
          });
      }
    },
  },
  created() {
    this.initHowTo();
    this.initActive();
  },
  beforeMount() {
    this.getInitialUsers();
  },
};
</script>
