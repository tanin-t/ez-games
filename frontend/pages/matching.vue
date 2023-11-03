<template>
    <v-app>
      <v-main>
        <div class="container">
        <v-card class="mx-auto" max-width="600" max-height="270">
          <v-img
            class="text-white mx-0"
            height="300"
            :src="question"
            cover
          >
            <v-row no-gutters>
              <v-col cols="6" class="pa-0 d-flex flex-wrap">
                <template v-for="i in buttons_left">
                  <v-btn
                    :disabled="disabledL"
                    v-if="i.status == 'close'"
                    elevation="0"
                    color="black"
                    style="height: 90px; width: 100px"
                    class="text-white mx-0"
                    rounded="0"
                    @click="OpencardLeft(i)"
                    >{{ i.label }}</v-btn
                  >
  
                  <img
                    v-if="i.status == 'open'"
                    style="height: 90px; width: 100px"
                    :src="i.url"
                  >
             
  
                  <div
                    v-if="i.status == 'clear'"
                    style="height: 90px; width: 100px"
                  ></div>
                </template>
              </v-col>
  
              <v-col cols="6" class="pa-0 d-flex flex-wrap">
                <template v-for="i in buttons_right">
                  <v-btn
                    v-if="i.status == 'close'"
                    :disabled="disabledR"
                    elevation="0"
                    color="pink"
                    style="height: 90px; width: 100px"
                    class="text-black mx-0"
                    rounded="0"
                    @click="OpencardRight(i)"
                    >{{ i.label }}</v-btn
                  >
  
                  <img
                    v-if="i.status == 'open'"
                    style="height: 90px; width: 100px"
                    :src="i.url"
                  >
      
  
                  <div
                    v-if="i.status == 'clear'"
                    style="height: 90px; width: 100px"
                  ></div>
                </template>
              </v-col>
            </v-row>
          </v-img>
        </v-card>
        <div class="my-2 mx-8">
          <v-btn block @click="clear()">clear</v-btn>
        </div>
        <div class="d-flex justify-space-between my-2 mx-8">
          <v-btn @click="answer()">answer</v-btn>
          <v-btn color="success" @click="next()">Next</v-btn>
        </div>
        
      </div>
      </v-main>
    </v-app>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  const L = ref(
    [
      { url: "public/IMG_565.jpg", status: "close" },
      { url: "public/IMG_5640.jpg", status: "close" },
      { url: "public/IMG_5642.jpg", status: "close" },
      { url: "public/IMG_5643.jpg", status: "close" },
      { url: "public/IMG_5644.jpg", status: "close" },
      { url: "public/IMG_5645.jpg", status: "close" },
      { url: "public/IMG_5646.jpg", status: "close" },
      { url: "public/IMG_5650.jpg", status: "close" },
      { url: "public/IMG_5652.jpg", status: "close" },
    ]
  );
  const R= ref(
    [
      { url: "public/IMG_565.jpg", status: "close" },
      { url: "public/IMG_5640.jpg", status: "close" },
      { url: "public/IMG_5642.jpg", status: "close" },
      { url: "public/IMG_5643.jpg", status: "close" },
      { url: "public/IMG_5644.jpg", status: "close" },
      { url: "public/IMG_5645.jpg", status: "close" },
      { url: "public/IMG_5646.jpg", status: "close" },
      { url: "public/IMG_5650.jpg", status: "close" },
      { url: "public/IMG_5652.jpg", status: "close" },
    ]
  );
  const buttons_left = ref([])
  const buttons_right = ref([])  
  const alphabets = ref(["A", "B", "C", "D", "E", "F", "G", "H", "I"]);
  const numbers = ref(["1", "2", "3", "4", "5", "6", "7", "8", "9"]);
  const left = ref("");
  const right = ref("");
  const disabledL = ref(false);
  const disabledR = ref(false);
  const questions = ref(["public/IMG_565.jpg","public/IMG_5642.jpg"])
  const question = ref('')
  onMounted(() => {
    ShuffleButton();
  });

  function ShuffleButton(){
    buttons_left.value = shuffle(L.value)
    buttons_right.value = shuffle(R.value)
    question.value = shuffle(questions.value)[0]

    AddProperty()
  }

  function AddProperty() {
    for (let i in buttons_left.value) {
      buttons_left.value[i].label = alphabets.value[i];
    }
  
    for (let i in buttons_right.value) {
      buttons_right.value[i].label = numbers.value[i];
    }
  }
  
  function OpencardLeft(i) {
    i.status = "open";
    left.value = i;
    console.log(left.value);
    disabledL.value = true;
    if (disabledR.value) {
      if (left.value.url == right.value.url) {
        left.value.status = "clear";
        right.value.status = "clear";
        disabledL.value = false;
        disabledR.value = false;
        left.value = ""
        right.value = ""
        new Audio("public/yeah.mp3").play()
      }
      else{
        new Audio("public/oh-no.mp3").play()
      }
    }
  }
  
  function OpencardRight(i) {
    i.status = "open";
    right.value = i;
    console.log(right.value);
    disabledR.value = true;
    if (disabledL.value) {
      if (left.value.url == right.value.url) {
        left.value.status = "clear";
        right.value.status = "clear";
        disabledL.value = false;
        disabledR.value = false;
        left.value = ""
        right.value = ""
        new Audio("public/yeah.mp3").play()
      }
      else{
        new Audio("public/oh-no.mp3").play()
      }
    }
  }
  
  function clear() {
    new Audio("public/click.mp3").play()
    if (left.value && right.value != ''){
      left.value.status = "close";
      right.value.status = "close";
      disabledL.value = false;
      disabledR.value = false;
    }
  }

  function answer() {
    new Audio("public/click.mp3").play()
    for(let i of buttons_left.value){
      i.status = 'clear'
    }
    for(let j of buttons_right.value){
      j.status = 'clear'
    }
  }

  function next() { 
    disabledL.value = false
    disabledR.value = false
    ShuffleButton()
    for(let i of buttons_left.value){
      i.status = 'close'
    }
    for(let j of buttons_right.value){
      j.status = 'close'
    }
  }
  
  function shuffle(array) {
    let currentIndex = array.length,
      randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex > 0) {
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex],
        array[currentIndex],
      ];
    }
  
    return array;
  }
  </script>
  
  <style>
  .hide {
    display: none;
  }
  </style>
  