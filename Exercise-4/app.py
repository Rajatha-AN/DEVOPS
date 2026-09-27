from flask import Flask, jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "This is a simple REST API built with Flask."
    })

@app.route('/redis', methods=['GET'])
def redis_test():
    try:
        r.set("message", "Hello from Flask to Redis!")
        value = r.get("message")
        return jsonify({
            "status": "success",
            "message": value
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
