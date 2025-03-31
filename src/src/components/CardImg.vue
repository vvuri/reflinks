<script setup lang="ts">
defineProps<{
  name: string
}>()
</script>

<template>
  <div class="wrapper">
    <div class="flex flex-col gap-2 sm:flex-row">
      <h2>{{ name }}</h2>
      <p>Some context</p>
    </div>
</div>
</template>

<style scoped>
.wrapper {
  width: 400px;
  height: 200px;
  background-color: aqua;
}
</style>
