__author__ = 'vincent'
import time,sys
import webbrowser

import urllib2
import json
import util
import message



Json_URL = "https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability.json"

Output_URL = "https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability"

mail_list = [""] # mazhaoqin mail
def run(t):
    while(True):
        # response = requests.get(URL)
        # response.encoding = 'gb2312'
        # text = response.text[1:-1]
        # test = json.loads(text)

        html = urllib2.urlopen(Json_URL)

        context = json.loads(html.read())
        tag = False

        for store in context.keys():
            if store != "updated":
                for model in context[store].keys():
                    # print util.getStore(store)+util.getMode(model)

                    if context[store][model] == True:
                        tag = True
                        print store+''+model
                        print util.getStore(store)+' '+util.getMode(model)
                        webbrowser.open_new_tab(Output_URL)
                        message.send_mail(mail_list,"iphone",util.getStore(store)+' '+util.getMode(model))
        if tag:
            time.sleep(120)
        time.sleep(float(t))

if __name__ == "__main__":
    run(sys.argv[1])
