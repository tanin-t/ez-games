<template>
    <v-app>
      <v-main>
        <v-card class="mx-auto" max-width="600" max-height="300">
          <v-img
            class="text-white mx-0"
            height="300"
            src="public/Untitled-2.png"
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
                    style="height: 100px; width: 100px"
                    class="text-white mx-0"
                    rounded="0"
                    @click="OpencardLeft(i)"
                    >{{ i.label }}</v-btn
                  >
  
                  <img
                    v-if="i.status == 'open'"
                    style="height: 100px; width: 100px"
                    :src="i.url"
                  >
             
  
                  <div
                    v-if="i.status == 'clear'"
                    style="height: 100px; width: 100px"
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
                    style="height: 100px; width: 100px"
                    class="text-black mx-0"
                    rounded="0"
                    @click="OpencardRight(i)"
                    >{{ i.label }}</v-btn
                  >
  
                  <img
                    v-if="i.status == 'open'"
                    style="height: 100px; width: 100px"
                    :src="i.url"
                  >
      
  
                  <div
                    v-if="i.status == 'clear'"
                    style="height: 100px; width: 100px"
                  ></div>
                </template>
              </v-col>
            </v-row>
          </v-img>
        </v-card>
        <v-btn @click="next()">Next</v-btn>
      </v-main>
    </v-app>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  const buttons_left = ref(
    shuffle([
      { url: "public/IMG_565.jpg", status: "close" },
      { url: "public/IMG_5640.jpg", status: "close" },
      { url: "public/IMG_5642.jpg", status: "close" },
      { url: "public/IMG_5643.jpg", status: "close" },
      { url: "public/IMG_5644.jpg", status: "close" },
      { url: "public/IMG_5645.jpg", status: "close" },
      { url: "public/IMG_5646.jpg", status: "close" },
      { url: "public/IMG_5650.jpg", status: "close" },
      { url: "public/IMG_5652.jpg", status: "close" },
    ])
  );
  const buttons_right = ref(
    shuffle([
      { url: "public/IMG_565.jpg", status: "close" },
      { url: "public/IMG_5640.jpg", status: "close" },
      { url: "public/IMG_5642.jpg", status: "close" },
      { url: "public/IMG_5643.jpg", status: "close" },
      { url: "public/IMG_5644.jpg", status: "close" },
      { url: "public/IMG_5645.jpg", status: "close" },
      { url: "public/IMG_5646.jpg", status: "close" },
      { url: "public/IMG_5650.jpg", status: "close" },
      { url: "public/IMG_5652.jpg", status: "close" },
    ])
  );
  
  const alphabets = ref(["A", "B", "C", "D", "E", "F", "G", "H", "I"]);
  const numbers = ref(["1", "2", "3", "4", "5", "6", "7", "8", "9"]);
  const left = ref("");
  const right = ref("");
  const disabledL = ref(false);
  const disabledR = ref(false);
  onMounted(() => {
    AddProperty();
  });
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
      if (left.value == right.value) {
        left.value.status = "clear";
        right.value.status = "clear";
        disabledL.value = false;
        disabledR.value = false;
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
      }
    }
  }
  
  function next() {
    left.value.status = "close";
    right.value.status = "close";
    disabledL.value = false;
    disabledR.value = false;
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
  