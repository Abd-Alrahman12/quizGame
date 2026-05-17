import random
import webbrowser #used for the web run **just for design**
import tempfile   #used for the web run **just for design**
import json       #used for the web run **just for design**
import os         #used for the web run **just for design**

#**********Start of Question section**********

#Football Section
#List of dictionary to store the questions and their choices (for the easy football section)
football_easy = [{
#question 1
"question":"كم عدد لاعبين الفريق داخل الملعب؟",
#options
"options":["11","22","40","10"],     
#answer 
"answer":0
},{
#question 2
"question":"أي منتخب فاز بكأس العالم 2022؟",
#options
"options":["اسبانيا","البرتغال","الارجنتين","البرازيل"],     
#answer 
"answer":2
},{
#question 3
"question":"كم شوط في المباراة؟",
#options 
"options":["1","2","4","3"],     
#answer 
"answer":1
},{
#question 4
"question":"كم مدة مباراة كرة القدم بالدقائق؟",
#options
"options":["90","70","50","20"],     
#answer 
"answer":0
},{
#question 5
"question":" ما الدولة التي ينتمي لها نادي ريال مدريد",
#options
"options":["انجلترا","برتغال","اسبانيا","ايطاليا"],     
#answer 
"answer":2
}]
#List of dictionary to store the questions and their choices (for the normal football section)
football_normal = [{
#question 1
"question":"من أكثر منتخب فاز بكأس العالم؟",
#options
"options":["البرازيل","اسبانيا","الارجنتين","المانيا"],     
#answer 
"answer":0
},{
#question 2
"question":"أي منتخب خسر نهائي كأس العالم 2010؟",
#options
"options":["اسبانيا","ايطاليا","هولندا","البرازيل"],     
#answer 
"answer":2
},{
#question 3
"question":"أي نادي يُلقب بالسيدة العجوز؟",
#options 
"options":["برشلونة","انتر ميلان","ارسنال","يوفنتوس"],     
#answer 
"answer":3
},{
#question 4
"question":"أي نادي حقق دوري أبطال أوروبا أكثر من 10 مرات؟",
#options
"options":["برشلونة","ريال مدريد","ليفربول","اسي ميلان"],     
#answer 
"answer":0
},{
#question 5
"question":"من المدرب الذي حقق السداسية مع نادي برشلونة؟",
#options
"options":["كومان","فليك","جوارديولا","انريكي"],     
#answer 
"answer":2
}]
#List of dictionary to store the questions and their choices (for the hard football section)
football_hard = [{
#question 1
"question":"من اللاعب الذي طُرد بعد نطحة شهيرة في نهائي كأس العالم 2006؟",
#options
"options":["رونالدو","ميسي","زيدان","توتي"],     
#answer 
"answer":2
},{
#question 2
"question":"ما المنتخب الذي أقصى البرازيل 7-1 في كأس العالم 2014؟",
#options
"options":["الارجنتين","البرتغال","اسبانيا","المانيا"],     
#answer 
"answer":3
},{
#question 3
"question":"من أول لاعب عربي سجل هاتريك في كأس العالم؟",
#options
"options":["عبدالرزاق خيري","سالم الدوسري","محمد صلاح","رياض محرز"],     
#answer 
"answer":0
},{
#question 4
"question":"منو اللاعب الذي أضاع ركلة الجزاء الحاسمة لإيطاليا في نهائي كأس العالم 1994؟",
#options
"options":["توتي","مالديني","باجيو","باريسي"],     
#answer 
"answer":2
},{
#question 5
"question":"من أكثر لاعب لعب مباريات في تاريخ كأس العالم؟",
#options
"options":["رونالدو","ميسي","مولر","نيمار"],     
#answer 
"answer":1
}]
#End of football section

