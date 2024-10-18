#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: W0516070     
#Student Name: Valentine Byrnes

def main():
# YOUR CODE STARTS HERE, each line must be indented (one tab)
#There is a base labour charge of $1000.
    tCost = 1000
    houseNum = input("Enter house number: ")

#If the surface (length * width) is over 5000 square feet, add $500.
    length = float(input("Enter property depth (ft.): "))
    width = float(input("Enter property width (ft.): ")) 
    sqft = length * width
    if sqft > 5000:
        tCost = tCost + 500

#The cost is calculated per square foot. If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
    grass = input("Please enter the type of grass you would like (fescue, bentgrass, campus): ").lower()
    if grass == "fescue":
        tCost = tCost + (sqft * 0.05)
    if grass == "bentgrass":
        tCost = tCost + (sqft * 0.02)
    if grass == "campus":
        tCost = tCost + (sqft * 0.01)

#Each tree requested has a $100 charge. 
    tree = int(input("How many trees would you like? (If at all): "))
    if tree > 0:
        tCost = tCost + (tree * 100)
    else:
        tCost = tCost

#Total cost
    print("The total cost for house", houseNum, "is: ${0:.2f}".format(tCost))

# YOUR CODE ENDS HERE

main()