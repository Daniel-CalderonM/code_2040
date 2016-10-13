import requests

dictionary = {'token': '2b911b9f12182ba5bf0b39cea4440605' }

request = requests.post('http://challenge.code2040.org/api/reverse', json = dictionary)

#utilized to make sure that my connection is correct and is retieving a string
print request.text

string = request.text

string_reverse  = ''

size = len(string)

for i in range(0,size):
    #works by addin the string to the new index EX reverse pizza; i + p
    string_reverse= string[i] + string_reverse
#dictionary to json
end = {'token' : '2b911b9f12182ba5bf0b39cea4440605' , 'string' : string_reverse}
#json post request
end_post = requests.post('http://challenge.code2040.org/api/reverse/validate', json = end)
