from flask import Flask,render_template, jsonify
from flask import request

app = Flask(__name__)

@app.route('/pptserver', methods=['GET', 'POST'])
#def index():
def index():
	requester = request.remote_addr
    	#logging.info('Data request from: %s' % requester)
    	url = request.url
    	uid = url.split('uid=')[-1]
	get_name=request.args.get("name")
	post_name=request.form.get("name")
	#return "Test message, your input uid=%s, method=%s, get_name=%s, post_name=%s  from %s\n" % (uid, request.method, get_name, post_name, requester)
	return jsonify(get_name=get_name,post_name=post_name)
if __name__ == '__main__':
	app.run()
