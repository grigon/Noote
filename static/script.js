import { default as anime } from '../animejs/lib/anime.es.js'

let add_note = document.getElementsByTagName('add_note')
console.log('dupa')


anime({
  targets: add_note,
  translateX: 250
});