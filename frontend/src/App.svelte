<script>
    async function getQuestionList() {
        const res = await fetch("http://127.0.0.1:8000/api/insurance/rates");
        const json = await res.json();

        if (res.ok) {
            return json.message;
        }
        else {
            alert("error");
        }
    }

    let promise = getQuestionList();
</script>>

{#await Promise}
<p>Process Waiting</p>
{:then message}
<h1>{meassage}</h1>
</await>