import requests

content = requests.get('https://www.hiof.no/').text
struct = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()

