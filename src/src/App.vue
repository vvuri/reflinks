<template>
  <p><strong>Текущий путь маршрута:</strong> {{ $route.fullPath }}</p>
  <nav>
    <RouterLink to="/">Go to Home </RouterLink>
    <RouterLink to="/cards">Go to Arhive </RouterLink>
    <RouterLink to="/edit/1">Go to Edit 1 </RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>


