def health_check():
   return {"status": "healthy"}

if __name__=="__main__":
   result=health_check()
   print(result)
