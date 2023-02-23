import os

def main(req):
    default_api=os.environ.get('default_api')
    success=os.environ.get("for_true")
    error=os.environ.get("for_false")
    api_key=req.get("api_key")
    try:
        if str(api_key)==str(default_api):
            return {"body":str(success)}
        else:
            return {"body":str(error)}
    except:
        return {"body":str(error)}

    
