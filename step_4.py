import requests
import ast
#request call
request = {'token': '2b911b9f12182ba5bf0b39cea4440605'}

#get the request
dictionary = requests.post('http://challenge.code2040.org/api/prefix' , json = request)

#convert the uncode request to a dictionary
array = ast.literal_eval(dictionary.text)

#prefix retrieval
prefix = array[array.keys()[0]]

#get length of prefix
size = len(prefix)

#result array
array_result = []

#following code will go through the array and check if the prefix exist within the code and if not will write to the array_result
for i in range (len(array ['array'])):
    if prefix != array['array'][i][:size]:
        array_result.append(array['array'][i])

#dictionary to json
end = {'token' : '2b911b9f12182ba5bf0b39cea4440605' , 'array' : array_result}

#json post request
end_post = requests.post('http://challenge.code2040.org/api/prefix/validate', json = end)
