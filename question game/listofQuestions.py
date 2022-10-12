questionsList=["what equals 2+2? \na)4 \nb)6 \nc)10","what is the color of the sea? \na)yellow \nb)blue \nc)red","What word rhymes with cat? \na)bat \nb)bin \nc)door"]

class Questions:
    def __init__ (self,eachquestion,eachanswer):
        self.question = eachquestion
        self.answer = eachanswer
    
x = Questions(questionsList[0],"a")
y = Questions(questionsList[1],"b")
z = Questions(questionsList[2],"a")

integrated_list_of_questions =[
    x,y,z
]

# integrated_list_of_questions =[
#     Questions(questionsList[0],"a"),Questions(questionsList[1],"b"),Questions(questionsList[2],"a")
# ]


def run_queries(totalquestions):
    score = 0
    for eq in totalquestions:
        print(eq.question)
        answer = input("what is the answer:")
        if answer == eq.answer:
            score = score + 1
    print(score)   


run_queries(integrated_list_of_questions)