#Geography Section
#List of dictionary to store the questions and their choices (for the easy geography section)
geography_easy = [{
#question 1
"question":"ما أطول نهر في العالم؟",
#options
"options":["النيل","الامازون","المسيسيبي","الفولغا"],   
#answer 
"answer":0
},{
#question 2
"question":"كم عدد قارات العالم؟",
#options
"options":["5","7","8","6"],    
#answer 
"answer":1
},{
#question 3
"question":"ما المحيط الأكبر في العالم؟",
#options 
"options":["الاطلسي","الهندي","المتجمد الجنوبي","الهادي"],     
#answer 
"answer":3
},{
#question 4
"question":"ما أكبر دولة في العالم من حيث المساحة؟",
#options
"options":["الصين","امريكا","روسيا","كندا"],     
#answer 
"answer":2
},{
#question 5
"question":"ما الدولة العربية الأكبر مساحة؟",
#options
"options":["الجزائر","السعودية","العراق","المغرب"],     
#answer 
"answer":0
}]
#List of dictionary to store the questions and their choices (for the normal geography section)
geography_normal = [{
#question 1
"question":"ما أصغر دولة في العالم؟",
#options
"options":["قطر","فاتيكان","الكويت","جزر القمر"],     
#answer 
"answer":1
},{
#question 2
"question":"ا أعلى شلالات في العالم؟",
#options
"options":["نياجارا","اغوازو","انجل","انجل"],     
#answer 
"answer":2
},{
#question 3
"question":"ما البحر الذي لا يطل على أي دولة؟",
#options 
"options":["بحر سارجاسو","البحر الاحمر","البحر الاسود","بايكال"],     
#answer 
"answer":0
},{
#question 4
"question":"ما أعمق بحيرة في العالم؟",
#options
"options":["بايكال","البحر الميت","البحر الاحمر","البحر الاسود"],     
#answer 
"answer":0
},{
#question 5
"question":"ما العاصمة التي تُعرف بمدينة الضباب؟",
#options
"options":["برلين","باريس","لندن","بكين"],     
#answer 
"answer":2
}]
#List of dictionary to store the questions and their choices (for the hard geography section)
geography_hard = [{
#question 1
"question":"أي دولة تمتلك أطول حدود برية في العالم؟",
#options
"options":["الصين","امريكا","كندا","البرازيل"],     
#answer 
"answer":2
},{
#question 2
"question":"ما اسم الجبل الذي يُعتبر ثاني أعلى قمة في العالم؟",
#options
"options":["كي2","ايفرست","جبل عرفة","الكونغو"],     
#answer 
"answer":0
},{
#question 3
"question":"ما الدولة التي تقع فيها بحيرة بايكال؟",
#options
"options":["امريكا","الصين","استراليا","روسيا"],     
#answer 
"answer":3
},{
#question 4
"question":"ما الدولة التي تمتلك أكبر احتياطي معروف من المياه العذبة في العالم؟",
#options
"options":["الارجنتين","البرازيل","الاكودور","ماليزيا"],     
#answer 
"answer":1
},{
#question 5
"question":"ما اسم الصحراء التي تمتد عبر أكثر من 10 دول في شمال إفريقيا؟",
#options
"options":["الصحراء الكبرى","الصحراء الصغرى","صحراء المغرب العربي","صحراء افريقية"],     
#answer 
"answer":0
}]
#End of geography section


#Python Section
#List of dictionary to store the questions and their choices (for the easy python section)
python_easy = [{
#question 1
"question":"print(7 + 2)",
#options
"options":["9","7","7 + 2","1"],     
#answer 
"answer":0
},{
#question 2
"question":"print(8 / 2)",
#options
"options":["2","4","8","0"],     
#answer 
"answer":1
},{
#question 3
"question":"print(9 % 2)",
#options 
"options":["2","9","3","1"],     
#answer 
"answer":3
},{
#question 4
"question":"print(len(\"code\"))",
#options
"options":["3","4","5","0"],     
#answer 
"answer":1
},{
#question 5
"question":"print(10 // 3)",
#options
"options":["3","10","1","7"],     
#answer 
"answer":0
}]
#List of dictionary to store the questions and their choices (for the normal python section)
python_normal = [{
#question 1
"question":"print(10 // 3 + 10 % 3)",
#options
"options":["3","5","4","6"],     
#answer 
"answer":2
},{
#question 2
"question":"print(\"Hi\" * 3)",
#options
"options":["HiHiHi","Hi3","Hi","erorr"],     
#answer 
"answer":0
},{
#question 3
"question":"print(len(\"Python\") > 5)",
#options 
"options":["true","false","5","erorr"],     
#answer 
"answer":0
},{
#question 4
"question":"""
x = 10
y = 4
print(x > y and y < 3)
""",
#options
"options":["true and false","false","true","erorr"],     
#answer 
"answer":1
},{
#question 5
"question":"""
lst = [1, 2, 3]
print(lst[1] + lst[2])
""",
#options
"options":["6","4","3","5"],     
#answer 
"answer":3
}]
#List of dictionary to store the questions and their choices (for the hard python section)
python_hard = [{
#question 1
"question":"أي من التالي يُعتبر mutable object في بايثون",
#options
"options":["tuple","string","list","int"],     
#answer 
"answer":2
},{
#question 2
"question":"ي من التالي يُستخدم لمعالجة الأخطاء في بايثون",
#options
"options":["check / catch","try / except","error / solve","fix / catch"],     
#answer 
"answer":1
},{
#question 3
"question":"ي نوع بيانات يمنع تكرار العناصر تلقائيًا؟",
#options
"options":["list","tuple","set","string"],     
#answer 
"answer":2
},{
#question 4
"question":"؟key-value أي من التالي يُستخدم لتخزين البيانات على شك",
#options
"options":["list","dictionary","tuple","set"],     
#answer 
"answer":1
},{
#question 5
"question":" مباشرة؟tupleماذا يحدث إذا حاولت تعديل عنصر داخل ",
#options
"options":["يظهر خطأ","يتم التعديل","يتم حذف العنصر","يتعحول الى list"],     
#answer 
"answer":0
}]
#End of python section

