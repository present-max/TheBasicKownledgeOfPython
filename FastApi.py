from pydantic import BaseModel, Field
from fastapi import FastAPI ,Path, Query,HTTPException
from fastapi.responses import HTMLResponse,FileResponse

app=FastAPI()

# 路径参数
@app.get("/book/{id}")#装饰器：当访问/book/1时，会调用get_book函数
async def get_book(id: int = Path(..., gt=0, lt=100, description="The ID of the book to get")):
    if id in range(1,101):
       return {f"拿到第{id}本书"}
    else:
        # 抛出异常
        raise HTTPException(status_code=404, detail="Book not found")

# 查询参数
@app.get("/book")
async def get_book(skip: int = Query(0, description="The number of items to skip"),
                   limit: int = Query(10, description="The number of items to limit")
                   ):
    return {"skip": skip, "limit": limit}

class Book(BaseModel):
    id: int = Field(..., gt=0, description="The ID of the book")
    title: str = Field(..., min_length=1, max_length=100, description="The title of the book")
    author: str = Field(..., min_length=1, max_length=100, description="The author of the book")
    price: float = Field(..., gt=0, description="The price of the book")
    is_available: bool = Field(..., description="Whether the book is available")

#请求体参数
@app.post("/book")
async def create_book(book: Book):
    return {"book": book}

#指定返回类型为HTML
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI</title>
        </head>
        <body>
            <h1>FastAPI</h1>
        </body>
    </html>
    """

#指定返回类型为文件
@app.get("/file")
async def read_file():
    return FileResponse("./projectdemo/resourse/movie_top100.png")

#中间件：各中间件的执行顺序：从代码顺序自下而上
@app.middleware("http")
async def midlle1(request, call_next):
    # 在请求处理之前执行的代码
    print("Something1 is happening before the request is processed")
    # 等待请求处理完成
    response = await call_next(request)
    # 在请求处理之后执行的代码
    print("Something1 is happening after the request is processed")
    return response
@app.middleware("http")
async def midlle2(request, call_next):
    print("Something2 is happening before the request is processed")
    response = await call_next(request)
    print("Something2 is happening after the request is processed")
    return response


#依赖注入（抽取共性的地方，比如查询参数、路径参数等））
from fastapi import Depends
async def common_parameters(q: str = Query(None, description="Query string"), skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to limit")):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("FastApi:app", host="127.0.0.1", port=8080, reload=True)
