import logging
from ditti_web.server import start_server

def main():
    # Set up the logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    start_server(threaded=True, debug=True)



if __name__ == '__main__':
    main()