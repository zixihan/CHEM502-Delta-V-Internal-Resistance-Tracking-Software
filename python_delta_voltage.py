#Data is the experimental data. Output is the calculated delta V.

fileR = open("Data.txt", "r")
fileW = open("Output.txt", "w")

read_count = 0  

cycle_num = int(input("How many cycles are there: "))   #ask for how much cycle needs to be calculate. 

while cycle_num > 0:                                    #run exact number of cylce that required. 

    loop_count = 0

    while loop_count < 1:                               #run this calculation once
        
  
        s = fileR.readline().split()                    #split readed values into an array

        
        s1 = float(s[0])
        s2 = float(s[1])
        s3 = float(s[2])
        s4 = float(s[3])
        
        delta_V = str((s3/s1)-(s4/s2))                  #calculate (Charge Energy/Charge Capacity) - (Discharge Energy/Discharge Capacity)

        print(delta_V)                                  #print calculated data
        
        fileW.write(delta_V)                            #write calculated data into "Output.txt" file
        fileW.write("\n")
        
        
        loop_count = loop_count + 1                     #counters update
        read_count = read_count + 1

    cycle_num = cycle_num - 1

fileR.close()                                           #Close files
fileW.close()
