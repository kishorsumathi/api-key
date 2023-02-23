import os

def main(req):
    default_api=os.environ.get('default_api')
    api_key=req.get("api_key")
    try:
        if str(api_key)==str(default_api):
            return {"body":"True"}
        else:
            return {"body":"False"}
    except:
        return {"body":"False"}

    
