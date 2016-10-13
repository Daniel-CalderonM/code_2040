#referenced https://en.wikipedia.org/wiki/ISO_8601 to get a grasp on ISO 8601
import requests
import ast
import datetime

#request call
request = {'token': '2b911b9f12182ba5bf0b39cea4440605'}

#get the request
dictionary = requests.post('http://challenge.code2040.org/api/dating' , json = request)

#will hold the conversion of unicode to a dictionary
time = ast.literal_eval(dictionary.text)

#will hold the iso 8601 value including date and time together
date_time = '%Y-%m-%dT%H:%M:%SZ'

#retrieves the date and sets it to the variable
date = time['datestamp']

#retrienves the interval and sets it to the variable
interval  = time['interval']

#retrieves the time from string of time
real_time = datetime.datetime.strptime(date,date_time)

#adds second to real_time
interval = long(interval)
real_time = real_time + datetime.timedelta(seconds = interval)
result = real_time.isoformat()
result = str(result) + 'Z'

#dictionary to json
end = {'token' : '2b911b9f12182ba5bf0b39cea4440605' , 'datestamp' : result}

#json post request
end_post = requests.post('http://challenge.code2040.org/api/dating/validate', json = end)
