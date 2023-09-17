from flask import Flask, render_template


from lc_retriever import *


ld = LCDataRetriever(cookie = "csrftoken=bwSKdfxUbn1fXw66X3C2qK2YTXiun1dp4B6CIPQJcCdqifrkNp17S35z2h3OCM94;LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTg1Njk0OSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjZiMjJiYWFlNjIzYWRmNGNlYTEyM2I4NDdkZDdiMGM2NmUwZWQ2NTciLCJpZCI6NTg1Njk0OSwiZW1haWwiOiJhemFrYmFyYWxpZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhemFrYmFyYWxpZXYiLCJ1c2VyX3NsdWciOiJhemFrYmFyYWxpZXYiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2ODUyNzAzNC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2OTQ4ODE0MDMsImlwIjoiMjEzLjIzMC44MC4zOSIsImlkZW50aXR5IjoiOTE5YjNjYzNkZGU4ODE3NThjNGFhMmNiYWY2MmY3ZjYiLCJzZXNzaW9uX2lkIjo0NjI2NDQyNn0.XGPfGebtmXjokMRV-DHjzAcgF3MebxMCFyUQoPbhmu8")


def getRequest():
        submissions =  ld.retrieve_submissions(pages=1)
        return str(submissions)





app = Flask(__name__)

@app.route('/')
def home():
    message = 'This is my Flask website yoohooo.'
    
    return render_template('index.html', message=getRequest())

if __name__ == '__main__':
    app.run(debug=True)
