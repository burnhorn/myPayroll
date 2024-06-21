<script>
  import { link } from "svelte-spa-router";
  import { authStore } from '../lib/store.js';
  import { onDestroy } from 'svelte';

  export let currentRoute = "/";
  let authDetails = {};

      // autoStore을 구독하여 최신 토큰 값을 얻기
  const unsubscribe = authStore.subscribe(value => {
    authDetails = value;
  });

    // 컴포넌트 기능 끝나면 리소스 제거
    onDestroy(() => {
        unsubscribe();
    });

    function logout() {
      authStore.set({
        access_token: '',
        token_type:'',
        username: '',
      });
    }

</script>

<nav>
  <ul>
    <div>
      <li><a use:link href="/" class="{currentRoute === '/' ? 'active' : ''}">Home</a></li>
      <li><a use:link href="/insurance/calculate">Calculation</a></li>
      <li><a use:link href="/dashboard">DashBoard</a></li>
    </div>
    <div class = "login-right">
      {#if $authStore.username}
      <li ><a use:link href="/" on:click={logout}>LogOut</a></li>
      <li class = "welcome-message"><span>환영합니다. {authDetails.username}님</span></li>
      {:else}
      <li ><a use:link href="/user-login">Login</a></li>
      <li ><a use:link href="/user-singup">Sing Up</a></li>
      {/if}
    </div>
    <!-- 필요한 만큼 링크 추가 -->
  </ul>
</nav>

<style>
  nav {
    background-color: #333;
    padding: 0.1rem;
    padding-right: 2rem;
  }

  ul {
    list-style: none;
    display: flex;
    gap: 1rem;
  }

  div {
    list-style: none;
    display: flex;
    gap: 1rem;
  }

  div.login-right {
    margin-left: auto;
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

  .welcome-message {
    color: white;
    margin-left: auto;
  }

</style>
