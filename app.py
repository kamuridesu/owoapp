from flask import Flask, jsonify, redirect
from read_env import EnvVariablesController


app = Flask(__name__)
environment_vars = EnvVariablesController()
host = "0.0.0.0"
port = 9000
my_host = f"http://{host}:{port}"

@app.route('/forward', methods=['GET'])
def index():
    check = environment_vars.check_vars("CONTEXT_PATH", "FORWARD", "DST_PATH")
    if check['status'] == "ok":
        if environment_vars.get("FORWARD").lower() == "true":
            return redirect(environment_vars.get("DST_PATH"))
        return jsonify({"msg": "Forward not allowed"}), 403
    else:
        return jsonify(check), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)