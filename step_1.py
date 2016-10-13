import requests

#Holds api token/dictionary and github key
register = {'token': '2b911b9f12182ba5bf0b39cea4440605','github' : 'https://github.com/Daniel-CalderonM/code_2040'}

#request utilizing post and json
request = requests.post('http://challenge.code2040.org/api/register',json = register)

print request.text
