from fastapi import FastAPI
from midlleware.middleware import setup_cors
app = FastAPI()
setup_cors(app)

@app.post("/chatbot/voice/")
async def rag(item: voiceAgent):
    try:
        response = voiceAgentController(item.base64,item.extension)
        return {}
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

@app.get("/")
def home():
    return {"message": "OK"}
    
# python -m uvicorn main:app --reload