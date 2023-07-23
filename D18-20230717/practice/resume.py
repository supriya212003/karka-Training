my_resume={
            "name":"supriya",
            "e_mail":"supriyaiyyappan2003@gmail.com",
            "mob_no":6381943829,
            "soft_skills":["team work","adaptability"],
            "hard_skills":"coding",
            "edu_qualification":[{
                "study":"sslc","scl_name":"st.joseph convent higher seconday school","percentage":"80%"},
                {"study":"hsc","scl_name":"st.joseph convent higher seconday school","percentage":"82%"},
                {"study":"degree","clg_name":"govt.arts and science college","percentage":"73%"}],
            "project":"youtube transcript summarizer",
            "experience":[{"company name":"flow","role":"frontend developer","duration":1.2},
                         {"company name":"zoho","role":"teaching assistant","duration":2},
                         {"company name":"software solutions","role":"frontend developer","duration":1}],
            "hobbies":["sketching","listening songs","watching movies"],
            "personal_details":{
                "father_name":"iyyappan",
                "father_occupation":"painter",
                "languages_known":["tamil","english"],
                "d.o.b":21-5-2003, 
                "gender":"female",
                "married_status":"single" ,          
                "adress":{
                "street name":"pulavarvilai",
                "village":"ganesapuram",
                "district":"kanyakumari"
                }}}


education=my_resume["edu_qualification"]
for ed in education:
    print(ed["study"])
    print(ed["percentage"])

add=my_resume["personal_details"]["adress"]
for i in add:
    print(add[i])

lan=my_resume["personal_details"]["languages_known"]
print(lan[1])

ad=my_resume["personal_details"]["adress"]
for ads in ad:
    if ads=="village":
        print(ad["village"])