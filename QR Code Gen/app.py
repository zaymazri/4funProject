from flask import Flask, request, send_file
from flask_cors import CORS
from io import BytesIO

import qrcode

app = Flask(__name__)
CORS(app)

@app.route('/gen_qrcode', method=['POST'])
def gen_qrcode():
    buffer  =BytesIO()
    data = request.form.get('data')

    img = qrcode.make("data")
    img.save(buffer)
    buffer.seek(0)

    response = send_file(buffer, mimetype='image/png')
    return response.read

if __name__ == '__main__':
    app.run()