<template>
  <div class="main-container">
    <div class="page-view">
      <div class="sandbox-view-frame-center">
          

        <div class="sandbox-left-frame">
          <!-- TODO -->
          <div class="sandbox-spacer-1"></div>
          <div class="frame22">
            <span class="operations">Operations</span>
            <div class="frame12" @click="handleBooleanNotClick">
              <p class="operation-text">
                Boolean Not
              </p>
              <p class="operation-symbol">
                !
              </p>
            </div>
            <div class="frame12" @click="handleBitwiseNotClick">
              <p class="operation-text" >
                Bit-wise Not
              </p>
              <p class="operation-symbol">
                ~
              </p>
            </div>
            <div class="frame12" @click="handleAddClick">
              <p class="operation-text">
                Add
              </p>
              <p class="operation-symbol">
                +
              </p>
            </div>
            <div class="frame12" @click="handleSubtractClick">
              <p class="operation-text">
                Subtract
              </p>
              <p class="operation-symbol">
                -
              </p>
            </div>
            <div class="frame12" @click="handleAndClick">
              <p class="operation-text">
                And
              </p>
              <p class="operation-symbol" >
                &
              </p>
            </div>
            <div class="frame12" @click="handleOrClick">
              <p class="operation-text">
                Or
              </p>
              <p class="operation-symbol">
                |
              </p>
            </div>
            <div class="frame12" @click="handleXorClick">
              <p class="operation-text">
                XOR
              </p>
              <p class="operation-symbol">
                ^
              </p>
            </div>
            <div class="frame12" @click="handleRightShiftClick">
              <p class="operation-text">
                Right Shift
              </p>
              <p class="operation-symbol">
                >>
              </p>
            </div>
            <div class="frame12" @click="handleLeftShiftClick">
              <p class="operation-text">
                Left Shift
              </p>
              <p class="operation-symbol">
                <<
              </p>
            </div>

          </div>
        </div>

        <div class="sandbox-center-frame">
          <div class="frame21">
            <span class="sandbox-text">Sandbox</span>
          </div>
          <div class="frame23">
            <div class="frame25">
              <span class="var-name">A =</span>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="bool-spacer"></div>
            </div>
            
          </div>


          <div class="frame23">
            <div class="frame25">
              <span class="var-name">B =</span>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="bool-spacer"></div>
            </div>
            
          </div>



          <div class="frame28">
            <span class="compute">Compute</span>
          </div>
          <div class="spacer-center1"></div>
          
          <div class="frame23">
            <div class="frame25">
              <span class="result-name">A | B =</span>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">0</span>
                <div class="bool-underline"></div>
              </div>
              <div class="frame24">
                <span class="bool-text">1</span>
                <div class="bool-underline"></div>
              </div>
              <div class="bool-spacer-long"></div>
            </div>
            
          </div>

          <div class="spacer-center2"></div>
        </div>

        <div class="sandbox-right-frame">
          <div class="sandbox-spacer-1"></div>
          <div class="frame52">
            <span class="operations">Options</span>
            <div class="frame12">
              <p class="options-text">
                Highlight Values
              </p>
              <p class="options-symbol">
                ON
              </p>
            </div>
            <div class="frame12">
              <p class="options-text">
                Show Steps
              </p>
              <p class="options-symbol">
                OFF
              </p>
            </div>
            <div class="frame12">
              <p class="options-text">
                Show Carry
              </p>
              <p class="options-symbol">
                OFF
              </p>
            </div>
            <div class="frame12">
              <p class="options-text">
                Signed
              </p>
              <p class="options-symbol">
                OFF
              </p>
            </div>
            <div class="frame12">
              <p class="options-text">
                Show Integer Value
              </p>
              <p class="options-symbol">
                OFF
              </p>
            </div>

          </div>
          <div class="frame56">
            <span class="feeling-confident">Feeling Confident?</span>
            <span class="try-practice">Try some practice problems</span>
          </div>
        </div>
      </div>

      <div class="sandbox-view-frame-bottom">
        <span class="developed-by">
          Developed by Angelica Bain (dcf3mm) and Paris Phan (auj4yx), 2024
        </span>
      </div>
    </div>
  </div>
</template>





<script>
export default {
  name: 'SandboxScreen',
  methods: {
    //to do
    handleBooleanNotClick() {
      console.log("boolean not clicked");
    },
    handleBitwiseNotClick() {
      console.log('Bitwise Not clicked!');
    },
    handleAddClick() {
      console.log('Test');
    },
    handleSubtractClick() {
      console.log('Click');
    },
    handleAndClick() {
      console.log('Click');
    },
    handleOrClick() {
      console.log('Click');
    },
    handleXorClick() {
      this.$router.push("/");
    },
    handleRightShiftClick() {
      //for later....
    },
    handleLeftShiftClick() {
      //...
    },
  },
};

  //To do!

</script>


<style>
:root {
    --default-font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
      "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
      "Source Han Sans CN", sans-serif;
  }

  .main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    width: 100vw;
    height: 100vh;
    margin: 0;
    padding: 0;
    background: #ffffff;
    overflow: hidden;
  }

  .page-view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%; 
    height: 100%;
  }

  .sandbox-view-frame-center {
      display: flex;
      width: 100%;
      /* flex-direction: column; */
      justify-content: center;
      align-items: center;
      /* gap: 21px; */
      flex: 1 0 0;
      align-self: stretch;
  }

  .sandbox-view-frame-bottom {
      display: flex;
      width: 1440px;
      height: 50px;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 21px;
      flex-shrink: 0;
  }

  .developed-by {
      align-self: stretch;
      color: #CECECE;
      text-align: center;
      font-family: Inter;
      font-size: 16px;
      font-style: normal;
      font-weight: 700;
      line-height: normal;
  }

  .sandbox-spacer-1 {
    height: 100px;
    flex-shrink: 0;
    align-self: stretch;
  }

  .frame22 {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
    flex: 1 0 0;
    align-self: stretch;
  }

  .operations {
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

  
  
  .frame12 {
    display: flex;
    width: 200px;
    align-items: center;
    gap: 10px;
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

  .sandbox-left-frame {
    display: flex;
    width: 294px;
    height: 857px;
    flex-direction: column;
    align-items: flex-end;
  }


  .sandbox-center-frame {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex: 1 0 0;
    align-self: stretch;
  }

  .spacer-center1 {
    flex: 1 0 0;
    align-self: stretch;  
  }

  .spacer-center2 {
    height: 157px;
    align-self: stretch;
  }

  .frame21 {
    display: flex;
    height: 100px;
    justify-content: center;
    align-items: flex-end;
    align-self: stretch;
  }

  .sandbox-text {
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

  .frame23 {
    display: flex;
    height: 100px;
    justify-content: center;
    align-items: flex-end;
    align-self: stretch;
  }

  .frame25 {
    display: flex;
    height: 50px;
    align-items: center;
    gap: 10px;
  }

  .var-name {
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
  .frame24 {
    display: flex;
    width: 35px;
    height: 50px;
    flex-direction: column;
    align-items: flex-start;
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

  .frame28 {
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
  }

  .result-name {
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

  .bool-spacer {
    width: 75px;
    height: 50px;
  }
  .bool-spacer-long {
    width: 125px;
    height: 50px;
  }

  .sandbox-right-frame {
    display: flex;
    width: 294px;
    height: 857px;
    flex-direction: column;
    align-items: flex-end;
  }

  .frame52 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    flex: 1 0 0;
    align-self: stretch;
  }

  .frame56 {
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

  .options-text {
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
  }

  .options-symbol {
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

  