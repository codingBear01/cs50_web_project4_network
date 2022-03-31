document.addEventListener('DOMContentLoaded', () => {
  const postEditBtns = document.querySelectorAll('.post_edit_btn');

  postEditBtns.forEach((btn) => {
    btn.onclick = () => {
      const postDelBtn = document.querySelector('.post_del_btn');
      const postBtnDivider = document.querySelector('.post_button_divider');

      btn.style.display = 'none';
      postDelBtn.style.display = 'none';
      postBtnDivider.style.display = 'none';

      let postContentDiv = document.querySelector(
        `.post_content_div${btn.dataset.postid}`
      );

      postContentDiv.innerHTML = `
      <form class="post_edit_form">
        <div>
            <textarea class="post_edit_textarea">
                ${postContentDiv.innerHTML}
            </textarea>
        </div>
        <input type="submit" value="Save" />
      </form>
      `;

      const postEditForm = document.querySelector('.post_edit_form');

      postEditForm.onsubmit = () => {
        const postContent = document.querySelector('.post_edit_textarea').value;
        const postID = btn.dataset.postid;

        fetch('/postedit', {
          method: 'PUT',
          body: JSON.stringify({
            postContent: postContent,
            postID: postID,
          }),
        })
          .then((response) => response.json())
          .then((result) => {
            if (result.error) {
              console.log(`Error editing post: ${result.error}`);
            } else {
              console.log(result.message);
              postContentDiv.innerHTML = postContent;
              console.log(postContent.innerHTML);
              btn.style.display = 'block';
              postDelBtn.style.display = 'block';
              postBtnDivider.style.display = 'block';
            }
          })
          .catch((err) => {
            console.log(err);
          });
        return false;
      };
    };
  });
});
