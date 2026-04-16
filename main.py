from fastapi import Body, FastAPI
app = FastAPI()

#requests Get Method URL
@app.get("/")
def root():
    return {"message": "Home of API"}

@app.get("/posts")
def get_posts():
    return {"message": "Get somes posts"}

@app.post("/creatposts")
def create_posts(payload: dict = Body(...)):
    print (payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}