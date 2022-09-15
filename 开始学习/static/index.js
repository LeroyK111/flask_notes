window.addEventListener("load", () => {
  let username = document.querySelector("#username");
  let password = document.querySelector("#password");
  let btn = document.querySelector("#login");

  btn.addEventListener("click", () => {
    if (username.value.length <= 0 || password.value.length <= 0) {
      alert("账号密码不能为空");
      return;
    }

    fetch("http://127.0.0.1:5000/auth", {
      method: "POST",
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
      headers: {
        "Content-Type": "application/json",
        "User-Agent":
          "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
      },
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        alert("登录成功准备跳转!");
      });
  });
});
