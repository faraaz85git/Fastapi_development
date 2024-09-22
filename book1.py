from fastapi import FastAPI,Body

app = FastAPI()
Books=[
    {'title':'One','author':'Author one','category':'one'},
    {'title':'Two','author':'Author one','category':'one'},
    {'title': 'Three', 'author': 'Author one', 'category': 'two'},

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

@app.get('/Books/{title}') #anything after Book is path parameter and title is pointing to it.
async def get_book(title):
    for book in Books:
        if book['title']==title:
            return book


@app.get('/Books/') #anything after Book is now query parameter
async def get_book_by_category(category:str):
    books=[]
    for book in Books:
        if book.get('category')==category:
            books.append(book)
    return books

@app.post('/Books/create_book')
async def create_book(new_book=Body()):
    Books.append(new_book)

@app.put('/Books/update_book')
async def update_book(update_book=Body()):
    for book in Books:
        if book.get('title')==update_book.get('title'):
            book['author']=update_book['author']
            book['category'] = update_book['category']

@app.delete('/Books/delete_book/{title}')
async def delete_book(title:str):
    for i in range(len(Books)):
        if Books[i]['title']==title:
            Books.pop(i)