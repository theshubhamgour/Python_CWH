# program to find whether a student is pass or fail
sub1=int(input("Enter makrs of first subjeect\n"))
sub2=int(input("Enter makrs of second subjeect\n"))
sub3=int(input("Enter makrs of third subjeect\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")

elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congratulations you're passed")