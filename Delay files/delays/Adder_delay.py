import os
import subprocess
# import time

# This clears the output file
fp3 = open("adder_delay_analysis.txt",'w')
fp3.close()

#this is the command this helps to choose which file to run
command = "ngspice adder_destination.cir"

#start of script

Input = ["aa0","aa1","aa2","aa3","bb0","bb1","bb2","bb3"]
Output = ["final0","final1","final2","final3"]


for k in range(8):
    if (k<4):
        input = f'''
V_in_A0 aa0 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_A1 aa1 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_A2 aa2 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_A3 aa3 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_B0 bb0 gnd dc 0
V_in_B1 bb1 gnd dc 0
V_in_B2 bb2 gnd dc 0
V_in_B3 bb3 gnd dc 0
        '''
    else:
        input = f'''
V_in_A0 aa0 gnd dc 0
V_in_A1 aa1 gnd dc 0
V_in_A2 aa2 gnd dc 0
V_in_A3 aa3 gnd dc 0
V_in_B0 bb0 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_B1 bb1 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_B2 bb2 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
V_in_B3 bb3 gnd PULSE(0 1.8 0ns 100ps 100ps 40ns 80ns)
        '''
    
    for l in range(4):
        fp1 = open("alu.cir",'r')
        fp2 = open("adder_destination.cir",'w')
        fp3 = open("adder_delay_analysis.txt",'a')
        mode1 = "RISE"
        mode2 = "RISE"
        mode3 = "FALL"
        mode4 = "FALL"

        data = fp1.read()
        search_input = "*Input"
        data = data.replace(search_input,input)
        
        search_text = "*target text"
        replace_text = f'''
.measure tran trise 
+ TRIG v({Input[k]}) VAL = 'SUPPLY/2' {mode1} =1
+ TARG v({Output[l]}) VAL = 'SUPPLY/2' {mode2} =1 

.measure tran tfall 
+ TRIG v({Input[k]}) VAL = 'SUPPLY/2' {mode3} =1 
+ TARG v({Output[l]}) VAL = 'SUPPLY/2' {mode4}=1

.measure tran tpd param = '(trise + tfall)/2' goal = 0
        '''

        data = data.replace(search_text,replace_text)

        fp2.write(data)
        fp1.close()
        fp2.close()

        completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if completed_process.returncode == 0:
            # Capture the standard output into a string
            output = completed_process.stdout
        else:
            output = ("Command execution failed. at",str(k),str(l))

        output = output.split('\n') #helps to seperate the string based on the new line characters
        output = output[-4] 
        additional_text = f" input = {Input[k]} output = {Output[l]}\n"

        fp3.write(output+additional_text)

        # time.sleep(0.4)
        
