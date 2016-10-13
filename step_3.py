import requests
#convert unicode to dictionary
import ast

request = {'token': '2b911b9f12182ba5bf0b39cea4440605' }

#grabs the request
dictionary = requests.post('http://challenge.code2040.org/api/haystack' , json = request)

#unicode to dict
haystack = ast.literal_eval(dictionary.text)

#retrived needle and assigned it to variable name
target = haystack[haystack.keys()[1]]

#find index value
target_index = haystack["haystack"].index(target)

#dictionary to json
end = {'token' : '2b911b9f12182ba5bf0b39cea4440605' , 'needle' : target_index}

#json post request
end_post = requests.post('http://challenge.code2040.org/api/haystack/validate', json = end)
