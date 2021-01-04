import random, sys, csv, time, pprint, docx

#Setup Selector Function
def food_selector():
    with open('vegan_food.csv') as food:
        reader = csv.DictReader(food)
        suggestion = random.choice(list(reader))
        return suggestion

#Setup while loop
while True:
    #Welcome Customer
    print ('Welcome to the food robot. Press y to receive meal suggestions or q to quit.')

    #Customer inputs answer
    answer=input()
    if answer=='q':
        sys.exit()

    if answer=='y':
        suggestions=[]
        print('For how many days (maximum 7) would you like me to suggest meals?')
        no_of_days=input()
        if no_of_days=='1':
            suggestion=food_selector()
            suggestions=suggestion
            print(suggestions)

        elif no_of_days=='2':
            suggestion=food_selector()
            suggestion_2=food_selector()
            print('Day One:'+ str(suggestion))
            time.sleep(1)
            print('Day Two:'+ str(suggestion_2))
            suggestions= [suggestion, suggestion_2]
        
        elif no_of_days=='3':
            suggestion=food_selector()
            suggestion_2=food_selector()
            suggestion_3=food_selector()
            print('Day One:'+ str(suggestion))
            time.sleep(1)
            print('Day Two:'+ str(suggestion_2))
            time.sleep(1)
            print('Day Three:'+ str(suggestion_3))
            suggestions=[suggestion,suggestion_2,suggestion_3]

        elif no_of_days=='4':
            suggestion=food_selector()
            suggestion_2=food_selector()
            suggestion_3=food_selector()
            suggestion_4=food_selector()
            print('Day One:'+ str(suggestion))
            time.sleep(1)
            print('Day Two:'+ str(suggestion_2))
            time.sleep(1)
            print('Day Three:'+ str(suggestion_3))
            time.sleep(1)
            print('Day Four:'+ str(suggestion_4))
            suggestions=[suggestion,suggestion_2,suggestion_3,suggestion_4]

        elif no_of_days=='5':
            suggestion=food_selector()
            suggestion_2=food_selector()
            suggestion_3=food_selector()
            suggestion_4=food_selector()
            suggestion_5=food_selector()
            print('Day One:'+ str(suggestion))
            time.sleep(1)
            print('Day Two:'+ str(suggestion_2))
            time.sleep(1)
            print('Day Three:'+ str(suggestion_3))
            time.sleep(1)
            print('Day Four:'+ str(suggestion_4))
            time.sleep(1)
            print('Day Five:'+ str(suggestion_5))  
            suggestions=[suggestion,suggestion_2,suggestion_3,suggestion_4,suggestion_5] 

        elif no_of_days=='6':
            suggestion=food_selector()
            suggestion_2=food_selector()
            suggestion_3=food_selector()
            suggestion_4=food_selector()
            suggestion_5=food_selector()
            suggestion_6=food_selector()
            print('Day One:'+ str(suggestion))
            time.sleep(1)
            print('Day Two:'+ str(suggestion_2))
            time.sleep(1)
            print('Day Three:'+ str(suggestion_3))
            time.sleep(1)
            print('Day Four:'+ str(suggestion_4))
            time.sleep(1)
            print('Day Five:'+ str(suggestion_5)) 
            time.sleep(1)
            print('Day Six:'+ str(suggestion_6))     
            suggestions=[suggestion,suggestion_2,suggestion_3,suggestion_4,suggestion_5,suggestion_6]

        elif no_of_days=='7':
            suggestion=food_selector()
            suggestion_2=food_selector()
            suggestion_3=food_selector()
            suggestion_4=food_selector()
            suggestion_5=food_selector()
            suggestion_6=food_selector()
            suggestion_7=food_selector()
            print('Day One:'+ str(suggestion))
            time.sleep(1)
            print('Day Two:'+ str(suggestion_2))
            time.sleep(1)
            print('Day Three:'+ str(suggestion_3))
            time.sleep(1)
            print('Day Four:'+ str(suggestion_4))
            time.sleep(1)
            print('Day Five:'+ str(suggestion_5)) 
            time.sleep(1)
            print('Day Six:'+ str(suggestion_6))  
            time.sleep(1)
            print('Day Seven:'+ str(suggestion_7)) 
            suggestions=[suggestion,suggestion_2,suggestion_3,suggestion_4,suggestion_5,suggestion_6,suggestion_7]

    print('Are you happy with your choice?')
    reply=input()

    if reply=='y':
        print('Enjoy your meal!')
        suggestions=str(suggestions)
        with open('Suggestions.pdf', "w") as f: 
            f.write(suggestions) 

        sys.exit()

    else:
        continue
    