#Dictionary to summarize questions 
#Big dictionary constant (Question)
QUESTIONS = {
    #Small dictionary (football)
    "football":{
        "easy":   football_easy,
        "normal": football_normal,
        "hard":   football_hard
    },
    #Small dictionary (geography)
    "geography":{
        "easy":   geography_easy,
        "normal": geography_normal,
        "hard":   geography_hard
    },
    #Small dictionary (python)
    "python":{
        "easy":   python_easy,
        "normal": python_normal,
        "hard":   python_hard
    }
}


#The points on every question in the Quiz project (constant)
POINTS_PER_QUESTION = 20

#**********End of Question section**********

#**********Start of Function section**********

#Function to calculate score
def calculate_score(correct,total):
    score = correct * POINTS_PER_QUESTION #calculate the score
    percentage = (correct/total)*100      #calculate the percentage
    return score , percentage

#Function to chose a random question
def random_question(question):
    random.shuffle(question)
    return question

#Function to return the rating 
def rating(percentage):
    if percentage>=80:
        return "ممتاز"
    elif percentage>=70:
        return "متوسط"
    elif percentage>=60:
        return "مقبول"   
    else:
        return "حاول مجدداً"

#Function to return options with their letters
def return_options(options):
    letters = ["أ", "ب", "ج", "د"]
    result = []
    for i, op in enumerate(options): #use enumerate fun to go on every option we have 
        result.append((letters[i],op)) #go on a loop to link every option with its letter
    return result 

#Function to return question text
def return_ques(questions):
    result =  list(map(lambda ques:ques["question"],questions))
    return result

#Function to filter the question that has more than 20 letter
def ques_leng(questions):
    result = list(filter(lambda q:len(q["question"])>20,questions))
    return result

#**just for design**
def open_browser():    #Function to open the HTML file in the browser **just for design**
    js_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions.js')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(f'const Q = {json.dumps(QUESTIONS, ensure_ascii=False)};')
        f.write(f'\nconst PTS = {POINTS_PER_QUESTION};')
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quiz.html')
    webbrowser.open('file:///' + html_path.replace('\\', '/'))
    #Function to open the HTML file in the browser **just for design**
#**just for design**


#**********End of Function section**********



#**********Start of Main Function section**********

print(open_browser())   #**just for design**

#dictionary to convirte types to numbers
quiz_type_map = {
    1:"football",
    2:"geography",
    3:"python"
}
#dictionary to convirte difficulties to numbers
quiz_difficulties_map = {
    1:"easy",
    2:"normal",
    3:"hard"
}

print("####### Welcome to the best quiz game #######")
print("===================================================")
print("Enter 1 if you want to play the football quiz")
print("Enter 2 if you want to play the geography quiz")
print("Enter 3 if you want to play the python quiz")
quiz_type= int(input("What do you want to play:"))
while quiz_type > 3 or quiz_type < 1: #to make sure the quiz type in between 1 and 3 
    quiz_type= int(input("Invaild value please re-Enter, What do you want to play:"))

quiz_difficulties =int(input("Great choice, now chose your quiz difficulty (easy=1,normal=2,hard=3):"))
while quiz_difficulties > 3 or quiz_difficulties < 1: #to make sure the quiz difficulty in between 1 and 3 
    quiz_difficulties =int(input("Invaild value please re-Chose your quiz difficulty (easy=1,normal=2,hard=3):"))
 
selected_type = quiz_type_map[quiz_type]  #variable to store the type
selected_difficulty = quiz_difficulties_map[quiz_difficulties] #variable to store the diffiuclty
questions = QUESTIONS[selected_type][selected_difficulty] #list for all the questions
questions = random_question(questions) #Shuffel questions
correct = 0
wrong = 0
total = len(questions)
for q in questions: #to print the questions
    print(q["question"])
    for letter,op in return_options(q["options"]): #to print options
        print(letter,"-",op)
    answer = input("Enter your answer(أ\ب\ج\د):") 
    let = ["أ","ب","ج","د"]
    answer_index = let.index(answer)
    if answer_index == q["answer"]:
        correct+=1
    else: 
        wrong+=1
print("=========================")  
print("thanks for your play")
print("your score= ",calculate_score(correct,total)[0])
print("your percent= ",calculate_score(correct,total)[1],"%")
print("your rating: ",rating(calculate_score(correct,total)[1]))

#**********End of Main Function section**********
