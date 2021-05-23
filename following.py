import os,sys,time,json,re

running_path = (os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(running_path)

def Read_():
    with open ('./data/following.json') as f:
        data = f.read()
        data = json.loads(data)
        print (type (data))
        body =  (data['body'])
        print (len (body['users']))
        user_list = body['users']
        for a in user_list:
            print (a['userId'])
            pass

        return user_list

def Write_():
    url_base = 'https://www.pixiv.net/ajax/user/13534898/profile/all?lang=zh'
    userid_pattern = r'\d\d{0,12}'
    userid = re.findall(userid_pattern,url_base)
    user_list = Read_()
    for a in user_list:
        userid = a['userId']
        url_new = re.sub(userid_pattern, userid, url_base)
        with open ('./data/user_id.txt', 'a+', encoding='utf-8') as f:
            f.write(url_new+'\n')

if __name__ == '__main__':
    Write_()
    