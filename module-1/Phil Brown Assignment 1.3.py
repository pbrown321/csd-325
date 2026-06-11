


#Phil Brown 6/11/2026 Assignment 1.3
#Purpose of this application is to intake user input for number of bottles of beer and count down to 0

#get user input for number of bottles
bottles_of_beer = int(input("How many bottles are currently on the wall? "))


while bottles_of_beer > 0:
#if bottle is plural have to use plural verse    
    if bottles_of_beer > 1:
        print(f"""{bottles_of_beer} bottles of beer on the wall, {bottles_of_beer} bottles of beer!
          You take one down and pass it around
          , {bottles_of_beer - 1} bottles of beer on the wall!""")
    else:
         print(f"""{bottles_of_beer} bottle of beer on the wall, {bottles_of_beer} bottle of beer!
          You take one down and pass it around
          , {bottles_of_beer - 1} bottle of beer on the wall!""")
    
    bottles_of_beer -= 1


#source for lyrics for 0 bottles on the wall: https://en.wikipedia.org/wiki/99_Bottles_of_Beer#Full-length_recitals
print (f"""No more bottles of beer on the wall,
        no more bottles of beer.
        Go to the store and buy some more!""")