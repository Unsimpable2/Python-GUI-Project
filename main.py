from email.mime import image
from tkinter import *
import tkinter.font as font
from math import *
from PIL import ImageTk, Image
from idlelib.tooltip import Hovertip

root = Tk()
root.geometry('1400x800')
root.winfo_toplevel().title("MyFitnessPlan")
root.resizable(False, False)

class Gui:
    def __init__(self, master):
        self.master = master
        self.ButtonValue = 0
        self.OptionValue = 0
        self.OptionValueDel = 0

        self.GenderValue = IntVar()
        self.ActivityValue = IntVar()
        self.GoalValue = IntVar()
        self.AgeValueKcal = StringVar()
        self.WeightValueKcal = StringVar()
        self.HeightValueKcal = StringVar()

        self.HeightValue = StringVar()
        self.WeightValue = StringVar()
        self.NeckValue = StringVar()
        self.WaistValue = StringVar()
        self.HipValue = StringVar()

        self.BMI = 0
        self.BFP = 0
        
        self.PhotoNumber = 1
        self.PhotoMax = 0
        self.Path = f''
        self.PartPath = f''
        
        self.BackgroundImg = PhotoImage(file = 'Img/GUI/Background.png')
        self.ButtonFrameImg = PhotoImage(file = 'Img/GUI/ButtonFrame.png')
        self.LanguageFrameImg = PhotoImage(file = 'Img/GUI/LangImg.png') 
        self.ChangeFrameImg = PhotoImage(file = 'Img/GUI/NextPrevImg.png')
        self.PhotoFrameImg = PhotoImage(file = 'Img/GUI/PhotoFrameImg.png')
        self.CalculatorImg = PhotoImage(file = 'Img/GUI/CalculatorFrameImg.png')
        self.CalculatorUpWholeImg = PhotoImage(file = 'Img/GUI/CalculatorUpWhole.png')
        self.CalculatorUpImg = PhotoImage(file = 'Img/GUI/CalculatorUp.png')
        self.CalculatorDownImg = PhotoImage(file = 'Img/GUI/CalculatorDownWhole.png')
        
        self.BackgroundLable = Label(self.master, image = self.BackgroundImg).place(x = -3, y = 0)  

        #ButtonFrame
        self.ButtonFrame = Frame(self.master, width = 200, height = 600)
        self.ButtonFrame.place(x = 30, y = 30)
        self.ButtonImageFrame = Label(self.ButtonFrame, image = self.ButtonFrameImg).place(x = -3, y = -4)

        #PhotoFrame
        self.PhotoFrame = Frame(self.master, width = 730, height = 600)
        self.PhotoFrame.place(x = 260, y = 30)
        self.PhotoImgFrame = Label(self.PhotoFrame, image = self.PhotoFrameImg).place(x = -6, y= -4)

        #CalculatorFrame
        self.CalculatorFrame = Frame(self.master, width = 350, height = 600)
        self.CalculatorFrame.place(x = 1020, y = 30)
        self.CalculatorFrameImg = Label(self.CalculatorFrame, image = self.CalculatorImg).place(x = -6, y = -6)

        self.CalculatorUpFrame = Frame(self.CalculatorFrame, width = 348, height = 208)
        self.CalculatorUpFrame.place(x = 1, y = 30)
        self.CalculatorUpFrameImg = Label(self.CalculatorUpFrame, image = self.CalculatorUpWholeImg).place(x = -8, y = -6)

        self.CalculatorUpSideFrame = Frame(self.CalculatorUpFrame, width = 262, height = 207)
        self.CalculatorUpSideFrame.place(x = 85, y = 1)
        self.CalculatorUpSideFrameImg = Label(self.CalculatorUpSideFrame, image = self.CalculatorUpImg).place(x = -6, y = -6)

        self.CalculatorDownFrame = Frame(self.CalculatorFrame, width = 348, height = 329, bg = 'blue')
        self.CalculatorDownFrame.place(x = 1, y = 270)
        self.CalculatorDownFrameImg = Label(self.CalculatorDownFrame,image = self.CalculatorDownImg).place(x = -7, y = -6)

        #ChangeButtonFrame
        self.ChangeFrame = Frame(self.master, width = 670, height = 50)
        self.ChangeFrame.place(x = 290, y = 650)
        self.NextPrevImg = Label(self.ChangeFrame, image = self.ChangeFrameImg).place(x = -9, y = -7)

        #LanguageChangeFrame
        self.LanguageFrame = Frame(self.master, width = 140, height = 60)
        self.LanguageFrame.place(x = 30, y = 705)
        self.LanguageImgFrame = Label(self.LanguageFrame, image = self.LanguageFrameImg).place(x = -2, y = -2)

        self.Run()

    def Run(self):
        self.ShowOptions()
        self.BMIBFPCalc()
        self.KcalCalc()

    def ShowOptions(self):
        #Workout
        self.BodyPartWorkout = Label(self.ButtonFrame, text = 'Workout Body Part', font = 'Helvetica 15 bold')
        self.BodyPartWorkout.place(x = 6, y = 15)

        self.ButtonBackWorkout = Button(self.ButtonFrame, text = 'Back', fg = "black", width = 10, command = self.BackVariableW, font = 'Helvetica 12 bold')
        self.ButtonBackWorkout.place(x = 50, y = 60)

        self.ButtonChestWorkout = Button(self.ButtonFrame, text = 'Chest', fg = "black", width = 10, command = self.ChestVariableW, font = 'Helvetica 12 bold')
        self.ButtonChestWorkout.place(x = 50, y = 100)

        self.ButtonShouldersWorkout = Button(self.ButtonFrame, text = 'Shoulders ', fg = "black", width = 10, command = self.ShouldersVariableW, font = 'Helvetica 12 bold')
        self.ButtonShouldersWorkout.place(x = 50, y = 140)

        self.ButtonBicepsWorkout = Button(self.ButtonFrame, text = 'Biceps', fg = "black", width = 10, command = self.BicepsVariableW, font = 'Helvetica 12 bold')
        self.ButtonBicepsWorkout.place(x = 50, y = 180)

        self.ButtonTricepsWorkout = Button(self.ButtonFrame, text = 'Triceps', fg = "black", width = 10, command = self.TricepsVariableW, font = 'Helvetica 12 bold')
        self.ButtonTricepsWorkout.place(x = 50, y = 220)

        self.ButtonLegsWorkout = Button(self.ButtonFrame, text = 'Legs', fg = "black", width = 10, command = self.LegsVariableW, font = 'Helvetica 12 bold')
        self.ButtonLegsWorkout.place(x = 50, y = 260)

        self.ButtonABSWorkout = Button(self.ButtonFrame, text = 'Abs', fg = "black", width = 10, command = self.AbsVariableW, font = 'Helvetica 12 bold')
        self.ButtonABSWorkout.place(x = 50, y = 300)

        #Stretch
        self.BodyPartStreach = Label(self.ButtonFrame, text = 'Stretch Body Part', font = 'Helvetica 15 bold')
        self.BodyPartStreach.place(x = 11, y = 345)

        self.ButtonLegsStreach = Button(self.ButtonFrame, text = 'Legs', fg = "black", width = 10, command = self.LegsVariableS, font = 'Helvetica 12 bold')
        self.ButtonLegsStreach.place(x = 50, y = 390)

        self.ButtonChestStreach = Button(self.ButtonFrame, text = 'Chest', fg = "black", width = 10, command = self.ChestVariableS, font = 'Helvetica 12 bold')
        self.ButtonChestStreach.place(x = 50, y = 430)

        self.ButtonArmsStreach = Button(self.ButtonFrame, text = 'Arms', fg = "black", width = 10, command = self.ArmsVariableS, font = 'Helvetica 12 bold')
        self.ButtonArmsStreach.place(x = 50, y = 470)
        
        self.ButtonABSStreach = Button(self.ButtonFrame, text = 'Abs', fg = "black", width = 10, command = self.AbsVariableS, font = 'Helvetica 12 bold')
        self.ButtonABSStreach.place(x = 50, y = 510)

        self.ButtonOthersStreach = Button(self.ButtonFrame, text = 'Others', fg = "black", command = self.OthersVariableS, width = 10, font = 'Helvetica 12 bold')
        self.ButtonOthersStreach.place(x = 50, y = 550)

        #Next/PrevPhoto
        self.PreviousButton = Button(self.ChangeFrame, text = 'Previous Photo', fg = "black", width = 15, command = self.PrevPhoto, font = 'Helvetica 12 bold')
        self.NextButton = Button(self.ChangeFrame, text = 'Next Photo', fg = "black", width = 15, command = self.NextPhoto, font = 'Helvetica 12 bold')
        
        #Language
        self.SelectLan = Label(self.LanguageFrame, text = 'Language Options', font = 'Helvetica 10 bold', borderwidth=0)
        self.SelectLan.place(x = 15, y = 15, anchor = 'w')

        self.PLButton = Button(self.LanguageFrame, text = 'PL', fg = "black", width = 5)
        self.PLButton.place(x = 21, y = 30)

        self.ENGButton = Button(self.LanguageFrame, text = 'ENG', fg = "black", width = 5)
        self.ENGButton.place(x = 82, y = 30)

        #ImportantInformation
        self.InformationButton = Button(self.master, text = 'Important information', fg = "black", width = 20, font = 'Helvetica 15 bold', command = self.Info)
        self.InformationButton.place(x = 1070, y = 650)

        #Exit
        self.ExitButton = Button(self.master, text = 'Exit', fg = "black", width = 8, command = self.FullExit, font = 'Helvetica 15 bold')
        self.ExitButton.place(x = 1265, y = 730)    
       
    def BMIBFPCalc(self):
        #CalculatorBMI/BFP
        Label(self.CalculatorFrame, text = 'BMI and Body Fat Procent Calculator', fg = "black", font = 'Helvetica 12 bold').place(x = 33, y = 15, anchor='w')

        self.ManButton = Button(self.CalculatorUpFrame, text = 'Man', fg = "black", width = 7, font = 'Helvetica 10 bold', command = self.ManOption)
        self.ManButton.place(x = 10, y = 10)

        self.WomanButton = Button(self.CalculatorUpFrame, text = 'Woman', fg = "black", width = 7, font = 'Helvetica 10 bold', command = self.WomanOption)
        self.WomanButton.place(x = 10, y = 45)

    def KcalCalc(self):
        #CalculatorKcal
        Label(self.CalculatorFrame, text = 'Daily Caloric Requirement Calculator', fg = "black", font = 'Helvetica 12 bold').place(x = 28, y = 254, anchor='w')

        self.GenderChoose = Label(self.CalculatorDownFrame, text = 'Choose gender:', font = 'Helvetica 10 bold').place(x = 5, y = 5)

        self.GenderMan = Radiobutton(self.CalculatorDownFrame, text = 'M', variable = self.GenderValue, value = 1)
        self.GenderMan.place(x = 5, y = 30)

        self.GenderWoman = Radiobutton(self.CalculatorDownFrame, text = 'F', variable = self.GenderValue, value = 2)
        self.GenderWoman.place(x = 40, y = 30)

        self.GenderChoose = Label(self.CalculatorDownFrame, text = 'Fill the Data:', font = 'Helvetica 10 bold').place(x = 5, y = 60)

        self.AgeLabelKcal = Label(self.CalculatorDownFrame, text = 'Age: ').place(x = 5, y = 85)
        self.AgeEntryKcal = Entry(self.CalculatorDownFrame, width = 3, textvariable = self.AgeValueKcal)
        self.AgeEntryKcal.place(x = 80, y = 86)

        self.HeightLabelKcal = Label(self.CalculatorDownFrame, text = 'Height(cm): ').place(x = 5, y = 110)
        self.HeightEntryKcal = Entry(self.CalculatorDownFrame, width = 5, textvariable = self.HeightValueKcal)
        self.HeightEntryKcal.place(x = 80, y = 111)

        self.WeightLabelKcal = Label(self.CalculatorDownFrame, text = 'Weight(kg): ').place(x = 5, y = 135)
        self.WeightEntryKcal = Entry(self.CalculatorDownFrame, width = 5, textvariable = self.WeightValueKcal)
        self.WeightEntryKcal.place(x = 80, y = 136)

        self.GenderChoose = Label(self.CalculatorDownFrame, text = 'Level of Physical Activity:', font = 'Helvetica 10 bold').place(x = 150, y = 5)

        self.ActivityZero = Radiobutton(self.CalculatorDownFrame, text = 'Zero Physical Activity', variable = self.ActivityValue, value = 1)
        self.ActivityZero.place(x = 150, y = 30)
        Hovertip(self.ActivityZero, text = 'No Physical Activity Whatsoever/Sitting Work')

        self.ActivityVeryLow = Radiobutton(self.CalculatorDownFrame, text = 'Very Low Physical Activity', variable = self.ActivityValue, value = 2)
        self.ActivityVeryLow.place(x = 150, y = 55)
        Hovertip(self.ActivityVeryLow, text = 'Rare Physical Activity, From Time to Time')

        self.ActivityLow = Radiobutton(self.CalculatorDownFrame, text = 'Low Physical Activity', variable = self.ActivityValue, value = 3)
        self.ActivityLow.place(x = 150, y = 80)
        Hovertip(self.ActivityLow, text = 'Physical Activity Once a Week')

        self.ActivityMid = Radiobutton(self.CalculatorDownFrame, text = 'Mid Physical Activity', variable = self.ActivityValue, value = 4)
        self.ActivityMid.place(x = 150, y = 105)
        Hovertip(self.ActivityMid, text = 'Physical Activity Two/Three a Week')

        self.ActivityHigh = Radiobutton(self.CalculatorDownFrame, text = 'High Physical Activity', variable = self.ActivityValue, value = 5)
        self.ActivityHigh.place(x = 150, y = 130)
        Hovertip(self.ActivityHigh, text = 'Physical Activity Four/Five a Week')

        self.ActivityVeryHigh = Radiobutton(self.CalculatorDownFrame, text = 'Very High Physical Activity', variable = self.ActivityValue, value = 6)
        self.ActivityVeryHigh.place(x = 150, y = 155)
        Hovertip(self.ActivityVeryHigh, text = 'Physical Work With Regular Trainings')

        self.GoalChoose = Label(self.CalculatorDownFrame, text = 'Set Your Goal:', font = 'Helvetica 10 bold').place(x = 150, y = 185)

        self.GoalReduction = Radiobutton(self.CalculatorDownFrame, text = 'Weight Reduction', variable = self.GoalValue, value = 1)
        self.GoalReduction.place(x = 150, y = 210)

        self.GoalStay = Radiobutton(self.CalculatorDownFrame, text = 'Weight Maintenance', variable = self.GoalValue, value = 2)
        self.GoalStay.place(x = 150, y = 235)

        self.GoalGain = Radiobutton(self.CalculatorDownFrame, text = 'Weight Gain', variable = self.GoalValue, value = 3)
        self.GoalGain.place(x = 150, y = 260)

        self.AnswerKcal = Label(self.CalculatorDownFrame, text = '')
        self.AnswerKcal.place(x = 10, y = 200)

        self.GenderValue.set("1")
        self.ActivityValue.set("1")
        self.GoalValue.set("1")

        self.KcalButton = Button(self.CalculatorDownFrame, text = "Calculate", font = 'Helvetica 10 bold', command = self.CountCalories)
        self.KcalButton.place(x = 265, y = 290)
        
    def CountCalories(self):
        GenderValue = self.GenderValue.get()
        AgeKcal = self.AgeValueKcal.get()
        HeightKcal = self.HeightValueKcal.get()
        WeightKcal = self.WeightValueKcal.get()
        ActivityValue = self.ActivityValue.get()
        GoalValue = self.GoalValue.get()

        Activity = 0
        Kcal = 0

        try:
            AgeKcal = int(AgeKcal)
            HeightKcal = int(HeightKcal)
            WeightKcal = int(WeightKcal)

            #common
            if ActivityValue == 1:
                Activity = 1.2

            elif ActivityValue == 2:
                Activity = 1.3

            #man
            elif ActivityValue == 3 and GenderValue == 1:
                Activity = 1.6

            elif ActivityValue == 4 and GenderValue == 1:
                Activity = 1.7

            elif ActivityValue == 5 and GenderValue == 1:
                Activity = 2.1

            elif ActivityValue == 6 and GenderValue == 1:
                Activity = 2.4

            #woman
            elif ActivityValue == 3 and GenderValue == 2:
                Activity = 1.5

            elif ActivityValue == 4 and GenderValue == 2:
                Activity = 1.6

            elif ActivityValue == 5 and GenderValue == 2:
                Activity = 1.9

            elif ActivityValue == 6 and GenderValue == 2:
                Activity = 2.2

            if GenderValue == 1:
                Kcla = 66.47 + 13.7 * WeightKcal + 5.0 * HeightKcal - 6.76 * AgeKcal
                Kcal = Kcal * Activity

                if GoalValue == 1:
                    Kcla = Kcla - 300

                if GoalValue == 3:
                    Kcla = Kcla + 300

            elif GenderValue == 2:
                Kcla = 665.1 + 9.567 * WeightKcal + 1.85 * HeightKcal - 4.68 * AgeKcal
                Kcal = Kcal * Activity

                if GoalValue == 1:
                    Kcla = Kcla - 300

                if GoalValue == 3:
                    Kcla = Kcla + 300

            Kcla = round(Kcla, 2)
            self.AnswerKcal['text'] = f'Your daily caloric \nrequirement is equal to\n {Kcla} kcal.'

        except ValueError:
            self.AnswerKcal['text'] = f' Only numbers are\n valible for calculations'

        self.ClearCalc()

    def ClearCalc(self):
        self.AgeEntryKcal.delete(0, 'end')
        self.HeightEntryKcal.delete(0, 'end')
        self.WeightEntryKcal.delete(0, 'end')

    def ManOption(self):
        self.ButtonValue += 1
        self.OptionValue = 1
        self.LoadCalc()

    def WomanOption(self):
        self.ButtonValue += 2
        self.OptionValue = 2
        self.OptionValueDel = 2
        self.LoadCalc()

    def LoadCalc(self):
        if self.ButtonValue > 4:
            self.ClearFrame()
            self.ButtonValue = 0    

        self.DataFill = Label(self.CalculatorUpSideFrame, text = 'Fill the Data: ', font = 'Helvetica 10 bold').place(x = 10, y = 10)
        self.HeightLabel = Label(self.CalculatorUpSideFrame, text = 'Height(cm): ').place(x = 10, y = 40)
        self.WeightLabel = Label(self.CalculatorUpSideFrame, text = 'Weight(kg): ').place(x = 10, y = 70)
        self.NeckLabel = Label(self.CalculatorUpSideFrame, text = 'Neck(cm): ').place(x = 10, y = 100)
        self.WaistLabel = Label(self.CalculatorUpSideFrame, text = 'Waist(cm): ').place(x = 10, y = 130)
        self.BMIAnswer = Label(self.CalculatorUpSideFrame, text = '')
        self.BFPAnswer = Label(self.CalculatorUpSideFrame, text = '')
        self.InfoAnswer = Label(self.CalculatorUpSideFrame, text = '')

        self.BMIAnswer.place(x = 143, y = 20)
        self.BFPAnswer.place(x = 143, y = 60)
        self.InfoAnswer.place(x = 135, y = 100)

        self.HeightEntry = Entry(self.CalculatorUpSideFrame, width = 5, textvariable = self.HeightValue)
        self.HeightEntry.place(x = 85, y = 40)

        self.WeightEntry = Entry(self.CalculatorUpSideFrame, width = 5, textvariable = self.WeightValue)
        self.WeightEntry.place(x = 85, y = 70)

        self.NeckEntry = Entry(self.CalculatorUpSideFrame, width = 5, textvariable = self.NeckValue)
        self.NeckEntry.place(x = 85, y = 100)

        self.WaistEntry = Entry(self.CalculatorUpSideFrame, width = 5, textvariable = self.WaistValue)
        self.WaistEntry.place(x = 85, y = 130)
            
        self.CalcButton = Button(self.CalculatorUpSideFrame, text = 'Calculate', fg = "black", width = 7, font = 'Helvetica 10 bold', command = self.CalcValue)
        self.CalcButton.place(x = 190, y = 170)

        if self.ButtonValue == 2 or self.ButtonValue == 3:
            self.HipLabel = Label(self.CalculatorUpSideFrame, text = 'Hip(cm): ').place(x = 10, y = 160)
            self.HipEntry = Entry(self.CalculatorUpSideFrame, width = 5, textvariable = self.HipValue) 
            self.HipEntry.place(x = 85, y = 160) 

    def CalcValue(self):
        Height = self.HeightValue.get()
        Weight = self.WeightValue.get()
        Neck = self.NeckValue.get()
        Waist = self.WaistValue.get()
        Hip = self.HipValue.get()

        try:
            Height = int(Height)
            Weight = int(Weight)
            Neck = int(Neck)
            Waist = int(Waist)

            self.BMI = Weight/(pow(Height/100, 2))
            self.BMI = round(self.BMI, 2)
            self.BMIAnswer['text'] = f' Your BMI is equal \nto: {self.BMI}.'

            if self.OptionValue == 1:
                self.BFP = (495/(1.0324 - 0.19077 * log10(Waist - Neck) + 0.15456 * log10(Height))) - 450
                self.BFP = round(self.BFP, 2)

            elif self.OptionValue == 2:
                Hip = int(Hip)

                self.BFP = (495/(1.29579 - 0.35004 * log10(Waist + Hip - Neck) + 0.22100 * log10(Height))) - 450
                self.BFP = round(self.BFP, 2)
            
            self.BFPAnswer['text'] = f' Your BFP is equal \nto: {self.BFP}%.'
            self.InfoAnswer['text'] = f' Check \nImortant Information \nfor more info.'

        except ValueError:
            self.BMIAnswer['text'] = ' Only numbers are\n valible for BMI'
            self.BFPAnswer['text'] = ' Only numbers are\n valible for BFP'
            self.InfoAnswer['text'] = f' Check \nImortant Information \nfor more info.'

        self.ClearEntryFrame()

    def ClearEntryFrame(self):
        self.HeightEntry.delete(0, 'end')
        self.WeightEntry.delete(0, 'end')
        self.NeckEntry.delete(0, 'end')
        self.WaistEntry.delete(0, 'end')

        if self.OptionValueDel == 2:
            self.OptionValueDel = 0
            self.HipEntry.delete(0, 'end')

    def ClearFrame(self):
        for Window in self.CalculatorUpSideFrame.winfo_children():
            Window.destroy()
            
        self.CalculatorUpSideFrameImg = Label(self.CalculatorUpSideFrame, image = self.CalculatorUpImg).place(x = -6, y = -6)

    def Info(self):
        self.Information = Toplevel()
        self.Information.geometry('800x400')
        self.Information.winfo_toplevel().title("Important information")
        self.Information.resizable(False, False)
        
        self.InfoFrame = Frame(self.Information, width = 800, height = 360, bg = 'blue')
        self.InfoFrame.place(x = 0, y = 0)

        self.InfoExitButton = Button(self.Information, text = 'Exit', fg = "black", width = 8, command = self.Exit, font = 'Helvetica 10 bold')
        self.InfoExitButton.place(x = 720, y = 365)

    def Photo(self):
        self.PreviousButton.place(x = 100, y = 8)
        self.NextButton.place(x = 400, y = 8)
        self.PhotoFame.place(x = 0, y = 0)

    def BackVariableW(self):
        self.Path = 'Img/Workout/Back/b.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Back'
        self.PhotoMax = 3
        self.Photo()
        
    def ChestVariableW(self):
        self.Path = 'Img/Workout/Chest/c.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Chest'
        self.PhotoMax = 3
        self.Photo()
        
    def ShouldersVariableW(self):
        self.Path = 'Img/Workout/Shoulders/s.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Shoulders'
        self.PhotoMax = 3
        self.Photo()

    def BicepsVariableW(self):
        self.Path = 'Img/Workout/Biceps/bi.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Biceps'
        self.PhotoMax = 3
        self.Photo()
        
    def TricepsVariableW(self):
        self.Path = 'Img/Workout/Triceps/t.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Triceps'
        self.PhotoMax = 3
        self.Photo()
        
    def LegsVariableW(self):
        self.Path = 'Img/Workout/Legs/l.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Legs'
        self.PhotoMax = 3
        self.Photo()
        
    def AbsVariableW(self):
        self.Path = 'Img/Workout/Abs/a.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Workout/Abs'
        self.PhotoMax = 3
        self.Photo()
        
    def LegsVariableS(self):
        self.Path = 'Img/Streach/Legs/sl.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Streach/Legs'
        self.PhotoMax = 3
        self.Photo()
        
    def ChestVariableS(self):
        self.Path = 'Img/Streach/Chest/sc.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Streach/Chest'
        self.PhotoMax = 3
        self.Photo()
    
    def ArmsVariableS(self):
        self.Path = 'Img/Streach/Arms/sa.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Streach/Arms'
        self.PhotoMax = 3
        self.Photo()
        
    def AbsVariableS(self):
        self.Path = 'Img/Streach/Abs/sabs.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Streach/Abs'
        self.PhotoMax = 3
        self.Photo()
        
    def OthersVariableS(self):
        self.Path = 'Img/Streach/Others/so.png'
        self.ChangeFirstPhoto()
        self.PartPath = 'Streach/Others'
        self.PhotoMax = 3
        self.Photo()

    def ChangeFirstPhoto(self):
        self.Image = ImageTk.PhotoImage(Image.open(self.Path))
        self.PhotoFame = Label(self.PhotoFrame, image = self.Image)
        self.PhotoFame.configure(image = self.Image)

    def NextPhoto(self):
        self.PhotoNumber = self.PhotoNumber + 1 
        
        if self.PhotoNumber == self.PhotoMax + 1:
            self.PhotoNumber = 1
        
        self.ChangePhoto()
        
    def PrevPhoto(self):
        self.PhotoNumber = self.PhotoNumber - 1 
        
        if self.PhotoNumber == 0:
            self.PhotoNumber = self.PhotoMax
        
        self.ChangePhoto()
        
    def ChangePhoto(self):
        self.Path = f'Img/{self.PartPath}/{self.PhotoNumber}.png'
        self.ImgNext = ImageTk.PhotoImage(Image.open(self.Path))
        self.PhotoFame.configure(image = self.ImgNext)
        self.PhotoFame.image = self.ImgNext

    def Exit(self):
        self.Information.destroy()

    def FullExit(self):
        root.destroy()

Obj = Gui(root)
root.mainloop()