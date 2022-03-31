document.addEventListener('DOMContentLoaded', () => {
  const commentTxt = document.querySelectorAll('.comment_textarea');
  const commentSubmitBtns = document.querySelectorAll('.comment_submit_btn');

  commentTxt.forEach((textarea) => {
    textareaHandler(textarea);
  });

  commentSubmitBtns.forEach((submitBtn) => {
    submitBtn.disabled = true;
  });

  function textareaHandler(textarea) {
    textarea.onkeyup = () => {
      if (textarea.value.trim().length > 0) {
        commentSubmitBtns.forEach((submitBtn) => {
          submitBtn.disabled = false;
        });
      } else {
        commentSubmitBtns.forEach((submitBtn) => {
          submitBtn.disabled = true;
        });
      }
    };
  }
});
