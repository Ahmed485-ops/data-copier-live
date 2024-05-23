import sys
from config import DB_DETAILS


def main():
    """Program takes at least one argument"""
    #for arg in sys.argv:
    #    print(arg)

    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)


if __name__  == '__main__':
    main()