<script>
  import NavBar from './Navigation.svelte';
</script>

<NavBar />

<main>
  <slot></slot>
</main>

<style>
  main {
    padding: 2rem;
  }
</style>