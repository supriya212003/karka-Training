study=[{
         
         "grade":"B.tech",
         "institute":"govt.clg,konam",
         "Semester":[{
         "semester_name":1,
         "subject":["architecture","computer","maths"],
         "grade":"A+"}]},
                         
         {"grade":"M.tech",
         "institute":"govt.clg,konam",
         "Semester":[{
         "semester_name":2,
         "subject":["data analysis","machine learning","nme"],
         "grade":"B+"}]}]
for item in study:
   print(item['Semester']) 
   sem=item["Semester"]
   for s in sem:
      print(s["subject"])
      ss=s["subject"]
      for y in ss:
         print(y)        

            