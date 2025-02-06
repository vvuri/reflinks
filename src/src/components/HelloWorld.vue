<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3 className='text-xs text-green-200'>123</h3>
    <div class="bg-sky-100 px-2 py-2">
      <input width="600" size="300" placeholder="put image url" className="rounded-sm">
    </div>
    <button class="rounded-full bg-sky-400 hover:bg-sky-500 px-5 py-2 text-sm">Save changes</button>
  </div>
</template>

<style scoped>
</style>
