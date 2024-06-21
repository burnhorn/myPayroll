<script>
    import { loginUser } from '../../lib/fetch.js';
    import { push } from 'svelte-spa-router'
    import { authStore } from '../../lib/store.js';
      
    let paramas = {
        username : "",
        password : ""
    };
  
    async function postLoginUser(event) {
        event.preventDefault();
        console.log("Submitting login with parameters:", paramas);
      try {
        const loginParams = await loginUser(paramas);
        console.log('Fetched loginparamas data:', loginParams);
        authStore.set(loginParams); // token값 저장
        push('/'); // 루트 route로 이동
      } catch (error) {
        console.error('로그인 중 오류가 발생했습니다:', error);
      }
    }

</script>

<div class = "container">
    <h2 class="login-border">로그인</h2>
    <form method="post">
        <div class = "login-name">
            <label for = "username">사용자 이름</label>
            <input type = "text" class ="form-control" id="username" bind:value="{paramas.username}">
        </div>
        <div class = "login-passowrd">
            <lable for = "password">비밀번호</lable>
            <input type = "text" class="form-control" id="password" bind:value="{paramas.password}">
        </div>
        <button type="submit" class="btn btn-primary" on:click="{postLoginUser}">로그인</button>
    </form>
</div>


<style>
    .login-border {
        display : flex;
        padding : 5px;
        margin : 0;
        width: 100%;
        color: rgb(104, 104, 104);
    }
</style>