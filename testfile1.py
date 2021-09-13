from Question import question

question_prompts=["What color is an apple?\n (a)Green/Red \n(b)Blue\n (c) Purple",
                  "What color is a mango?\n (a)Green/Orange \n(b)Blue \n(c) Purple",
                  "What color are grapes?\n (a)Green/Red \n(b)Blue \n(c) Purple",
                  "What color is a tomato?\n (a)Red \n(b)Blue \n(c) Purple"]
questions=[question(question_prompts[0],"a"),
           question(question_prompts[1],"a"),
           question(question_prompts[2],"c"),
           question(question_prompts[3],"a")]

def runtest(list) :
    score=0
    for question in list:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("Your score is",score,"/",len(list))

runtest(questions)





