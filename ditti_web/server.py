from ditti_web.app import app

def start_server(host='localhost', port=5000, threaded=True, debug=True):
    app.run(host=host, port=port, threaded=threaded, debug=debug)