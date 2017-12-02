from flask import Response


def response(status_code, content):
    res = Response(content, content_type='application/json')
    res.status_code = status_code
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PATCH,POST,PUT,DELETE,OPTIONS'
    res.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return res
