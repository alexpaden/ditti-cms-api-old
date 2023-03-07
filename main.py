import logging
from ditti_api.server import start_server, app
import os


def main():
    # Set up the logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    start_server(threaded=True, debug=True, port=os.getenv("PORT", default=5000))

if __name__ == '__main__':
    main()