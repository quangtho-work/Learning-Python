if __name__ ==  "__main__":

    question = ("Which device is made by Apple?",
                 "Which device is made by Samsung?",
                 "Which device is made by Microsoft?")
    option = (("A. Iphone", "B. Samsung Galaxy", "C. Microsoft Surface"),
               ("A. Iphone", "B. Samsung Galaxy",  "C. Microsoft Surface"),
               ("A. Microsoft Surface", "B. Iphone", "C. Samsung Galaxy"))
    Answer = ("A", "B", "A")
    quiz = (question, Answer)
    guess = []
    print("Quiz:")
    for i in quiz[0]:        
        #in câu hỏi và thứ tự
        print(f"{quiz[0].index(i) + 1}. {i}")
        #in đáp án
        for j in option[quiz[0].index(i)]:
            print(j)
        # yêu cầu người dùng nhập đáp án rồi thêm vào guess
        guess.append(input("\nChọn đáp án: "))
        #kiem tra đáp án
        if guess[quiz[0].index(i)].upper() == Answer[quiz[0].index(i)]:
            print("Đúng!")
        else:
            print("Sai!")

    print("\nKết quả:")
    rightAns = 0
    for i in Answer:
        if i == guess[Answer.index(i)].upper():
            rightAns += 1
    print(f"Số câu trả lời đúng: {rightAns}/{len(quiz[0])}")
