# LAB-ORM-1


## Using what you learned , Create a Blog website called `Blogger` . Has the following pages:
- A homepage : displays the lates posts (Post title, content, date & time published) .
- A page to add new posts.


### To Acheive that, you need to create model `Post` , it should have the following attributes :
- title : char field (max 2048)
- content : text field.
- is_published : boolean field, default is True.
- published_at : datetime field, default is now.

### Design & Layout:
  - Make sure you use Templates & Templates inheritance to unify the look of the website.
  - Make sure to use static files if needed, and dynamic URL resolving when linking to your pages.
  - Generally use best practices (what you learned in previous lessons).
  - It is up to you how you design it. Use whatever means you need (colors, icons, logo, images, fonts, etc.) .