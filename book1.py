from fastapi import FastAPI

app = FastAPI()
Books=[
    {'title':'One','author':'Author one','category':'one'},
    {'title':'Two','author':'Author one','category':'one'},
    {'title': 'Three', 'author': 'Author one', 'category': 'one'},

]

@app.get("/greet")
async def wish():
    return {"Hello Divya. How are you"}

@app.get('/Books')
async def books():
    return Books

@app.get('/Books/One')
async def get_book():
    for book in Books:
        if book['title']=='One':
            return book

@app.get('/Books/{title}')
async def get_book(title):
    for book in Books:
        if book['title']==title:
            return book

