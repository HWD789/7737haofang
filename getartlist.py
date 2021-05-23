import os,sys,re,time,json

running_path = (os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(running_path)

print (running_path)

def Scan_pixiv():
    doc_list = []
    read_file = running_path+'/pixiv/'
    path = os.path.realpath(read_file)
    for root, dirs, files in os.walk(path):
        for a in files:
            tarfile = (os.path.join(root,a))
            # print (os.path.join(root,a))
            art_list = Read(tarfile) 
            art_num = len(art_list)
            userid = a.split('.')[0]
            print (userid)
            doc = {'_id':int(userid),'user_id':int(userid),'art':art_num,'art_list':art_list}
            
            doc_list.append(doc)

    print (doc_list)
    return doc_list


def Read(file_):
    with open (file_, 'r+', encoding='utf-8') as f:
        data = f.read()
    header = '<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">'
    data = data.strip(header)
    data = json.loads(data)
    # print (type (data))
    art_list = []
    # print ((data['body']['illusts']))
    for a,b in (data['body']['illusts']).items():
        art_list.append(int(a))
    # print (art_list)
    return art_list
    pass

if __name__ == '__main__':
    # Read(r'I:\File\Code\code_python\Pixiv\pixiv\4780571.txt')
    Scan_pixiv()
    pass