import module1
if __name__ == "__main__":
   if module1.guess_height(int(input("Hãy đoán chiều cao của tôi (cm): "))):
       print("Chúc mừng bạn đoán đúng!")
   else:
       print(f"Sai rồi, chiều cao của tôi là {module1.myhight} cm.")    
