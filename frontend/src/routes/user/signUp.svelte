<script>
    import { signUpUser } from '../../lib/fetch.js';
    import { push } from 'svelte-spa-router'
      
    let paramas = {
        user_name : "",
        password1 : "",
        password2 : "",
        email : "",
    };
  
    async function postSignUpUser(event) {
        event.preventDefault();
        console.log("Submitting signup form with parameters:", paramas);
      try {
        const signupParams = await signUpUser(paramas);
        console.log('Fetched signupParams data:', signupParams);
        push('/'); // 루트 / 이동
      } catch (error) {
        console.error('로그인 중 오류가 발생했습니다:', error);
      }
    }

</script>

<div class = "container">
    <h2 class="signup-border">로그인</h2>
    <form method="post">
        <div class = "signup-name">
            <label for = "username">사용자 이름</label>
            <input type = "text" class ="form-control" id="username" bind:value="{paramas.user_name}">
        </div>
        <div class = "signup-passowrd">
            <div>
            <lable for = "password1">비밀번호</lable>
            <input type = "text" class="form-control" id="password1" bind:value="{paramas.password1}">
            </div>
            <div>
            <lable for = "password2">비밀번호 확인</lable>
            <input type = "text" class="form-control" id="password2" bind:value="{paramas.password2}">
            </div> 
            <div>
            <lable for = "email">Email</lable>
            <input type = "text" class="form-control" id="email" bind:value="{paramas.email}">
            </div>
        </div>
        <button type="submit" class="btn btn-primary" on:click="{postSignUpUser}">회원가입</button>
    </form>
</div>


<style>
    .signup-border {
        display : flex;
        padding : 5px;
        margin : 0;
        width: 100%;
        color: rgb(104, 104, 104);
    }
</style>