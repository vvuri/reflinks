<template>
  <router-view />

  <header>
    <h2>Главная</h2>
  </header>

  <main>
    <div class="wrapper">
      <HelloWorld msg="Прототип!" />
    </div>
    <h3>Delete card:</h3>
    <DeleteCard/>
  </main>

</template>

<script setup lang="ts">
import DeleteCard from '../components/DeleteCard.vue'

</script>
