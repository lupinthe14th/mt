<template>
  <div id="app">
    <div id="main" class="has-text-justified">
      <h1 class="title is-1">
        <font-awesome-icon :icon="['fas','language']" />
        Translation</h1>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title">原文</p>
            <p class="subtitle">日本語</p>
            <div id="textarea">
            <textarea class="content textarea"
                      @input="textareaResize"
                      @keyup.capture="translate"
                      ref="textarea"
                      v-model="src"
                      name='src'
                      value=''
                      placeholder='テキストを入力'
                      rows="5"
                      />
              <font-awesome-icon id="clearButton"
                                 v-show="Object.keys(this.src).length"
                :icon="['far','times-circle']" v-on:click="clear()" />
            </div>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title">訳文</p>
            <p class="subtitle">英語</p>
            <div v-for="translations in translationList" :key="translations.id">
              <div v-for="translation in translations" :key="translation.id">
                <p class="content">{{ translation.tgt }}</p>
              </div>
            </div>
          </article>
        </div>
      </div>
      <footer class="footer">
        <div class="content has-text-justfied">
          <a href="https://bulma.io" target="_blank">
            <img src="https://bulma.io/images/made-with-bulma.png" alt="Made with Bulma" width="128" height="24">
          </a>
        </div>
      </footer>
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
        if (!value) {
          console.log('value is null or undefined or ""')
        } else {
          payload.push({ src: value })
        }
      })
      console.log('payload', payload)
      return payload
    }
  },
  methods: {
    textareaResize () {
      this.$refs.textarea.style.minHeight =
        this.$refs.textarea.scrollHeight + 'px'
    },
    clear: function () {
      Object.assign(this.$data, this.$options.data.call(this))
    },
    translate: function () {
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
  position: relative;
  background-image: url("./assets/image/bgimage.jpeg");
  background-size: cover;
}

#main {
  position: absolute;
  width: 99%;
}
#textarea {
  position: relative;
  display: inline-block;
  width: 100%;
}
#clearButton {
  position: absolute;
  right: 2px;
  top: 2px;
  cursor: pointer;
}
h1 {
  color: #ffffff !important;
  text-shadow: 5px 5px 0px #000000;
  font-family: "Dosis", sans-serif;
}

footer {
  background-color: transparent !important;
}
</style>
