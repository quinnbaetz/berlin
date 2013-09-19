import json

import httplib, urllib, urllib2

class NetworkPlayer():
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}

    def __init__(self, id, port, obj=None, timeout=5000):
        print "player #%s initing with %s" % (id, port)
        self.id = id
        self.port = port
        if(obj):
            self.send_data(obj, timeout)


    def send_data(self, obj, timeout=5000):


        jsonmap = json.dumps(obj);

        #PUTS IN DATA
        #try:
        #    req = urllib2.Request("http://127.0.0.1:"+self.port)
        #    req.add_data(jsonmap)
        #    req.add_header('Content-Type', 'application/json')
##
        #    response = urllib2.urlopen(req, timeout=(timeout/1000))
        #    ret = json.load(response)
        #except:
        #    print "failed to load json from %s on port %s " % (self.id, self.port)
        #    return



        #PUTS IT IN ARGS - switch to otehr encoder
        try:
            req = urllib2.Request("http://127.0.0.1:"+self.port+"?"+urllib.urlencode(obj))
            req.add_header('Content-Type', 'application/json')
            req.get_method = lambda: 'POST'
            response = urllib2.urlopen(req, timeout=(timeout/1000))
            ret = json.load(response)
        except:
            print "failed to load json from %s on port %s " % (self.id, self.port)
            return


        #PUTS IT IN FORM DATA
        #try:
        #    req = urllib2.Request("http://127.0.0.1:"+self.port)
        #    req.add_header('Content-Type', 'application/json')

        #    response = urllib2.urlopen(req, jsonmap, timeout=(timeout/1000))
        #    ret = json.load(response)
        #except:
        #    print "failed to load json from %s on port %s " % (self.id, self.port)
        #    return

        #conn = httplib.HTTPConnection("127.0.0.1", int(self.port), timeout=(timeout/1000))
        #conn.request("POST", "/", jsonmap, self.headers)
        #resp = conn.getresponse()
        #obj = json.load(resp)

        return ret;
