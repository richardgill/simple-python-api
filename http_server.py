from bottle import request, response, route, run
import json
import os

@route('/milanFunction')
def hello():
  input = request.query.getall('input[]')
  print(input)
  print(type(input))
  response.content_type = 'application/json'
  return json.dumps({'hello': "world"})

if os.environ.get('PYTHON_ENV') == 'PRODUCTION':
  print('Running in prod :serious_face:')
  run(host='0.0.0.0', port=os.environ.get('PORT'))
else:
  run(host='localhost', port=8080, debug=True)
