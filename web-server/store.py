import requests

def get_categoriess():
    r=requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)

    cat=r.json()
    for c in cat:
        print(c['name'])
