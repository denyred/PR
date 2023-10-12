import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

# Load product data
with open('products.json') as f:
    products = json.load(f)


class ProductHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Home Page</h1></body></html>')

        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>About Us</h1></body></html>')

        elif re.match(r'/product/\d+', self.path):
            product_id = int(self.path.split('/')[-1])
            product = products[product_id]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f'''
                <html>
                <body>
                    <h1>{product['name']}</h1>  
                    <p>By: {product['author']}</p>
                    <p>Price: {product['price']}</p>
                    <p>{product['description']}</p>
                </body>
                </html>
            '''
            self.wfile.write(html.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404 Not Found</h1></body></html>')


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), ProductHTTPHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()