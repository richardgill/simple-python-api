from bottle import request, response, route, run
import json

@route('/milanFunction')
def hello():
  input = request.query.getall('input[]')
  print(input)
  print(type(input))
  response.content_type = 'application/json'
  return json.dumps({'hello': "world"})

run(host='localhost', port=8080, debug=True)
