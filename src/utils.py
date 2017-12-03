from flask import Response


def response(status_code, content):
    res = Response(content, content_type='application/json')
    res.status_code = status_code
    return res
