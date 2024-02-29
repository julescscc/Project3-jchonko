from direct.showbase.ShowBase import ShowBase
import sys, math
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths


class SpaceJam(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

        self.accept('escape', self.quit)

        base.disableMouse()
        
        #x = base.mouseWatcherNode.getMouseX()
        #y = base.mouseWatcherNode.getMouseY()


    def SetupScene(self):

        #Universe, Planets, Player, Space Station setup
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/universe.jpg", (0, 0, 0), 10000)
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/planet1.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/planet2.jpg", (0, 6000, 0), 300)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/planet3.jpg", (500, -5000, 200), 500)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/planet4.jpg", (300, 6000, 500), 150)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/planet5.jpg", (700, -2000, 100), 500)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/planet6.jpg", (0, -900, -1400), 700)
        self.Player = spaceJamClasses.Player(self.loader, "./Assets/Spaceships/Khan/Khan.x", self.render, 'Player', "./Assets/Spaceships/Khan/Khan.jpg", (100, -1000, -100), 1, 'manager')
        self.SpaceStation = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation/spaceStation.x", self.render, 'SpaceStation', "./Assets/Space Station/SpaceStation/SpaceStation1_Dif2.png", (500, -1000, 0), 30)

        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount +- 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.Planet2, nickName, j, fullCycle, 2)
            
        halfCycle = 30
        for j in range(halfCycle):
            spaceJamClasses.Drone.droneCount +- 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawXYplane()
            self.DrawXZplane()
            self.DrawYZplane()

    def SetCamera(self):
            self.disableMouse()
            self.camera.reparentTo(self.Player.modelNode)
            self.camera.setFluidPos(0, 1, 0)

    def DrawCloudDefense(self, centralObject, droneName):
            unitVec = defensePaths.Cloud()
            unitVec.normalize()
            position = unitVec * 500 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
            unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
            unitVec.normalize()
            position = unitVec * radius * 250 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawXYplane(self):
        self.parent = self.loader.loadModel("./Assets/Drone Defender/DroneDefender/DroneDefender.x")
        theta = 0.0
        inc = 0.2
        radius = 50.0

        for i in range(30):
            posVec = (radius * math.cos(theta), radius * math.sin(theta), 0)
            self.placeholder = self.render.attachNewNode("Placeholder")
            self.placeholder.setPos(posVec)
            self.placeholder.setColor(255, 0, 0, 1)
            self.parent.instanceTo(self.placeholder)
            theta += inc

    def DrawXZplane(self):
        self.parent = self.loader.loadModel("./Assets/Drone Defender/DroneDefender/DroneDefender.x")
        theta = 0.0
        inc = 0.2
        R = 50.0

        for i in range(30):
            posVec = (R * math.cos(theta), 0, R * math.sin(theta))
            self.placeholder = self.render.attachNewNode("Placeholder")
            self.placeholder.setPos(posVec)
            self.placeholder.setColor(0, 255, 0, 1)
            self.parent.instanceTo(self.placeholder)
            theta += inc

    def DrawYZplane(self):
        self.parent = self.loader.loadModel("./Assets/Drone Defender/DroneDefender/DroneDefender.x")
        theta = 0.0
        inc = 0.2
        R = 50.0

        for i in range(30):
            posVec = (0, R * math.cos(theta), R * math.sin(theta))
            self.placeholder = self.render.attachNewNode("Placeholder")
            self.placeholder.setPos(posVec)
            self.placeholder.setColor(0, 0, 255, 1)
            self.parent.instanceTo(self.placeholder)
            theta += inc


    def quit(self):
        sys.exit()


app = SpaceJam()
app.run()