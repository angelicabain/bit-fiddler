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

<style src="./HomeScreen.css"></style>




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
</style>