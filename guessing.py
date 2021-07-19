import random
Name=input("Enter your name= ")
secret_no= random.randint(0,9)
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess_count +=1
    guess_no = int(input(f"Guess the no. (between 0 and 9)="))
    if guess_no == secret_no:
        print(f'{Name} You Won, {secret_no} is the secret no.')
        break
else:
    print(f'{Name} you lost. {secret_no} is the secret no.')