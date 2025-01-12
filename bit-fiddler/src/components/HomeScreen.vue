<template>
  <div class="main-container" @click="goToSandbox">
    <div class="page-view">
      <div class="view-frame-center">

        <span class="bit-fiddler-main-text">{{ currentText }}</span>
        <span class="interactive-learning-tool">
          An Interactive Learning Tool
        </span>
        <div class="spacer-10"></div>
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

<!-- Scripts -->
<script>

export default {
  name: "HomeScreen",
  data() {
    return {
      strings: [],
      currentText: "",
      currentIndex: 0,
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
        if (this.currentIndex > 73){
          this.delay = this.delay + 50;
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

<!-- General -->
<style scoped>
.view-frame-center {
    display: flex;
    width: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 21px;
    flex: 1 0 0;
}

</style>

<!-- Specific Elements -->
<style scoped>

.interactive-learning-tool,
.click-anywhere,
.view-frame-bottom {
  opacity: 0;
  animation: fadeInElements 3s ease-in-out forwards;
  animation-delay: 5s;
}

@keyframes fadeInElements {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.bit-fiddler-main-text {
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
    font-family: Inter;
    font-size: 24px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

.spacer-10 {
  width: 10%;
  height: 10%;
  background-size: cover;
}

.click-anywhere {
    align-self: stretch;
    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

@media (max-width: 768px) {
  .bit-fiddler-main-text {
    font-size: 6vw;
  }

  .interactive-learning-tool {
    font-size: 4vw;
  }

  .click-anywhere {
    font-size: 2vw;
  }

  .spacer-10 {
    width: 20%;
    height: 20%;
  }
}

</style>