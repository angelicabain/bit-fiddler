<template>
  <div class="main-container">
    <div class="page-view">
      <div class="view-frame-center">
          
        <!-- Left Frame -->
        <div class="left-frame">
          <!-- TODO -->
          <div class="spacer-1-8th"></div>
          <div class="operations-frame">
            <span class="side-panel-header-text">Operations</span>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'booleannot' }" @click="handleBooleanNotClick">
              <p class="operation-text">
                Boolean Not
              </p>
              <p class="operation-symbol">
                !
              </p>
            </div>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'bitwisenot' }" @click="handleBitwiseNotClick">
              <p class="operation-text" >
                Bit-wise Not
              </p>
              <p class="operation-symbol">
                ~
              </p>
            </div>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'add' }" @click="handleAddClick">
              <p class="operation-text">
                Add
              </p>
              <p class="operation-symbol">
                +
              </p>
            </div>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'subtract' }" @click="handleSubtractClick">
              <p class="operation-text">
                Subtract
              </p>
              <p class="operation-symbol">
                -
              </p>
            </div>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'and' }" @click="handleAndClick">
              <p class="operation-text">
                And
              </p>
              <p class="operation-symbol" >
                &
              </p>
            </div>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'or' }" @click="handleOrClick">
              <p class="operation-text">
                Or
              </p>
              <p class="operation-symbol">
                |
              </p>
            </div>
            <div class="operation-frame" :class="{ underlined: operationSelected === 'xor' }" @click="handleXorClick">
              <p class="operation-text">
                XOR
              </p>
              <p class="operation-symbol">
                ^
              </p>
            </div>
            <div class="operation-frame" @click="handleRightShiftClick">
              <p class="operation-text">
                Right Shift
              </p>
              <p class="operation-symbol">
                >>
              </p>
            </div>
            <div class="operation-frame" @click="handleLeftShiftClick">
              <p class="operation-text">
                Left Shift
              </p>
              <p class="operation-symbol">
                <<
              </p>
            </div>

          </div>
        </div>

        <!-- Center Frame -->
        <div class="center-frame">
          <div class="center-top-frame">
            <span class="sandbox-main-text">Sandbox</span>
          </div>
          <div class="center-binary-frame">
            <div class="binary-frame">
              <span class="binary-var-text">A =</span>
              <div class="bool-frame" v-for="(bit, index) in inputA" :key="index">
                <span class="bool-text">{{ bit }}</span>
                <div class="bool-underline"></div>
              </div>
              <div class="binary-spacer"></div>
            </div>
            
          </div>


          <div class="center-binary-frame" >
            <div class="binary-frame" v-if="showBFrame">
              <span class="binary-var-text">B =</span>
              <div class="bool-frame" v-for="(bit, index) in inputB" :key="index">
                <span class="bool-text">{{ bit }}</span>
                <div class="bool-underline"></div>
              </div>
              <div class="binary-spacer"></div>
            </div>
          </div>



          <div class="center-compute-frame"  @click="handleComputeClick">
            <span class="compute">Compute</span>
          </div>
          <div class="spacer-25"></div>
          
          <div class="center-binary-frame">
            <div class="binary-frame">
              <span class="binary-result-text"> {{ resultText }} </span>
              <div class="bool-frame" v-for="(bit, index) in binaryNumbers" :key="index">
                <span class="bool-text">{{ bit }}</span>
                <div class="bool-underline"></div>
              </div>
              <div class="binary-spacer"></div>
            </div>
            
          </div>

        </div>

        <!-- Right Frame -->
        <div class="right-frame">
          <div class="spacer-1-8th"></div>
          <div class="options-frame">
            <span class="side-panel-header-text">Options</span>
            <div class="option-frame">
              <p class="option-text">
                Highlight Values
              </p>
              <p class="option-symbol">
                ON
              </p>
            </div>
            <div class="option-frame">
              <p class="option-text">
                Show Steps
              </p>
              <p class="option-symbol">
                OFF
              </p>
            </div>
            <div class="option-frame">
              <p class="option-text">
                Show Carry
              </p>
              <p class="option-symbol">
                OFF
              </p>
            </div>
            <div class="option-frame">
              <p class="option-text">
                Signed
              </p>
              <p class="option-symbol">
                OFF
              </p>
            </div>
            <div class="option-frame">
              <p class="option-text">
                Show Integer Value
              </p>
              <p class="option-symbol">
                OFF
              </p>
            </div>

          </div>
          <div class="practice-link-frame">
            <span class="feeling-confident">Feeling Confident?</span>
            <span class="try-practice">Try some practice problems</span>
          </div>
        </div>
      </div>

      <div class="view-frame-bottom">
        <span class="developed-by">
          Developed by Angelica Bain (dcf3mm) and Paris Phan (auj4yx), 2024
        </span>
      </div>
    </div>
  </div>
</template>

