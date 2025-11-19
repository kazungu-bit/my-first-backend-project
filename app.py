
from flask import Flask
app =Flask(__name__)
@app.route('/')
def hello__world():
 return 'Hello , World! This is my first web server'
if __name__ == '__main__':
  app.run(debug=True)
  
