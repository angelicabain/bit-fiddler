<template>
  <div class="main-container" @click="goToSandbox">
    <div class="page-view">
      <div class="view-frame-center">

        <span class="bit-fiddler">{{ currentText }}</span>
        <span class="interactive-learning-tool">
          An Interactive Learning Tool
        </span>
        <div class="spacer"></div>
        <span class="click-anywhere">click anywhere to get started </span>
      </div>
      <div class="view-frame-bottom">
        <span class="developed-by">
          Developed by Angelica Bain (dcf3mm) and Paris Phan (auj4yx), 2024
        </span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "HomeScreen",
  data() {
    return {
      strings: [],
      currentText: "",
      currentIndex: 0,
      // delay: Math.sin(1/12*this.currentIndex - Math.PI/2)*(-66)+131,
      delay: 65,
      canClick: false,
    };
  },
  methods: {
    async fetchStrings() {
      try{ 
        const response = await fetch("/text-animation-bit-fiddler.csv");
        const text = await response.text();
        this.strings = text.split("\n").map((line) => line.trim());
      }
      catch (error) {
        console.error("Error loading string csv", error);
      }
    },
    animateText() {
      if(this.currentIndex < this.strings.length) {
        this.currentText = this.strings[this.currentIndex];
        this.currentIndex++;
        setTimeout(this.animateText, this.delay);
        // if (this.currentIndex > 70){
        //   this.delay = this.delay + 50;
        // }
        if(this.currentIndex > 38){
          this.delay = Math.sin(1/12*this.currentIndex - Math.PI/2)*(-66)+131;
        }
        
        
      }else {
        this.currentText = this.strings[this.strings.length - 1];
      }
      
    },
    goToSandbox() {
      if(this.canClick){
        this.$router.push("/sandbox");
      }
      
    },
    enableClick() {
      this.canClick = true;
    }
  },
  async mounted() {
    await this.fetchStrings();
    if (this.strings.length > 0){
      this.animateText();
    }
    setTimeout(this.enableClick, 5000);
  }
};

</script>

<!-- <style src="./HomeScreen.css"></style>  -->




<!-- FOR FADING IN ANIMATION -->


<style>
.page-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%; 
  height: 100%;
}

.interactive-learning-tool,
.click-anywhere,
.view-frame-bottom {
  opacity: 0;
  animation: fadeInElements 3s ease-in-out forwards;
  animation-delay: 5.5s;
}

@keyframes fadeInElements {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

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
  /* max-width: 1920px; */
  /* max-height: calc(1920px / 16 * 9); */
  /* aspect-ratio: 16 / 9; */
  background-color: #f8f9fa;
}

.view-frame-center {
    display: flex;
    width: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 21px;
    flex: 1 0 0;
}

.bit-fiddler {
    align-self: stretch;
    color: #000;
    text-align: center;
    /* font-family: Inter; */
    font-size: 32px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;

    font-family: "Courier New", Courier, monospace;
    white-space: pre;
    /* letter-spacing: 0.025em; */
}

.interactive-learning-tool {
    align-self: stretch;
    color: #000;
    text-align: center;
    /* font-family: Inter; */
    font-family: "Courier New", Courier, monospace;
    font-size: 24px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

.spacer {
  width: 10%;
  height: 10%;
  background: a
    no-repeat center;
  background-size: cover;
}

.click-anywhere {
    align-self: stretch;
    color: #000;
    text-align: center;
    /* font-family: Inter; */
    font-family: "Courier New", Courier, monospace;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.view-frame-bottom {
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
    /* font-family: "Courier New", Courier, monospace; */
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
}

@media (max-width: 768px) {
  .bit-fiddler {
    font-size: 6vw;
  }

  .interactive-learning-tool {
    font-size: 4vw;
  }

  .click-anywhere {
    font-size: 2vw;
  }

  .spacer {
    width: 20%;
    height: 20%;
  }
}
</style>