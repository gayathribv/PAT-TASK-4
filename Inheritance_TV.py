"""

Create a TV class with properties like brand, channel , price , inches , OnOFF
status and volume. Specify brand in a constructor parameter. Channel should be 1 by default.
Volume should be 50 by default.

"""
class TV:
    # Instance attribute
    def __init__(self, brand):
        self.brand=Brand
        self.channel=1
        self.price=0
        self.inches=32
        self.OnOFF="On"
        self.volume=50

    def TV_status(self):
        print(self.brand, "TV", "Volume is", self.volume, "In Channel", self.channel)
        
    #Function to change volume
    def change_volume(self):
        chng_vol="+"
        while chng_vol != "":
            print("do you want to change volume?")
            print("Enter + to increase and - to decrease")
            chng_vol=input()
            #Case +(increase volume)
            if chng_vol == '+':
                if self.volume == 100:
                    print("Reached Max Volume of 100")
                    continue
                else:
                    self.volume= self.volume+1
                    print("Volume is", self.volume)
            #Case -(decrease volume)
            if chng_vol == '-':
                if self.volume == 0:
                    print("Reached Min Volume of 0")
                    continue
                else:
                    self.volume= self.volume-1
                    print("Volume is", self.volume)
        self.TV_status()

    def change_channel(self):
        """
            The user can directly set channel numbers or increase using + and decrease
            using -. So function will handle both cases.
            Channel number cannot exceed 60 or go below 1
        """
        chng_chnl=0
        while chng_chnl != "":
             print("do you want to change channels?")
             print("Enter + to increase and - to decrease or channel no.")
             chng_chnl=input()
             if chng_chnl== "":
                 continue
             elif chng_chnl == "+":
                 if self.channel >=0 and self.channel <= 49:
                     self.channel=self.channel + 1
                     self.TV_status()
                 else:
                     self.TV_status
                     continue
             elif chng_chnl == "-":
                 if self.channel >=1 and self.channel <= 50:
                    if self.channel >=0 and self.channel <= 49:
                        self.channel=self.channel - 1
                        self.TV_status()
             elif chng_chnl.isalnum() == False:
                 print("Not a valid input")
                 continue
             elif int(chng_chnl) >= 0 and int(chng_chnl) <= 50:
                 print("here")
                 self.channel=int(chng_chnl)
                 self.TV_status()
             else:
                 self.TV_status()
                 continue

#Child Class LEDTV
class LEDTV(TV):
        def __init__(self,Brand,Dtype):
            #Calling parent class (TV) constructor
            super().__init__(Brand)
            self.Displaytype=Dtype
            self.size=32
            self.screen_thickness="7cm"
            self.energy_usage="50W"
            self.Lifespan="10Years"
            self.Refresh_rate="60Hz"
            self.viewingAngle=15
            self.Backlight="Full Array"

        def DisplayDetails(self):
            super().TV_status()
            print("TV Display Type is", self.Displaytype)
            print("TV Size is", self.size)
            print("screen_thickness is", self.screen_thickness)
            print("Energy Usage is", self.energy_usage)
            print("Lifespan is", self.Lifespan)
            print("self.viewing Angle is", self.viewingAngle)
            print("Backlight option is", self.Backlight)


            
class PLASMATV(TV):
        def __init__(self,Brand,Dtype):
            #Calling parent class (TV) constructor
            super().__init__(Brand)
            self.Displaytype=Dtype
            self.size=32
            self.screen_thickness="15cm"
            self.energy_usage="100W"
            self.Lifespan="5Years"
            self.Refresh_rate="60Hz"
            self.viewingAngle=15

        def DisplayDetails(self):
            super().TV_status()
            print("TV Display Type is", self.Displaytype)
            print("TV Size is", self.size)
            print("screen_thickness is", self.screen_thickness)
            print("Energy Usage is", self.energy_usage)
            print("Lifespan is", self.Lifespan)
            print("self.viewing Angle is", self.viewingAngle)



    # Driver code
    # Object instantiation
    # Accept TV Brand
if __name__ == "__main__":
    Brand="Some"
    Dtype="Any"
    if Brand == "Some" and Dtype == "Any":
            print("Please enter the TV Brand")
            Brand=input()
            while Brand == "":
                    print("Brand has to be entered")
                    Brand=input()
            print("Please enter the Display Type(LED/PLASMA)")
            Dtype=input()
            while Dtype == "":
                    print("Dtype has to be entered")
                    Dtype=input()
                    
    if Dtype == "LED":
        ledtv = LEDTV(Brand, Dtype)
        # Accessing class attributes
        print("The Brand you have chosen is", ledtv.brand)
        ledtv.change_volume()
        ledtv.change_channel()
        ledtv.DisplayDetails()
       
    if Dtype == "PLASMA":
        plasmatv=PLASMATV(Brand, Dtype)
        # Accessing class attributes
        print("The Brand you have chosen is", plasmatv.brand)
        plasmatv.change_volume()
        plasmatv.change_channel()
        plasmatv.DisplayDetails()
