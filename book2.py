from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from starlette import status
app=FastAPI()

class Books:
    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author = author
        self.description = description
        self.rating=rating
        self.published_date=published_date
class Book_request(BaseModel):
        #id is optional is now
        id :Optional[int]  = Field(description='id is not required for create',default=None)
        title:str = Field(min_length=3)
        author:str=Field(min_length=0,max_length=20)
        description:str=Field(max_length=100)
        rating:float=Field(gt=-1,lt=6)
        published_date:int=Field(gt=0)
        model_config = {      # ceate an example schema
            "json_schema_extra":{
                "example":{
                    "title":"a new title",
                    "author":"a new author",
                    "description":"new desc",
                    "rating":1,
                    "published_date":200
                }
            }
        }
Book_list=[
Books(1,'computer science','coding head','A guide to coding',3.9,2000),
Books(2,'Resnick haliday','resnick','Physics',4.9,3000),
Books(3,'I.E irodov','sir irodov','A master of physics',3005,305),
Books(4,'Cenage','Unkown','PCMB',2.9,3000),
Books(5,'rd sharma','R.D Sharma','for mathematics',3.5,3000),
]

@app.get('/Books',status_code=status.HTTP_200_OK)
async def get_books():
    return Book_list

@app.get('/Books/{id}')
async def get_book_by_id(id:int=Path(gt=-1)):
    for book in Book_list:
        if book.id==id:
            return book
    raise HTTPException(status_code=404,detail='Nah!')
@app.get('/Books/')
async def get_book_rating(rating:float=Query(gt=0.0,lt=5.1)):
    book_to_return=[]
    for book in Book_list:
        if book.rating==rating:
           book_to_return.append(book)
    return book_to_return

@app.post('/create_book',status_code=status.HTTP_201_CREATED)
async def create_book(book:Book_request):
    new_book=Books(**book.model_dump())#model_dump == .dict()
    Book_list.append(get_book_id(new_book))

@app.put('/update_book')
async def update_book(book_update:Book_request):
    book_change=False
    for i in range(len(Book_list)):
        if Book_list[i].id==book_update.id:
            Book_list[i] = Books(**book_update.model_dump())
            book_change=True
    if not book_change:
        raise HTTPException(status_code=404,detail='not updated')

@app.delete('/delete_book/{id}')
async def delete_book_by_id(id:int=Path(gt=-1)):
    for i in range(len(Book_list)):
        if Book_list[i].id==id:
            Book_list.pop(i)
            return

    raise HTTPException(status_code=404,detail="not deleted")

def get_book_id(book:Books):
    if len(Book_list)>0:
        book.id=Book_list[-1].id+1
    else:
        book.id=0

    return book

