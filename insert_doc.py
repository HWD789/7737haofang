import pymongo
import logging

import getartlist


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s - %(filename)s %(funcName)s] - %(levelname)s: %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
)

connectMongo = 'mongodb://localhost:27017'
mongoclient = pymongo.MongoClient(connectMongo)
dblist = mongoclient.list_database_names()

for dbname in dblist:
    # print (dbname)
    pass
pdb = mongoclient['pixiv']
pcol = pdb['arts']

def DB_in():
    if 'pixiv' in dblist:
        logging.info ('pixiv数据库存在')
    pdict = getartlist.Scan_pixiv()
    try:
        result = pcol.insert_many(pdict)
        logging.info (result.inserted_ids)
    except pymongo.errors.DuplicateKeyError as e:
        # print ((e.details))
        if 11000 in (e.details).values():
            logging.info('目标文档存在')

if __name__ == '__main__':
    DB_in()
    