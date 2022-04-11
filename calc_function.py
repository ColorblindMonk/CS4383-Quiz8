import functions_framework
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@cross_origin()
@functions_framework.http
def do_op(request):
    """ Responds to an HTTP request using data from the request body parsed
    according to the "content-type" header.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_args = request.args
    args_list = ['operation', 'data1', 'data2']

    if request_args and (set(args_list) & set(request_args)) == set(args_list):
        match_case = request_args['operation']
        if match_case == 'add':
            return str(round(float(request_args['data1']) + float(request_args['data2']), 2))
        if match_case == 'sub':
            return str(round(float(request_args['data1']) - float(request_args['data2']), 2))
        if match_case == 'mul':
            return str(round(float(request_args['data1']) * float(request_args['data2']), 2))
        if match_case == 'div':
            try:
                return str(round(float(request_args['data1']) / float(request_args['data2']), 2))
            except ZeroDivisionError:
                return 'Div by zero!'

    return 'No operation!'