<!-- Scripts -->
<script>
export default {
  name: 'SandboxScreen',
  data() {
    return {
      windowWidth: window.innerWidth,
      windowHeight: window.innerHeight,
      inputA: ['0', '0', '0', '1', '0', '1', '1', '0'],
      inputB: ['0', '0', '0', '0', '1', '0', '0', '1'],
      binaryNumbers: ['0', '0', '0', '0', '0', '0', '0', '0'],
      resultText: "A | B =",
      isOperationSelected: false,
      operationSelected: "",
    };
  },
  computed: {
    showBFrame() {
      return this.operationSelected !== "booleannot" && this.operationSelected !== "bitwisenot";
    },
  },
  methods: {
    //to do
    handleComputeClick()
    {
      //no op selected
      this.binaryNumbers.fill('-1');

      //Boolean Not
      if(this.operationSelected === "booleannot") {
        this.resultText = "!A =";

        const isAllZero = this.inputA.every(value => value === '0');

        if (isAllZero) {
          this.binaryNumbers = ['0', '0', '0', '0', '0', '0', '0', '1'];
        } else {
          this.binaryNumbers = ['0', '0', '0', '0', '0', '0', '0', '0'];
        }
      }
      //Bitwise Not
      else if(this.operationSelected === "bitwisenot") {
        this.resultText = "~A =";
        this.binaryNumbers = this.inputA.map(value => (value === '1' ? '0' : '1'));
      }


      // Add
      else if (this.operationSelected === "add") {
        this.resultText = "A + B =";
        const sum = (parseInt(this.inputA.join(''), 2) + parseInt(this.inputB.join(''), 2)).toString(2);
        this.binaryNumbers = sum.padStart(8, '0').split('');
      }

      // Subtract
      else if (this.operationSelected === "subtract") {
        this.resultText = "A - B =";
        const difference = (parseInt(this.inputA.join(''), 2) - parseInt(this.inputB.join(''), 2)).toString(2);
        this.binaryNumbers = difference.padStart(8, '0').split('');
      }

      // And
      else if (this.operationSelected === "and") {
        this.resultText = "A & B =";
        this.binaryNumbers = this.inputA.map((bit, index) => (bit === '1' && this.inputB[index] === '1' ? '1' : '0'));
      }

      // Or
      else if (this.operationSelected === "or") {
        this.resultText = "A | B =";
        this.binaryNumbers = this.inputA.map((bit, index) => (bit === '1' || this.inputB[index] === '1' ? '1' : '0'));
      }

      // Xor
      else if (this.operationSelected === "xor") {
        this.resultText = "A ^ B =";
        this.binaryNumbers = this.inputA.map((bit, index) => (bit === this.inputB[index] ? '0' : '1'));
      }

    },
    handleBooleanNotClick() {
      if (this.operationSelected === 'booleannot') {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "booleannot";
      }
    },
    handleBitwiseNotClick() {
      if (this.operationSelected === 'bitwisenot') {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "bitwisenot";
      }
    },
    handleAddClick() {
      if (this.operationSelected === "add") {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "add";
      }
    },

    handleSubtractClick() {
      if (this.operationSelected === "subtract") {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "subtract";
      }
    },

    handleAndClick() {
      if (this.operationSelected === "and") {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "and";
      }
    },

    handleOrClick() {
      if (this.operationSelected === "or") {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "or";
      }
    },

    handleXorClick() {
      if (this.operationSelected === "xor") {
        this.isOperationSelected = false;
        this.operationSelected = "";
      } else {
        this.isOperationSelected = true;
        this.operationSelected = "xor";
      }
    },
    handleRightShiftClick() {
      //for later....
    },
    handleLeftShiftClick() {
      //...
    },
    updateWindowSize() {
      this.windowWidth = window.innerWidth;
      this.windowHeight = window.innerHeight;
    },
  },
  mounted() {
    window.addEventListener('resize', this.updateWindowSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWindowSize);
  }
};

  //To do!

</script>

<!-- General -->
<style scoped>
  .view-frame-center {
      display: flex;
      width: 100%;
      /* flex-direction: column; */
      justify-content: center;
      align-items: center;
      /* gap: 21px; */
      flex: 1 0 0;
      align-self: stretch;
  }


  .side-panel-header-text {
    display: flex;
    width: 200px;
    height: 50px;
    flex-direction: column;
    justify-content: center;
    color: #000;
    font-family: Inter;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: underline;
    text-decoration-style: solid;
    text-decoration-skip-ink: auto;
    text-decoration-thickness: auto;
    text-underline-offset: auto;
    text-underline-position: from-font;
  }


</style>

