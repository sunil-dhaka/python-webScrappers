import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

student_photo=[]
student_name=[]
student_father_name=[]
student_campus=[]
student_rollno=[]
student_batch=[]
student_address=[]
issues_count=0

for page in range(1,91):
    print(f'Working on: {page} ===========')
    url=f'https://www.matrixedu.in/matrix_alumni/{page}'
    r=requests.get(url)
    if r.status_code==200:
        soup=bs(r.text,'html.parser')
        students_list=soup.find_all('div',class_='studentbox')
        for i,student in enumerate(students_list):
            try:
                student_photo.append(student.img.get('src'))

                names=student.find('div',class_='stdent-nam').text.strip().split('\n')
                student_name.append(names[0])
                student_father_name.append(names[1].strip()[7:])

                other_info=student.find('div',class_='student-otherinfo').find_all('li')
                student_campus.append(other_info[0].text) ##
                student_rollno.append(other_info[1].span.text)
                student_batch.append(other_info[2].span.text)

                student_address.append(student.find('div',class_='studnetaddress').text.strip()[10:])

            except Exception as e:
                issues_count+=1
                print(f'Error: {e}')
                print(f'Item No:{i+1} on Page:{page}')

matrix_achivers_df=pd.DataFrame({'Roll No':student_rollno,'Name':student_name,'Father':student_father_name,'Batch':student_batch,'Campus':student_campus,'Address':student_address,'Photo':student_photo})
matrix_achivers_df.to_csv('Matrix_student_data.csv',index=False)