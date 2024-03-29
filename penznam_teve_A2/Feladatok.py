#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image
import Feladatok

class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        # self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        # kepek
        self.kep1 = Image(ImageFile.CRAZY_1)
        self.kep2 = Image(ImageFile.CRAZY_2)
        self.kep3 = Image(ImageFile.DIZZY)
        

    def elore(self, hossz):
        self.robot.settings(straight_speed=250, straight_acceleration=100, turn_rate=100)
        self.robot.drive(hossz,0)
        wait(1000)
        self.robot.stop(Stop.BRAKE)

    def fordul(self):
        self.robot.settings(straight_speed=250, straight_acceleration=100, turn_rate=100)
        self.robot.drive(0, -90)
        wait(1000)
        self.robot.stop(Stop.BRAKE)

    def versenyKozeprol(self):
        self.robot.settings(straight_speed=900)
        self.robot.straight(1650)
        wait(1000)
        self.robot.turn(-100)
        wait(1000)
        self.robot.straight(1300)
        wait(1000)
        self.robot.turn(-99)
        wait(1000)
        self.robot.straight(2100)
        wait(1000)                      #középről indul
        self.robot.turn(-99)
        wait(1000)
        self.robot.straight(1300)
        wait(1000)
        self.robot.turn(-98)
        wait(1000)
        self.robot.straight(500)
        wait(1000)
        self.robot.stop(Stop.BRAKE)

    def versenySzelerol(self):
        self.robot.settings(straight_speed=900)
        self.robot.straight(1650)
        wait(1000)
        self.robot.turn(-100)
        wait(1000)
        self.robot.straight(1300)
        wait(1000)
        self.robot.turn(-99)
        wait(1000)
        self.robot.straight(2100)
        wait(1000)                      #széléről indul 
        self.robot.turn(-99)
        wait(1000)
        self.robot.straight(1300)
        wait(1000)
        self.robot.turn(-98)
        wait(1000)
        self.robot.straight(500)
        wait(1000)
        self.robot.stop(Stop.BRAKE)

   # def kepernyoreIras(self):
        wait(1000)
        self.ev3.screen.load_image(self.kep1)
        wait(500)
        self.ev3.screen.load_image(self.kep2)
        wait(500)
        self.ev3.screen.load_image(self.kep3)
        wait(1000)
        self.ev3.screen.load_image(self.kep1)
        wait(1000)
