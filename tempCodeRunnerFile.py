import pyshorteners
s = pyshorteners.Shortener()
print(s.tinyurl.short("https://teams.microsoft.com/_?lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid"))