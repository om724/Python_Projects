questions = [
    ["who is shah rukh khan ?","WWE Wrestler","Asstronaut","Actor","Plumber",3],
    ["What is the capital of france?","Rome","Berlin","London","Paris",4],
    ["Which planet is known as the red planet?","Earth","Venus","Mars","Jupiter",3],
    ["what is the largest mammal ?","Elephant","Blue Whale","Giraffe","Shark",2],
    ["who wrote 'Romeo and juliet'?","Charles Dickens","william Shakespeare","Jane Austen","Homer",2],
    ["what is the square of 64 ?","6","8","10","13",2],
    ["which country is known as the land of thr rising Sun?","China","Japan","South Korea","India",2],
    ["Who painted the Mona Lisa?","Vincent van Gogh","Pablop Picasso","Leonardo da vinci","claude mone",2]

]
prizes = [10000,32000,400000,50000,1000000,2000000,3000000000,]
i=0
for question in questions:
    
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    # check Whether The answer is correct or not
    a= int(input("Enter your answer . 1 for a ,/ 2 for b ,/3 for c,/4 for d \n "))
    if(question[5]==a):
        print("Correct Answer")
    else:
        print(f"Incorrect , the correct answer was {question[5]}")
        print("Better luck next Time")
        break
    print(f"You won {prizes[i]}")
    i=i+1
