"""
This script can rename files in a path by number you given. It can help you when you are fidgety by disordered files.


author   : ZhangWeiqi
data     : 2016-10-10
location :  Xi'an
"""

import os
import sys



def rename(path, num):
    for filename in os.listdir(path):
        file_name = os.path.splitext(filename)[0]
        new_name = filename.replace(file_name, str(num))
        num += 1
        os.rename(
            os.path.join(path, filename),
            os.path.join(path, new_name)
        )


def main():
    if len(sys.argv) != 3:
        print "[+++]Usage: python %s   path    number" %sys.argv[0]
        sys.exit(1)
    else:
        path = sys.argv[1]
        number = sys.argv[2]
        try:
            if not os.path.exists(path):
                print "[---]Error: %s don't exist!" %path
                sys.exit(1)
            number = int(number)
        except:
            print "[---]Error: Last argv must be a int number."
            sys.exit(1)
    rename(path, number)


if __name__ ==  "__main__":
    main()
