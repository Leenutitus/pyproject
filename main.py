from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
foods={'user1':{'country':'indian','dishes':'three','token_no':1},
'user2':{'country':'russian','dishes':'two','token_no':2},
'user3':{'country':'japanese','dishes':'four','token_no':3}}
class Users(BaseModel):
country: str
dishes: str
token_no: int



'''@app.get('/users')
async def get_users():
food_list = list(foods.values())
return food_list'''

@app.get("/user1/{country}")
async def get_users_path(country: str):
return foods.get(country)

@app.get('/users')
async def get_users_query(limit: int=20):
food_list = list(foods.values())
return food_list[:limit]
@app.post('/users')
def create_user(user: Users):
country =user.country
foods[country]=user.dict()
return {'message':f'Sucessfulley created user'}
@app.delete('/users/{country}')
def delete_user(country: str):
del foods[country]
return{'message':f'Sucessfulley deleted user:{country}'}
@app.put('/users')
def update_user(user: Users):
country=user.country
foods[country]=user.dict()
return{'message':f'Sucessfulley updated user:{country}'}
@app.patch('/users')
def update_user_partial(user: Users):
country=user.country
foods[country].update(user.dict(exclude_unset=True))
return {'message':f'Sucessfullay updated user:{country}'}
