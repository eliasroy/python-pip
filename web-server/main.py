import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/')
def getlist():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def getlist():
    return """
    <html>
        <head>
            <title>HELLO</title>
        </head>
        <body>
            <stromg>HOLA SOY ELIAS</strong>
        </body>
    </html>
    """

def run():
    store.get_categoriess()

if __name__=='__main__':
    run()