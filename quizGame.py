import re

print("\nPersonality Questions\n\nKnow who you are!")

print("\nRule: For each question, simply answer A, B, C, D or E and make sure to keep track of your points. At the end of the game, add all your points together to know your result)\n\nNB: after the user selects their answer, after 5 seconds, the point should appear next to all the answers and the user should track their scores\n")

q1 = """Choose one sport from the following:
a) Football or soccer or basketball
b) Table tennis or long tennis
c) Lacrosse or cricket or baseball
d) Hockey or golf
e) Wrestling or boxing"""

q2 = """How do you respond when someone insults you?
a) Get angry, but do nothing
b) I blush or start crying
c) I punch them
d) Doesn't affect me at all
e) I ignore them"""

q3 = """How would you prefer to travel?
a) By aeroplane
b) By train
c) By boat or ship
d) By bus
e) By private car or bike"""

q4 = """How does your social friends look like?
a) A bunch of old friends
b) Mostly just family
c) A small circle of loyal friends
d) A bunch of new friends
e) I am a lonely wolf and stick to myself"""

q5 = """What is your dominant emotion?
a) Courage
b) Love
c) Fear
d) Anger
e) Hate"""

q6 = """How aggressive are you?
a) Strong willed, but no aggressive
b) Very aggressive
c) I am peaceful and friendly
d) A little aggressive
e) Extremely aggressive"""

q7 = """What would you rather eat?
a) Vegetable
b) Junk food
c) Fruits
d) Sweets
e) Meat"""

q8 = """What is your worst quality?
a) I am insecure
b) I am clumsy
c) I am perfect
d) I am lazy
e) I am too quiet"""

q9 = """How athletic are you?
a) I enjoy sport occasionally
b) I work out regularly
c) I hate exercise or sports
d) I am generally active
e) I am extremely athletic"""

q10 = """What would upset you the most?
a) Being lied to my face
b) Being alone
c) Being interrupted
d) When a good book or movie ends
e) Being ignored"""

answers1 = {"a":30, "b":10, "c":20, "d":40, "e":50}
answers2 = {"a":40, "b":30, "c":50, "d":20, "e":10}
answers3 = {"a":40, "b":30, "c":20, "d":10, "e":50}
answers4 = {"a":20, "b":10, "c":30, "d":50, "e":40}
answers5 = {"a":30, "b":20, "c":50, "d":40, "e":10}
answers6 = {"a":20, "b":40, "c":10, "d":20, "e":50}
answers7 = {"a":10, "b":30, "c":40, "d":50, "e":20}
answers8 = {"a":40, "b":40, "c":50, "d":20, "e":10}
answers9 = {"a":30, "b":40, "c":10, "d":20, "e":50}
answers10 = {"a":40, "b":20, "c":50, "d":10, "e":30}

questions = {q1:answers1, q2:answers2, q3:answers3, q4:answers4, q5:answers5, q6:answers6, q7:answers7, q8:answers8, q9:answers9, q10:answers10}

elephant = "You are kind, peaceful, caring and dedicated to making those around you happy. You motivate people around you with your innovative ideas and creative insight"
panda = "You are calm and easy-going, but sometimes lazy. People like to be around you because you are fun, insightful and a good listener"
lion = "Practical, productive and strong willed, you are a natural leader. You enjoy challenges, difficult assignments and solving mysteries"
wolf = "You are exciting, quick-witted and adventurous. You are fun and energetic, but sometimes you need to calm down and be more sensitive to the moods of people around you"
horse = "You are very competitive and get annoyed or frustrated when you lose or don’t reach your full potential, but you are almost always a good sport!"

score = 0

for i in questions:
    print("\n", i)

    while True:
        ans = input("\nEnter the answer: a/b/c/d/e: ")

        if re.search(r'^[a-eA-E]$', ans):
            break
        else:
            print("\nSorry, I didn't understand that")
            continue

    score += questions[i][ans]

print("\nFinal score is: ", score, "\n")

if(100 <= score <= 160):
    print(f"You are a {elephant=}\n")
elif(170 <= score <= 250):
    print(f"You are a {panda=}\n")
elif(260 <= score <= 330):
    print(f"You are a {lion=}\n")
elif(340 <= score <= 420):
    print(f"You are a {wolf=}\n")
elif(430 <= score <= 500):
    print(f"You are a {horse=}\n")