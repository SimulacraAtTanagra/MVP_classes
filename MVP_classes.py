# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:16:35 2021

@author: shane
"""
Purpose="""
Simple M.V.P. questionaire to guide development processes based on my 5-stage
model balancing ease of use, ease of assembly, ease of repair, materials, and
force multiplication.

Desired end result is a simple program that allows easy categorization of ideas
within the model and recommends next steps to the users. Data should be packaged
for storage or use by other projects.
"""
import ast

#meta stage to create all the stages
class stage:
    def __init__(
            self,Number=False,
            Assembly=False,
            Repair=False,
            Material=False,
            ):  #if we already know the properties, let's establish them
        if Number:
            self.number=Number
        if Assembly:
            self.assembly=Assembly
        if Repair:
            self.repair=Repair
        if Material:
            self.material=self.materials[Material]
        self.up=self.ups[self.number]
        self.down=self.downs[self.number]
    def assessment(self):   #if we don't already know the properties, define them
        self.assembly=ast.literal_eval(input("Is this idea easy to assemble? True/False"))
        self.repair=ast.literal_eval(input("Is this idea easy to repair? True/False"))
        print([f'{ix}. {i}' for ix,i in enumerate(self.materials)])
        self.material=self.materials[
                int(
                input("Which number from the above list best describes the materials involved in your idea?"
                ))]
    def print_props(self):  #and now to display some data for the user
        print(f"This is a stage {self.number} idea.")
        print(f"This idea is {self.booldict[self.assembly]} to assemble and {self.booldict[self.repair]} to repair.")
        print(f"This idea is likely made with {self.materials[self.number]} materials.")
        print(f"This idea is {self.powereds[self.number]}.")
        print(f"If you want to escalate this idea to the next stage, increasing its complexity for innovation, do the following:\n{self.ups[self.number]}")
        print(f"If you want to reduce this idea to the previous stage, reducing its complexity for initial creation, do the following:\n{self.downs[self.number]}")
    booldict={0:'difficult',1:'easy'}
    number=0
    assembly=False
    repair=False
    powereds={1:"completely human powered",2:"completely human powered",3:"partially human powered",4:"externally powered",5:"externally powered"}
    materials={1:'common',2:'common',3:'uncommon',4:'rare',5:'rare'}
    ups={1:"Allow people to more easily navigate by adding functionality.",
         2:"Add functionality that acts as a force multiplier. Make it comfortable to wield often.",
         3:"Add a component which removes the need for the majority of human effort.",
         4:"Full redesign so that the process is effortless, beyond efficient completeness, and very complex.",
         5:"There is no further room for development at this stage and along this dimension"
            }
    downs={1:"There is no further room for simplification at this stage and along this dimension",
         2:"Remove parts intended for ease of use. Leave base design with most basic materials",
         3:"Remove automation. Use more common components.",
         4:"Add ability for product to be assembled by a knowledgeable user. Increase human energy required for use. Simplify design.",
         5:"Add ability for product to be fixable by a knowledgeable user. Offset reduced capability for intuitive design for use."
            }
class stage1():
    #TODO fix this. Figure out how to game inheritence into allowing you to 
    def __init__(self,stage):
        self.print_props()
    
if __name__=="__main__":
    x=stage(Number=1,Assembly=True,Repair=True,Material=0)
    x.print_props()