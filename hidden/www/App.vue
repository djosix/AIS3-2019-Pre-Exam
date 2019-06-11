<template lang="pug">
  center
    h1(v-if='false') {{ text }}
    h1(v-else) Hidden
</template>

<script>
import getFlag from './flag.js';

export default {
  created() {
    this.text = getFlag();
  }
};
</script>


