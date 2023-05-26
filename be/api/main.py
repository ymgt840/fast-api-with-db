from fastapi import FastAPI
from db import session
from model import TestUserTable, TestUser
from typing import Optional

app = FastAPI()

#　ユーザー情報一覧取得
@app.get("/test_users")
def get_user_list():
    users = session.query(TestUserTable).all()
    return users


# ユーザー情報取得(id指定)
@app.get("/test_users/{user_id}")
def get_user(user_id: int):
    user = session.query(TestUserTable).\
        filter(TestUserTable.id == user_id).first()
    return user


# ユーザ情報登録
@app.post("/test_users")
def post_user(user: TestUser):
    db_test_user = TestUser(name=user.name,
                            email=user.email)
    session.add(db_test_user)
    session.commit()


# ユーザ情報更新
@app.put("/test_users/{user_id}")
def put_users(user: TestUser, user_id: int):
    target_user = session.query(TestUserTable).\
        filter(TestUserTable.id == user_id).first()
    target_user.name = user.name
    target_user.email = user.email
    session.commit()

# パスパラメータ
@app.get("/countries/{country_name}")
def get_country_name(country_name: str): #　Pydantic が実行している
    return {'country_name': country_name}

# クエリパラメータ
@app.get("/foods/")
def get_foods(food_name: str = 'pizza', food_no: int = 1):
    return {
        'name': food_name,
        'no': food_no
    }

# パス & クエリ
@app.get("/sports/{team_name}")
def get_sports_team(team_name: str, city_name: str = 'chicago'):
    return {
        'name': team_name,
        'city': city_name
    }

@app.get("/tests/")
def get_sports_team(test_name: Optional[str] = None, test_no: Optional[str] = 'chicago'):
    return {
        'name': test_name,
        'city': test_no
    }

