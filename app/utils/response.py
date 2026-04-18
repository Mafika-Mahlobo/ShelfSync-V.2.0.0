
class Response:

    def __init__(self, success: bool, data=None, error=None, status_code=200):
        self.success = success
        self.data = data
        self.error = error
        self.status_code = status_code

    def to_dict(self):
        return {
            'success': self.success,
            'data': self.data,
            'error': self.error,
            'status_code': self.status_code
        }
    
    def to_http(self):
        from flask import jsonify
        return jsonify(self.to_dict()), self.status_code
    
    @classmethod
    def fail(cls, error=None, status_code=400):
        return cls(False, error=error, status_code=status_code)

    @classmethod
    def success(cls, data=None, status_code=200):
        return cls(True, data=data, status_code=status_code)