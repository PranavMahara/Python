for i in range(10):
    print(i)
    if(i==5):
        break

else:    # wont work as else only works with successful termination of loop, since we used break so there is no successful termination so else dont work
    print("EXIT")