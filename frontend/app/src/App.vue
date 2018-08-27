<template>
  <div id="app">
    <div id="main" class="has-text-justified">
      <h1 class="title is-1">Translation</h1>
      <h4 class="subtitle is-4">テキストボックスの文章をOpenNMTで作成した学習モデルで翻訳した結果を表示します。</h4>
      <div class="columns">
        <div class="column">
          <article class="message">
            <div class="message-header">
              <p>原文</p>
            </div>
            <div class="message-body">
              <form v-on:submit.prevent="translate">
                <textarea class="textarea" v-model="src" name='src' value=''></textarea>
                <button class="button is-light">
                  <span class="icon">
                    <font-awesome-icon prefix="fas" icon="language" />
                  </span>
                  <span>翻訳</span>
                </button>
              </form>
            </div>
          </article>
        </div>
        <div class="column">
          <article class="message">
            <div class="message-header">
              <p>訳文</p>
            </div>
            <div class="message-body">
              <div v-for="translations in translationList" :key="translations.id">
                <div v-for="translation in translations" :key="translation.id">
              <p>{{ translation.tgt }}</p>
                </div>
              </div>
            </div>
          </article>
        </div>
      </div>
      <a href="https://bulma.io" target="_blank">
        <img src="https://bulma.io/images/made-with-bulma.png" alt="Made with Bulma" width="128" height="24">
      </a>
    </div>
    <vue-particles
      color="#dedede"
      :particleOpacity="0.7"
      :particlesNumber="80"
      shapeType="circle"
      :particleSize="4"
      linesColor="#dedede"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="3"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
      clickMode="push"
    >
    </vue-particles>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data () {
    return {
      src: '',
      translationList: ''
    }
  },
  computed: {
    payload: function () {
      console.log('src: ', this.src)
      let srcList = this.src.split(/\n/)
      let payload = []
      console.log('srcList: ', srcList)
      srcList.forEach(value => {
        console.log('value', value)
        payload.push({ src: value })
      })
      return payload
    }
  },
  methods: {
    translate: function (event) {
      event.preventDefault()
      let uri = 'http://localhost:8080/transate'
      axios
        .post(uri, this.payload, {
          headers: {
            'Content-Type': 'text/plain;charset=utf-8'
          }
        })
        .then(response => {
          console.log('status: ', response.status)
          console.log('data: ', response.data)
          this.translationList = response.data
          console.log('translationList: ', this.translationList)
        })
        .catch(error => {
          console.log('error: ', error)
        })
    }
  }
}
</script>

<style>
html,
body,
#app {
  height: 100%;
}

#app {
  position: relative;
  background-image: url("./assets/image/bgimage.jpeg");
  background-size: cover;
}

#main {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}

h1 {
  color: #ffffff !important;
  text-shadow: 5px 5px 0px #000000;
  font-family: "Dosis", sans-serif;
}
h4 {
  color: #ffffff !important;
  text-shadow: 5px 5px 0px #000000;
  font-family: "Dosis", sans-serif;
}
</style>
