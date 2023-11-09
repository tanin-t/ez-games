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
  min-height: 200px;
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
  <div>
    <!-- Total  -->
    <div class="d-flex justify-space-between">
      <div class="w-25"></div>
      <div>
        <div class="score my-3">
          {{ count }}
        </div>
      </div>
      <div class="w-25 d-flex justify-end align-center">
        <v-dialog v-model="dialog" persistent width="500">
          <template v-slot:activator="{ props }">
            <v-btn size="x-large" class="me-3" v-bind="props">
              <v-icon color="amber" class="text-h4">mdi-crown-circle</v-icon>
            </v-btn>
          </template>

          <template v-slot:default="{}">
            <v-card class="pa-3" title="score">
              <v-table>
                <thead>
                  <tr>
                    <th class="text-left" style="width: 100px">No.</th>
                    <th class="text-left">Name</th>
                    <th class="text-left">score</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in rank.score" :key="item">
                    <td>{{ index + 1 }}</td>
                    <td v-if="item.input">
                      <v-text-field
                        label="Enter your name"
                        variant="underlined"
                        v-model="item.name"
                      >
                      </v-text-field>
                    </td>
                    <td v-else>{{ item.name }}</td>
                    <td>{{ item.score }}</td>
                  </tr>
                </tbody>
              </v-table>
              <div class="text-center mt-3">
                <v-btn
                  :hidden="statusBTN"
                  color="red"
                  text="Close"
                  @click="dialog = !dialog"
                ></v-btn>
                <v-btn
                  :hidden="!statusBTN"
                  color="green"
                  text="Save"
                  @click="saveScore()"
                ></v-btn>
              </div>
            </v-card>
          </template>
        </v-dialog>
      </div>
    </div>

    <div id="showQ" class="show-question pa-3">
      <div v-if="questions.length > 0">{{ questions[count].question }}</div>
    </div>
    <div class="flex-container">
      <button
        :disabled="stop"
        :class="btn[0]"
        id="b1"
        @click="handleBtnClick(1)"
      >
        <div v-if="questions.length > 0">
          {{ questions[count].choice1 }}
        </div>
      </button>
      <button
        :disabled="stop"
        :class="btn[1]"
        id="b2"
        @click="handleBtnClick(2)"
      >
        <div v-if="questions.length > 0">
          {{ questions[count].choice2 }}
        </div>
      </button>
      <button
        :disabled="stop"
        :class="btn[2]"
        id="b3"
        @click="handleBtnClick(3)"
      >
        <div v-if="questions.length > 0">
          {{ questions[count].choice3 }}
        </div>
      </button>
      <button
        :disabled="stop"
        :class="btn[3]"
        id="b4"
        @click="handleBtnClick(4)"
      >
        <div v-if="questions.length > 0">
          {{ questions[count].choice4 }}
        </div>
      </button>
    </div>
    <div class="text-center">
      <v-btn :hidden="next" @click="nextbtn()" color="#03A9F4">NEXT</v-btn>
      <v-btn :hidden="finish" @click="checkScore(1)" color="green"
        >FINISH</v-btn
      >
      <v-btn :hidden="reset" @click="checkScore(0)" color="red">reset</v-btn>
    </div>
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
const finish = ref(true);
const stop = ref(false);
const reset = ref(true);
const statusBTN = ref(false);

const rank = ref({});

function handleBtnClick(studentAns) {
  console.log(btn.value[0] + "disabled");
  const keyAns = questions.value[count.value].answer;
  console.log(keyAns);
  if (keyAns == studentAns) {
    btn.value[studentAns - 1] = "green";
    if (count.value + 1 == questions.value.length) {
      finish.value = false;
    } else {
      next.value = false;
    }
  } else {
    btn.value[studentAns - 1] = "red";
    btn.value[keyAns - 1] = "green";
    reset.value = false;
    stop.value = true;
  }
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

function checkScore(point) {
  statusBTN.value = true;
  dialog.value = true;
  const totalScore = point + count.value;
  if (rank.value.score.length > 0 && rank.value.score.length < 6) {
    let dataScore = { name: "", score: totalScore, input: true };
    rank.value.score.forEach((element, index) => {
      console.log(index);
      if (dataScore.score >= element.score) {
        console.log(">");
        let keepScore = element;
        rank.value.score[index] = dataScore;
        dataScore = keepScore;
      }
    });
  } else {
    console.log(rank.value);
    rank.value.score = [
      { name: "", score: totalScore, input: true },
      { name: "", score: 0, input: false },
      { name: "", score: 0, input: false },
      { name: "", score: 0, input: false },
      { name: "", score: 0, input: false },
    ];
    console.log(rank.value);
  }
  finish.value = true;
}

function saveScore() {
  rank.value.score.forEach((element) => {
    element.input = false;
  });
  statusBTN.value = !statusBTN.value;
  console.log(rank.value);
  resetgame();
  postScore();
}

async function getData() {
  const response = await fetch("https://games.ez-zone.com/api/snippets/data/");

  const data = await response.json();
  console.log("this is data", data);
  questions.value = data;
  console.log(questions.value);
}

async function getScore() {
  const response = await fetch("http://games.ez-zone.com/api/snippets/score/");
  const data = await response.json();
  console.log("data", data[0].score);
  if (data[0].score == "") {
    data[0].score = [];
    rank.value = data[0];
    console.log("this is score if", rank.value);
  } else {
    rank.value = data[0];
    console.log("this is score else", rank.value);
  }
}

async function postScore() {
  console.log("Put Score", rank.value.id);
  await fetch(
    `https://games.ez-zone.com/api/snippets/score/${rank.value.id}/update/`,
    {
      method: "PUT",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        score: rank.value.score,
      }),
    }
  );
}

getScore();
getData();
</script>
