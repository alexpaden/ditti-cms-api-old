import logging
from ditti_api.server import start_server

def main():
    # Set up the logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    start_server(threaded=True, debug=False)

if __name__ == '__main__':
    main()