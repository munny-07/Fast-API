from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sklearn.ensemble import RandomForestClassifier
import pickle
from titan import titans
import uvicorn

template=Jinja2Templates(directory='templates')

app=FastAPI()
tit=pickle.load(open('tit_rf.pkl','rb'))

@app.get('/')
async def welcome(req:Request):
    return template.TemplateResponse(name='index.html',context={'request':req})

@app.post('/click/',response_model=titans)
async def predict(req:Request,Pclass:int=Form(...),Sex:int=Form(...),
    Age:float=Form(...),
    SibSp:int=Form(...),
    Parch:int=Form(...),
    Fare:float=Form(...),
    Embarked:float=Form(...)):

    '''Pclass=Form['Pclass']
    Sex=Form['Sex']
    Age=Form['Age']
    SibSp=Form['SibSp']
    Parch=Form['Parch']
    Fare=Form['Fare']
    Embarked=Form['Embarked']'''

    data1=[[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]]
    
    pred=tit.predict(data1)[0]

    rdata={'request':req,"prediction":pred}
        
    return template.TemplateResponse(name='predict.html',context=rdata)

# u
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)



