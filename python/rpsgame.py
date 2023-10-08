import random

right_hand=['rock','paper','scissors']
left_hand=['rock','paper','scissors']
right_pick=random.choice(right_hand)
left_pick=random.choice(left_hand)
print(right_pick, left_pick)

if right_pick=='rock' and left_pick=='rock' :
       print ("draw")
elif right_pick== 'paper' and left_pick== 'paper' :
       print ("draw")
elif right_pick== 'scissors' and left_pick=='scissors' :
      print ("draw")
elif right_pick=='rock'and left_pick== 'scissors':
       print ("right wins")
elif right_pick=='rock'and left_pick== 'paper':
       print ("left wins")
elif right_pick== 'paper' and left_pick=='rock':
       print ("right wins")
elif right_pick== 'paper' and left_pick== 'scissors' :
       print("left wins")
elif right_pick=='scissors' and left_pick== 'paper' :
       print ("right wins")
elif right_pick=='scissors'and left_pick== 'rock':
       print("left wins")