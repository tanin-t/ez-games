<style scoped>
.red {
  background-color: rgb(246, 89, 89) !important;
}

.green {
  background-color: rgba(114, 174, 24, 0.862) !important;
}

.number {
  border-style: solid;
  border-color: tomato;
  text-align: center;
  padding: 5px;
  margin-top: 20px;
}

.help-button {
  width: 100px;
  height: 69.5px;
  font-size: 30px;
  background-color: rgb(255, 255, 69);
  border-radius: 16px;
}

.show-question {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 16px;
  height: 200px;
  border: 10px solid rgb(222, 215, 75);
  background-color: green;
  margin: 5px;
  color: aliceblue;
  font-size: 35px;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.flex-container > button {
  background-color: #ffff68;
  border-radius: 16px;
  width: 300px;
  margin: 10px;
  text-align: center;
  line-height: 75px;
  font-size: 30px;
}
.score {
  display: inline-block;
  border: 1px solid tomato;
  background-color: tomato;
  border-radius: 16px;
  font-size: 50px;
  width: 100px;
  margin-top: 5px;
  text-align: center;
  color: white;
  padding: 6px;
}
</style>

<template>
  <!-- Total  -->
  <v-row>
    <v-col cols="4"></v-col>
    <v-col cols="4" class="text-center">
      <div class="score">
        {{ count }}
      </div>
    </v-col>
    <v-col cols="4" class="justify-end d-flex align-center">
      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ props }">
          <v-btn
            color=""
            variant="plaint"
            icon="mdi-crown-circle"
            size="x-large"
            class="me-3 text-h4"
            v-bind="props"
          ></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
          <v-card title="Dialog">
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                text="Close Dialog"
                @click="isActive.value = false"
              ></v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
    </v-col>
  </v-row>

  <div v-if="questions.length > 0" id="showQ" class="show-question">
    <div>{{ questions[count].question }}</div>
  </div>
  <div v-if="questions.length > 0" class="flex-container">
    <button :disabled="stop" :class="btn[0]" id="b1" @click="handleBtnClick(1)">
      {{ questions[count].choice1 }}
    </button>
    <button :disabled="stop" :class="btn[1]" id="b2" @click="handleBtnClick(2)">
      {{ questions[count].choice2 }}
    </button>
    <button :disabled="stop" :class="btn[2]" id="b3" @click="handleBtnClick(3)">
      {{ questions[count].choice3 }}
    </button>
    <button :disabled="stop" :class="btn[3]" id="b4" @click="handleBtnClick(4)">
      {{ questions[count].choice4 }}
    </button>
  </div>
  <div class="text-center">
    <v-btn :hidden="next" @click="nextbtn()" color="green">NEXT</v-btn>
    <v-btn :hidden="reset" @click="resetgame()" color="red">reset</v-btn>

    <!-- dialog -->
  </div>
</template>

<script setup>
import { ref } from "vue";
const questions = ref([]);
const count = ref(0);
const dialog = ref(false);
let btn = ref(["", "", "", ""]);
const st = ref("button");
const next = ref(true);
const reset = ref(true);
const stop = ref(false);

function handleBtnClick(studentAns) {
  console.log(btn.value[0] + "disabled");
  const keyAns = questions.value[count.value].answer;
  console.log(keyAns);
  if (keyAns == studentAns) {
    btn.value[studentAns - 1] = "green";
    next.value = false;
  } else {
    btn.value[studentAns - 1] = "red";
    btn.value[keyAns - 1] = "green";
    reset.value = false;
  }
  stop.value = true;
}

function nextbtn() {
  count.value = count.value + 1;
  console.log(count.value);
  stop.value = false;
  btn.value = ["", "", "", ""];
  next.value = true;
}

function resetgame() {
  count.value = 0;
  stop.value = false;
  btn.value = ["", "", "", ""];
  reset.value = true;
}

function checkScore() {}

async function getData() {
  const response = await fetch(
    "http://games.ez-zone.com/api/snippets/data/"
  );

  const data = await response.json();
  console.log("this is data", data);
  questions.value = data;
  console.log(questions.value);
}

getData();
</script>