<!-- Center Frame -->
 <style scoped>



  .center-frame {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    justify-content: flex-sart;
    align-items: flex-start;
    height: 100%;
  }

  .center-top-frame {
    display: flex;
    height: 12.5%;
    justify-content: center;
    align-items: flex-end;
    align-self: stretch;
  }

  .sandbox-main-text {
    display: flex;
    width: 280px;
    height: 50px;
    flex-direction: column;
    justify-content: center;

    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 32px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }

  .center-binary-frame {
    display: flex;
    height: 100px;
    justify-content: center;
    align-items: flex-end;
    align-self: stretch;
  }

  .binary-frame {
    display: flex;
    height: 50px;
    align-items: center;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .binary-var-text {
    display: flex;
    width: 75px;
    flex-direction: column;
    justify-content: center;
    align-self: stretch;

    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 32px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }

  .bool-frame {
    display: flex;
    width: 35px;
    height: 50px;
    flex-direction: column;
    align-items: center;
  }

  .bool-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1 0 0;
    align-self: stretch;

    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 48px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }

  .bool-underline {
    height: 3px;
    flex-shrink: 0;
    align-self: stretch;

    border-radius: 3px;
    background: #666;
  }

  .center-compute-frame {
    display: flex;
    height: 100px;
    padding: 10px;
    justify-content: center;
    align-items: center;
    gap: 10px;
    align-self: stretch;
  }

  .compute {
    display: flex;
    width: 400px;
    height: 30px;
    flex-direction: column;
    justify-content: center;

    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: underline;
    text-decoration-style: solid;
    text-decoration-skip-ink: auto;
    text-decoration-thickness: auto;
    text-underline-offset: auto;
    text-underline-position: from-font;
    cursor: pointer;
  }


  .binary-result-text {
    display: flex;
    width: 125px;
    flex-direction: column;
    justify-content: center;
    align-self: stretch;

    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 32px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }

  .binary-spacer {
    width: 75px;
    height: 50px;
  }
  .binary-spacer-long {
    width: 125px;
    height: 50px;
  }

  @media (max-width: 768px) {
    .left-frame,
    .right-frame {
      display: none; 
    }

    .center-frame {
      padding: 20px;
    }
  }

  @media (min-width: 1200px) {
    .left-frame,
    .right-frame {
      flex: 1 1 15%;
    }

    .center-frame {
      flex: 1 1 70%;
    }
  }

</style>


<!-- Left Frame -->
 <style scoped>

  .left-frame,
  .right-frame {
    flex: 1 1 20%; 
    min-width: 200px; 
    max-width: 300px; 
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }

  .operations-frame,
  .options-frame {
    flex: 1;
    width: 100%;
  }

  .operations-frame {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
    flex: 1 0 0;
    align-self: stretch;
  }


  .operation-frame {
    display: flex;
    width: 200px;
    align-items: center;
    gap: 10px;
  }

  .operation-frame.underlined {
    text-decoration: underline;
    font-weight: bold;
  }

  .operation-text {
    display: flex;
    width: 150px;
    height: 25px;
    flex-direction: column;
    justify-content: flex-end;
    flex-shrink: 0;

    color: #000;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    cursor: pointer;
  }

  .operation-text:hover {
    text-decoration: underline;
  }


  .operation-symbol {
    display: flex;
    height: 25px;
    flex-direction: column;
    justify-content: flex-end;
    flex: 1 0 0;

    color: #000;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }

</style>

<!-- Right Frame -->
<style scoped>

  /* .right-frame {
    display: flex;
    width: 294px;
    height: 857px;
    flex-direction: column;
    align-items: flex-end;
  } */

  .options-frame {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    flex: 1 0 0;
    align-self: stretch;
  }

  .practice-link-frame {
    display: flex;
    height: 157px;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    flex-shrink: 0;
    align-self: stretch;
  }

  .feeling-confident {
    display: flex;
    height: 75px;
    flex-direction: column;
    justify-content: flex-end;
    flex-shrink: 0;
    align-self: stretch;

    color: #000;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }

  .try-practice {
    display: flex;
    height: 20px;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;
    align-self: stretch;

    color: #000;
    font-family: Inter;
    font-size: 14px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: underline;
    text-decoration-style: solid;
    text-decoration-skip-ink: auto;
    text-decoration-thickness: auto;
    text-underline-offset: auto;
    text-underline-position: from-font;
  }
  .option-frame {
    display: flex;
    width: 200px;
    align-items: center;
    gap: 10px;
  }

  .option-text {
    display: flex;
    width: 150px;
    height: 25px;
    flex-direction: column;
    justify-content: flex-end;
    flex-shrink: 0;

    color: #000;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    cursor: pointer;
  }



  .option-symbol {
    display: flex;
    height: 25px;
    flex-direction: column;
    justify-content: flex-end;
    flex: 1 0 0;

    color: #000;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: underline;
    text-decoration-style: solid;
    text-decoration-skip-ink: auto;
    text-decoration-thickness: auto;
    text-underline-offset: auto;
    text-underline-position: from-font;
  }

</style>
