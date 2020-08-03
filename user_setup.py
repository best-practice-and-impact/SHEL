from app import db
from app.models import User, Post
from datetime import datetime

if len(User.query.all()) == 0:
    print("Creating Admin User")
    u = User(username = "Admin", email = "admin@admin.com", is_admin = "True")
    u.set_password("123456")
    db.session.add(u)
    db.session.commit()
else:
    print("User tables already setup")

if len(Post.query.all()) < 3:
    remaining_posts_to_add = 3 - len(Post.query.all())
    for i in range(remaining_posts_to_add):
        p = Post(body = "Example Event " + str(i+1), 
                location = "Example Location " + str(i+1),
                date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                )
        db.session.add(p)
        db.session.commit()
        print("Created example event")
else:
    print("Events already created")