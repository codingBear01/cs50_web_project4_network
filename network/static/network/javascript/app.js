document.addEventListener('DOMContentLoaded', () => {
  // Post Like
  const postLikeButton = document.querySelectorAll('.post_like');

  postLikeButton.forEach((element) => {
    postLikeHandler(element);
  });

  function postLikeHandler(element) {
    element.addEventListener('click', () => {
      const postID = element.getAttribute('post_id');
      const postIsLiked = element.getAttribute('post_is_liked');
      const postLikeCount = element.querySelector(`#post_count_${postID}`);
      const postLikeHeart = element.querySelector(`#post_heart_${postID}`);

      const form = new FormData();
      form.append('postID', postID);
      form.append('postIsLiked', postIsLiked);

      fetch('/postLike', {
        method: 'POST',
        body: form,
      })
        .then((response) => response.json())
        .then((response) => {
          if (response.status === 201) {
            if (response.postIsLiked === 'yes') {
              element.setAttribute('post_is_liked', 'yes');
              postLikeHeart.innerText = '❤';
            } else {
              element.setAttribute('post_is_liked', 'no');
              postLikeHeart.innerText = '🤍';
            }
            postLikeCount.textContent = response.postLikeCount;
          }
        });
    });
  }

  // Comment Like
  const commentLikeButton = document.querySelectorAll('.comment_like');

  commentLikeButton.forEach((element) => {
    commentLikeHandler(element);
  });

  function commentLikeHandler(element) {
    element.addEventListener('click', () => {
      const commentID = element.getAttribute('comment_id');
      const commentIsLiked = element.getAttribute('comment_is_liked');
      const commentLikeCount = element.querySelector(
        `#comment_count_${commentID}`
      );
      const commentLikeHeart = element.querySelector(
        `#comment_heart_${commentID}`
      );

      const form = new FormData();
      form.append('commentID', commentID);
      form.append('commentIsLiked', commentIsLiked);

      fetch('/commentLike', {
        method: 'POST',
        body: form,
      })
        .then((response) => response.json())
        .then((response) => {
          if (response.status === 201) {
            if (response.commentIsLiked === 'yes') {
              element.setAttribute('comment_is_liked', 'yes');
              commentLikeHeart.innerText = '❤';
            } else {
              element.setAttribute('comment_is_liked', 'no');
              commentLikeHeart.innerText = '🤍';
            }
            commentLikeCount.textContent = response.commentLikeCount;
          }
        });
    });
  }
});
