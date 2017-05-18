import os
import pandas as pd
import sys


def validateUser():
    print('Validating The User...')

    current_path=os.path.dirname(__file__)
    user_file=os.path.join(current_path, 'api', 'users.users')
    user=sys.argv[1]

    df=pd.read_csv(user_file, sep='|')
    rec=df[df.USERNAME==user]
    if len(rec)==0:
        raise ValueError('Invalid User')
    else:
        password=rec['PASSWORD']
        pas=raw_input('Enter Password For {}: '.format(user))
        if pas==password[0]:
            userName=rec['NAME']
            return userName[0]
        else:
            raise ValueError('Invalid Password')


def getExtents():
    print('Getting Pan Extents...')

    vertices=sys.argv[2]
    if vertices<3:
        raise ValueError('Tool Works From Triangular Polygons')

    bbox=[]
    counter=1

    for i in xrange(int(vertices)):
        point=raw_input('Enter Vertex {}: '.format(counter))
        coords=point.split(',')
        if not len(coords)==2:
            print('Please Enter a Valid X,Y Pair')
            continue
       
        bbox.append(tuple(map(lambda x: int(x), coords)))
        counter+=1

    return tuple(bbox)

