<template>
  <v-row>
    <v-col cols="3">
      <v-card class="rounded-xl my-10 ms-5 elevation-10 bg-green-lighten-3">
        <h1 class="d-flex justify-center my-6" style="font-size: 50px">
          player
        </h1>
        <div class="ms-6 pa-3" style="font-size: 40px" v-for="i in new_player">
          {{ i.name }}
        </div>
      </v-card>
    </v-col>
    <v-col cols="9">
      <v-card
        class="rounded-xl ms-3 ma-10 elevation-10 pa-6 bg-green-lighten-2"
      >
        <h1 class="d-flex justify-center my-6" style="font-size: 50px">
          Bingo
        </h1>

        <div class="d-flex justify-center">
          <v-card class="number rounded-xl text-center">{{
            bingo_number
          }}</v-card>
        </div>
        <div class="d-flex justify-center pa-5">
          <v-btn class="mx-2 bg-success" @click="nextnumber(), next()"
            >Next number</v-btn
          >
          <v-btn class="mx-2 bg-error" @click="resetnumber()">reset</v-btn>
        </div>

        <span
          v-for="h in old_number"
          class="rounded-lg elevation-2 ma-1 pa-1"
          style="
            font-size: 40px;
            white-space: nowrap;
            display: inline-block;
            width: 80px;
            height: 65px;
            text-align: center;
            background-color: rgb(255, 171, 60);
          "
          >{{ h }}</span
        >
      </v-card>
    </v-col>
  </v-row>
</template>
<style scoped>
.number {
  font-size: 120px;
  width: 600px;
  background-color: rgb(217, 142, 142);
}
</style>
<script setup>
import { ofetch } from "ofetch";
const bingo_number = ref("");
const old_number = ref([]);
const new_player = ref([]);
async function nextnumber() {
  const run = await ofetch(
    "https://games.ez-zone.com/api/bingo/bingo-number/generate/",
    {
      method: "POST",
    }
  );
  bingo_number.value = run.number;
  old_number.value.push(run.number);
  console.log(run);
}
async function resetnumber() {
  await ofetch("https://games.ez-zone.com/api/bingo/reset-game/", {
    method: "POST",
  });
  bingo_number.value = "";
  old_number.value = [];
  new_player.value = [];
}
async function getPlayer() {
  const player = await ofetch("https://games.ez-zone.com/api/bingo/player/", {
    method: "GET",
  });
  new_player.value = player;
  console.log(new_player.value);
}

function next() {
  new Audio("/next.mp3").play();
}

getPlayer();
</script>
