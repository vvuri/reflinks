<script setup lang="ts">
import CardImg from '../components/CardImg.vue'

</script>

<template>
  <main>
    <div class="cards">
      <CardImg name="Карточка 1"/>
      <CardImg name="Карточка 2"/>
      <CardImg name="Карточка 3"/>
    </div>
  </main>
</template>

<style scoped>
.cards {
  width: 100%;
  display: flex;
  gap: 8px;
}
</style>
