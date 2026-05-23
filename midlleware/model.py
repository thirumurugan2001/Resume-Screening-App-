from pydantic import BaseModel
from pydantic import Field as field

# USER AUTHENTICATION
class userSignup(BaseModel):
    mailId : str = field(..., example="john.doe@example.com")
    password : str = field(..., example="your_password_here")
    confirmPassword : str = field(..., example="your_password_here")

class userSignin(BaseModel):
    mailId : str = field(..., example="john.doe@example.com")
    password : str = field(..., example="your_password_here")

class updatePassword(BaseModel):
    mailId : str = field(..., example="")
    oldPassword : str = field(..., example="your_old_password_here")
    newPassword : str = field(..., example="your_new_password_here")

class ForgotPassword(BaseModel):
    mailId : str = field(..., example="")

class deleteUser(BaseModel):
    mailId : str = field(..., example="")
    userId : str = field(..., example="")

# JOB DESCRIPTION MANAGEMENT
class createJD(BaseModel):
    userID: str = field(..., example="user123")
    JBbase64 : str = field(..., example="base64_encoded_job_description")
    JBbase64extension : str = field(..., example=".pdf")

class UpdateJD(BaseModel):
    userID: str = field(..., example="user123")
    updatedJBbase64 : str = field(..., example="base64_encoded_updated_job_description")
    updatedJBbase64extension : str = field(..., example=".pdf")

class deleteJD(BaseModel):
    userID: str = field(..., example="user123")
    JobDescriptionID : str = field(..., example="jobdesc123")

# RESUME SCREENING
class ResumeScreeningApp(BaseModel):
    base64Resume : str = field(..., example="base64_encoded_resume")
    resumeExtension : str = field(..., example=".pdf")
