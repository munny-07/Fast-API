#pip install fastapi uvicorn
import uvicorn
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates=Jinja2Templates(directory="templates")

app=FastAPI()

@app.get('/')
async def index(req: Request):
    return templates.TemplateResponse(name='index.html',context={'request':req})

'''@app.get('/welcome')
def get_name(name: str):
    return {'welcome bro !':f'{name}'}'''

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)

#python -m uvicorn main:app --reload (for run)