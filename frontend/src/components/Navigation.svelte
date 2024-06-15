<script>
  import { link } from "svelte-spa-router";
  export let currentRoute = "/";
</script>

<nav>
  <ul>
    <li><a use:link href="/" class="{currentRoute === '/' ? 'active' : ''}">Home</a></li>
    <li><a use:link href="/insurance/calculate">Calculation</a></li>
    <li><a use:link href="/user_login">Login</a></li>
    <!-- 필요한 만큼 링크 추가 -->
  </ul>
</nav>

<style>
  nav {
    background-color: #333;
    padding: 0.1rem;
  }

  ul {
    list-style: none;
    display: flex;
    gap: 1rem;
  }

  li {
    margin: 0;
  }

  a {
    color: white;
    text-decoration: none;
  }

  .active {
    font-weight: bold;
  }
</style>
