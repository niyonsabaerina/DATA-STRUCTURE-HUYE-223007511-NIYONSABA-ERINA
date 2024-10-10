from array import array
print('Q1.')

temperatures =[27,30,28,31,32,26,22]
temperatures[1]=20
#The study of other's cares
temperatures.append(1000)
temperatures.remove(1000)
for index , temperature in enumerate(temperatures):
	print(f"day {index + 1} temperature {temperature}"); 
print('Q2.')
dailysales =[200,230,120,234,450,360,207]
print(f"average of daily sales {sum(dailysales) / 7}") 

print("Q3")

val = [20,30,60,50,1,8]
print(f"maximum is{ max(val)} then the minimum { min(val)}")

print("Q4")
marks = [80,60,20,40,90,100]
marks.sort(reverse= True)
print(marks)

print("Q5")
numbers= [1,23,24,12,6,7,9,100,29,80, 90]
def countEven(numbers):
	count = 0
	for number in numbers:
		if number % 2 ==0:
			count += 1
	return count
print(f"even numbers are:{countEven(numbers)}")
odd = len(numbers) - countEven(numbers)
print(f"odd numbers are:{odd}")


print("multi_deminsion array")

print("Q6")

board =[
          ['x','o','o'],
          ['o','x','o'],
          ['x','x','x']
]
def check_winner(board):
   for row in board:
   	    if row[0] == row[1] == row[2]:
       	       return f"winner is {row[0]}"
   for col in range(3):
       if board[0][col] == board[1][col] == board[2][col]:
	         return f"the winner is {board[0][col]}"
	
   if board[0][0] == board[1][1] == board[2][2]:
		     return {board[0][0]}
   return'toe'

print(check_winner(board))
print('Q7')

shop = [
[100,200,300,400,250,500,700],
[250,200,300,400,600,500,700],
[100,200,250,400,600,500,700]
]
for index ,product in enumerate(shop):
	print (f"product{index+1}{list(product)}")
print("Q8")

colors =[
           [255,0,0],
           [0,255,0],
           [0,0,255]

 ]
colors[0] = colors[1]
colors[1] = colors[2]
colors[2] = colors[0]

print(colors)
print('Q9')
total_marks=[
       [90,80,20],
       [50,67,76],
       [98,87,86]


]
for index ,total in enumerate(total_marks):
	
	print(f"student {index+1} marks:{sum(total)}")

print('Q10')
temperatures_city = [
[20, 30, 40, 20, 40, 20, 30], 
[ 20, 40, 20, 30, 20, 40,10], 
[30, 20, 40, 10,30, 20, 40,], 
[30, 20, 40, 10,30, 20, 40,] 
]

for index , daily in enumerate(temperatures_city):
 print(f"the temperature of city{index+1} {sum(daily)/7:.2f}")



print('the quest on list')

print('Q1')

Meeting =['onesphore','enock','betty']
Meeting.append('HE know me')
print(Meeting)  

print('Q2')

shopp =['meat','beans','oranges']
shopp.remove ('beans')
print(shopp)

print('Q3')
names=[24,60,34,55]

names.sort()
print(names)

print('Q4')

todo_list = ["driving", "teaching", "preaching", "pray"]

print("Original to-do list:", todo_list)


def complete_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f'Task completed: "{task}"')
    else:
        print(f'Task not found: "{task}"')


complete_task("Pay bills")


print("Updated to-do list:", todo_list)


print('q5')

double_list=["belyse","kelen","enock"]
print(f"first list:{double_list}")
friend_list=["enock","annet","danny"]
print(f"second list:{friend_list}")
merged_friend_list= list(set(friend_list + double_list))
print(f"removed after duplicated names: {merged_friend_list}")



print('Q6')
for index ,days in enumerate(temperatures_city):
	print(f"the day{index+1}:{sum(days)/7:.2f}%")

students = [
 ['stud1', 30, 'A'],
 ['stud2', 28, 'C'],
 ['stud3', 32, 'B']
]
students.sort(key=lambda student: student[2])
print(students)

print('Q7')
expenses = [
    [1200, 300, 150],  
    [1300, 350, 200],
    [1250, 320, 180],
    [1400, 400, 220],
    [1350, 370, 210],
    [1300, 360, 230] 
]


total_expenses = [0] * len(expenses[0])


for month in expenses:
    for i in range(len(month)):
        total_expenses[i] += month[i]    


average_expenses = [total / len(expenses) for total in total_expenses]


categories = ["Rent", "Food", "Utilities"]
for category, average in zip(categories, average_expenses):
    print(f"Average monthly expense for {category}: Rwf{average:.2f}")

print('q8')

seating_arr=[
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14]
]

seating_arr.reverse()
print(seating_arr)


print('q9')


products=[
["apple",500,10],
["beans",1000,35],
["rice",1500,40],
["salt", 2000,80]
]
in_stock_products= [product for product in products if product[2] > 0]

print("in stock products:")
for product in in_stock_products:
	print(f"name:{product[0]},price: rwf{product[1]:.3f},stock:{product[2]}")

print('Q10')	
scores = [
    ["Derrick", [90, 85, 78]],
    ["Ora", [82, 91, 88]],
    ["Chantal", [75, 80, 95]],
    ["David", [100, 90, 85]]
]

def average_score(scores):
    return sum(scores) / len(scores)

winner = None
highest_average = 0

for player in scores:
    name = player[0]
    player_scores = player[1]
    avg = average_score(player_scores)
    
    if avg > highest_average:
        highest_average = avg
        winner = name


print(f"The winner is {winner} with an average score of {highest_average:.2f}.")











