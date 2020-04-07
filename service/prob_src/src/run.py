from app import *
import sys

def main():
    #TODO : disable debug
    app.run(debug=False, host="0.0.0.0", port=8080)

if __name__ == '__main__':
    main()
