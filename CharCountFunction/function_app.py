from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

@app.route('/CharCounter', methods=['GET', 'POST'])
def CharCounter():
    logging.info('Python HTTP trigger function processed a request.')

    name = request.args.get('name')
    if not name:
        try:
            req_body = request.get_json()
        except ValueError:
            req_body = None
        if req_body:
            name = req_body.get('name')

    if name:
        return f"Hello, {name}. This HTTP triggered function executed successfully."
    else:
        return (
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            200
        )

if __name__ == '__main__':
    app.run(debug=True)