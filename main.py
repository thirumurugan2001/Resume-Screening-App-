from fastapi import FastAPI
# Importing CORS setup and data models
from midlleware.middleware import setup_cors
# Importing data models for request bodies
from midlleware.model import *
# Importing user-related functions
from app.Users.signUp import signUp
from app.Users.signIn import signIn
from app.Users.updatePassword import userupdatePassword
from app.Users.forgotPassword import forgotPassword
from app.Users.deleteUser import userdeleteUser
# Importing job description-related functions
from app.JD.createJD import JDcreate
from app.JD.updateJD import JDupdate
from app.JD.deleteJD import JDdelete
# Importing resume screening function
from app.Resume.resumeScreening import resumeScreening
# TODO: Implement the home route logic
app = FastAPI()
setup_cors(app)

# TODO: Implement the home route logic
@app.get("/")
def home():
    return {"message": "OK"}

# TODO: Implement the user signup logic and database integration
@app.post("/user/signUp/")
async def userSignUp(item: userSignup):
    try:
        result = signUp(item.mailId, item.password, item.confirmPassword)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the user signin logic and database integration
@app.post("/user/signIn/")
async def userSignIn(item: userSignin):
    try:
        result = signIn(item.mailId, item.password)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the password update logic and database integration
@app.post("/user/updatePassword/")
async def userUpdatePassword(item: updatePassword):
    try:
        result = userupdatePassword(item.mailId, item.oldPassword, item.newPassword)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }
    
# TODO: Implement the forgot password logic and database integration
@app.post("/user/forgotPassword/")  
async def userForgotPassword(item: ForgotPassword):
    try:
        result = forgotPassword(item.mailId)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the user deletion logic and database integration
@app.post("/user/delete/")
async def userDeleteUser(item: deleteUser):
    try:
        result = userdeleteUser(item.mailId,item.userId)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the job description creation logic and database integration
@app.post("/jobDescription/create/")
async def JDcreate(item: createJD):
    try:
        result = JDcreate(item.userID, item.JBbase64, item.JBbase64extension)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the job description update logic and database integration
@app.post("/jobDescription/update/")
async def JDupdate(item: UpdateJD):
    try:
        result = JDupdate(item.userID, item.updatedJBbase64, item.updatedJBbase64extension)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the job description deletion logic and database integration
@app.post("/jobDescription/delete/")
async def JDdelete(item: deleteJD):
    try:
        result = JDdelete(item.userID, item.JobDescriptionID)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

# TODO: Implement the resume screening logic and database integration
@app.post("/resumeScreening/")
async def userResumeScreening(item: ResumeScreeningApp):
    try:
        result = resumeScreening(item.userID, item.base64Resume, item.resumeExtension)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }
    
# python -m uvicorn main:app --reload