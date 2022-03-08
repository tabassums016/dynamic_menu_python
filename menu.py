import keyboard #Using module keyboard
import os

import asyncio

# ind = 0
# length = 0
# exit=0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

options= ["1. Option1","2. Option2","3. Option3"]
option1= ["a. Suboption1.1 ", "b. Suboption1.2", "c. Suboption1.3"]
option2= ["a. Suboption2.1", "b. Suboption2.2", "c. Suboption2.3"]
option3= ["a. Suboption3.1", "b. Suboption3.2", "c. Suboption3.3"]
miniop1= ["i. Minioption1.1", "ii. Minioption1.2", "Minioption1.3"]
miniop2= ["i. Minioption2.1", "ii. Minioption2.2", "Minioption2.3"]
miniop3= ["i. Minioption3.1", "ii. Minioption3.2", "Minioption3.3"]


option_d = { options[0]:{option1[0]:"abc",option1[1]:"def",option1[2]:"abghia"}, options[1]:{option2[0]:miniop2[0],option2[1]:miniop2[1],option2[2]:miniop2[2]}, options[2]:option3}

# def print_list(op_list, cursor):
#     for item in range(len(op_list)):
#         if item==cursor:
#             print(bcolors.WARNING + op_list[item])
#         else:
#             print(bcolors.OKBLUE + op_list[item])


class menu:

    def __init__ (self):
            self.exit = 0
            self.length = len(option_d.keys())
            self.opt=0
            self.cursor=[]
            self.prev_list=[]
            
            
            self.this_d=option_d
            # self.op_list=op_list

    def create_menu(self,this_d,opt):
        self.this_d=this_d
        i=0
        
        #os.system('cls' if os.name == 'nt' else 'clear')
        for val in self.this_d :
            
            if i<self.length:
                if self.opt==i:
                    if type(self.this_d)==dict:
                        self.prev_list.append(self.this_d)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.print_list(self.this_d[val],0)
                        self.cursor.append(self.opt)
                    self.opt=0   
            i+=1
            
        self.this_d=this_d
        # self.cursor=cursor
        temp_list=[]
        
        #loop = asyncio.get_event_loop()
        # Blocking call which returns when the display_date() coroutine is done
        # loop.run_until_complete(scroll

        # self.create_menu(self.this_d[val],self.opt)
        # self.this_d=self.this_d[val]
        # if self.opt==-1:
        #     self.print_list(self.this_d,self.cursor)


    # async def scroll(self,color,text):
    #     if len(text)>16:
    #         for i in range(len(text)-16):
    #             print(end="\r"+"\t\t\t" + color+ text[i:len(text)])
    #             await asyncio.sleep(0.25)
    #         print("\n")
        # else:
        #     print("\t\t\t" + color+ text)

    def print_list(self, this_d, cursor):
        #self.op_list=op_list
        self.this_d=this_d
        # self.cursor=cursor
        temp_list=[]
        
        #loop = asyncio.get_event_loop()
        # Blocking call which returns when the display_date() coroutine is done
        # loop.run_until_complete(scroll(loop))
        # loop.close()
        print("\n\n\n")
        print(bcolors.OKGREEN+"\t\t\t---------------LCD---------------")
        if type(self.this_d)==str:
            print("\t\t\t"+bcolors.WARNING + self.this_d)
        else:
            for x in self.this_d:
                temp_list.append(x)
            self.length=len(temp_list)
            for item in range(len(temp_list)):
                # if item==cursor:
                #     print(bcolors.WARNING + temp_list[item])
                # else:
                #     print(bcolors.OKBLUE + temp_list[item])
                if item==cursor and item==0:
                    # if len(temp_list[item])<=16:    
                    #     print("\t\t\t" + bcolors.WARNING + temp_list[item] )
                    # else:
                    #     loop.run_until_complete(self.scroll(bcolors.WARNING,temp_list[item]))
                    #     loop.close()
                    print("\t\t\t" + bcolors.WARNING + temp_list[item] )
                    print("\t\t\t" + bcolors.OKBLUE + temp_list[item +1] )
                    # self.scroll(bcolors.WARNING,temp_list[item])
                    # self.scroll(bcolors.OKBLUE,temp_list[item+1])
                elif item+1==cursor :
                    print("\t\t\t" + bcolors.OKBLUE + temp_list[item] )
                    print("\t\t\t" + bcolors.WARNING + temp_list[item +1] )
        print(bcolors.OKGREEN+"\t\t\t---------------------------------")
        
        
        # self.cursor=0

        
    # def get_key(self, prev_list):
    #     self.prev_list=prev_list
    #     for key, value in self.prev_list.items():
    #         if val == value:
    #             return key

    # def menu_func(self,opt):
    #     # if menu==option[0]:
    #     #     print_list(option1)
    #     # if menu==option[1]:
    #     #     print_list(option2)
    #     # if menu== option[2]:
    #     #     print_list(option3)
        
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     if self.opt==1:
    #         self.print_list(option1,self.cursor)   
    #     if self.opt==2:
    #         self.print_list(option2,self.cursor)
    #     if self.opt==3:
    #         self.print_list(option3,self.cursor)
    #     self.opt=0

    def handle_menu(self,event):
        os.system('cls' if os.name == 'nt' else 'clear')
        # global opt
        # self.opt=1
        # print("inside on press")
        # while True:
            
        if event.name == 'down' :
            # print("inside down press")
            if self.opt<self.length-1:
                self.opt+=1
        elif event.name == 'up' :
            if self.opt>0:
                self.opt-=1
        
        if event.name =='left':
            #self.opt=-1
            self.print_list(self.prev_list[-1],self.cursor[-1])
            if self.prev_list[-1]!=self.prev_list[0]:
                self.prev_list.pop(-1)
                self.cursor.pop(-1)
            self.opt=0
        # elif event.name == 'end':
        # print(self.opt)
        else:
            self.print_list(self.this_d,self.opt)   

        if event.name =='enter' or event.name=='right':
            # print("inside enter")
            # global ind
            # ind=self.opt
            # self.prev_list.append(self.this_d)
            self.create_menu(self.this_d,self.opt)
            # self.exit=1
           
            #return
            # break
            # while event.name !='end':
            #     pass

#def home():
lcd=menu()

os.system('cls' if os.name == 'nt' else 'clear')
lcd.print_list(option_d,lcd.opt)
#print(option_d)
# lcd.menu_func(ind)
keyboard.on_press(lcd.handle_menu)   


    # keyboard.on_press(lcd.handle_menu)   
#opt= lcd.opt
# print(ind)


while lcd.exit!=1:
    pass
#print(opt)


#home()
# keyboard.on_press(handle_menu)
# # keyboard.on_press(main_menu.handle_menu)
# menu_func(opt)