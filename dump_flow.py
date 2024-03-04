# Store dict to json file
# create directory in path if not exist
import json
import os

def store_json(data, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'w') as fp:
        json.dump(data, fp)

def response(flow):
    if "https://www.tiktok.com/api/comment/list/" in flow.request.url:
        # convert string to dict 
        data = json.loads(flow.response.get_text())
        comments = data['comments']
        for comment in comments:
            aweme_id = comment['aweme_id']
            cid = comment['cid']
            store_json(comment, './data/spdbt/comments/'+ aweme_id + "/", cid + '.json')

            
        

        

