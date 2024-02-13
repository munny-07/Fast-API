import json

class Calculator:
    def __init__(self):
        pass
    
    def calculate(self, num1, num2, operation):
        result = None
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return {'error': 'Cannot divide by zero'}
        else:
            return {'error': 'Invalid operation'}
        
        return {'result': result}

class App:
    def __init__(self):
        self.calculator = Calculator()
    
    def handle_request(self, data):
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']
        
        result = self.calculator.calculate(num1, num2, operation)
        return result
    
    def run(self, environ, start_response):
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        request_body = environ['wsgi.input'].read(content_length).decode('utf-8')
        data = json.loads(request_body)
        
        result = self.handle_request(data)
        
        response_body = json.dumps(result)
        response_headers = [('Content-Type', 'application/json')]
        start_response('200 OK', response_headers)
        
        return [response_body.encode('utf-8')]

if __name__ == '__main__':
    app = App()
    app.run()