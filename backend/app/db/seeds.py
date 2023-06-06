print('Seeding database with 100 users, 100 products, and 100 comments')
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import random
import string
import os
env_var = os.environ

# SQLAlchemy >= 1.4 deprecated the use of `postgres://` in favor of `postgresql://`
# for the database connection url
database_url = env_var['DATABASE_URL'].replace("postgres://", "postgresql://")

engine = create_engine(database_url, echo=False)

user_insert_statement = text("""INSERT INTO users(username, email, salt, bio, hashed_password) VALUES(:username, :email, :salt, :bio, :hashed_password)""")
select_last_user_id = text("""SELECT * FROM users ORDER BY id DESC LIMIT 1""")
item_statement = text("""INSERT INTO items(slug, title, description, seller_id) VALUES(:slug, :title, :description, :seller_id)""")
select_last_item = text("""SELECT * FROM items ORDER BY id DESC LIMIT 1""")
comment_statement = text("""INSERT INTO comments(body, seller_id, item_id) VALUES(:body, :seller_id, :item_id)""")

letters = string.ascii_lowercase

def create_user_and_item(con):
  random_generator = lambda: ''.join(random.choice(letters) for i in range(10))
  random_username = random_generator()
  random_slug = lambda: ''.join(f'{random_generator()}_{random_generator()}_{random_generator()}')
  user = {
    'username': random_username,
    'email': f'{random_username}@mail.com',
    'salt': 'abc',
    'bio': 'bio',
    'hashed_password': '12345689',
  }

  con.execute(user_insert_statement, **user)

  result = con.execute(select_last_user_id)

  generated_user_id = None
  for row in result:
    generated_user_id = row['id']

  item = {
    'slug': random_slug(),
    'title': 'title',
    'description': ' description',
    'seller_id': generated_user_id,
    'image': 'placeholder.png'
  }

  con.execute(item_statement, **item)

  result = con.execute(select_last_item)
  generated_item_id = None
  for row in result:
    generated_item_id = row['id']

  comment = {
     'body': 'comment! :)',
     'seller_id': generated_user_id,
     'item_id': generated_item_id
  }

  con.execute(comment_statement, **comment)

with engine.connect() as con:
    for _ in range(101):
        create_user_and_item(con)
