<template>
  <v-dialog v-model="dialog" width="400px">
    <v-card class="rounded-lg pa-6 py-10 elevation-10">
      <h1 class="py-2">Enter your name</h1>
      <v-text-field label="Label" v-model="name"></v-text-field>
      <v-btn color="success" @click="(dialog = false), createName(name)"
        >Next</v-btn
      >
    </v-card>
  </v-dialog>

  <div class="d-flex justify-center align-center pt-16">
    <v-card
      class="rounded-xl py-2 pa-1 pb-6 elevation-10 bg-success"
      width="400px"
      height="auto"
    >
      <h1 class="d-flex justify-center my-4">{{ name }}</h1>

      <v-sheet
        class="d-flex align-content-start flex-wrap justify-center bg-success rounded-lg"
        min-height="200"
      >
        <v-sheet v-for="(n, index) in nums" :key="n">
          <v-btn
            class="num"
            :class="n.color"
            @click="checkNum(n.value, index)"
            >{{ n.value }}</v-btn
          >
        </v-sheet>
      </v-sheet>
    </v-card>
  </div>
</template>
<script setup>
import { ofetch } from "ofetch";
import { ref } from "vue";
const name = ref("");
const nums = ref([]);
const dialog = ref(true);
function players() {
  nums.value = [];
  let i = 0;
  while (i < 16) {
    let num = Math.floor(Math.random() * 100);

    if (!nums.value.map((x) => x.value).includes(num)) {
      nums.value.push({
        value: num,
        color: "",
      });
      i += 1;
    }
  }
}

function textToSpeech(text) {
  const synth = window.speechSynthesis;
  const msg = new SpeechSynthesisUtterance();
  msg.text = text;
  //   msg.voice = getSelectedVoice();

  synth.speak(msg);
}
async function checkNum(n, index) {
  const check = await ofetch(
    "https://games.ez-zone.com/api/bingo/bingo-number/check/",
    {
      method: "POST",
      body: { number: n },
    }
  );
  console.log(check);

  if (check.ok == true) {
    nums.value[index].color = "correct";
    new Audio("/green_2.mp3").play();
  } else {
    nums.value[index].color = "";
    new Audio("/wrong.mp3").play();
  }
}

function createName(name) {
  ofetch("https://games.ez-zone.com/api/bingo/player/", {
    method: "POST",
    body: { name: name },
  });
}

onMounted(() => {
  players();
});
</script>

<style scoped>
.num {
  width: 70px;
  height: 70px !important;
  border-radius: 10%;
  margin: 6px;
  font-size: 45px !important;
  color: #000000;
  background-color: rgba(0, 0, 0, 0.2);
}
.correct {
  background-color: #53ac65;
  color: black;
}
</style>
