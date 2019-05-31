# SIMPLE SUVAT CALCULATOR
# YOUSEF ZAHER
# PHYSICS AND MECHANICS
# SyberProjects

# SOFT STAGE (ALPHA) v0.2

## EVENTS
## ------
## v0.1
## ------
## UTILISES 5 SUVAT EQUATIONS.
## AUTO-CALCULATES ALL UNKNOWNS IF POSSIBLE.
## ERROR HANDLING IMPLEMENTED.
## BASIC SUVAT
## -------
## v0.2
## -------
## OUTPUTS ORIGINAL FORMULA
## OUTPUTS REARRANGED FORMULA
## -------


## LOGS
## --------
## 1
## --------
### CURRENT RECORDED ERRORS
#-> INPUT 36, 1, 2, ?, 5
#-> OUTPUT 36, 1, 2, 48, 5
#-> REVIEW SET EQUATIONS
## RESOLVED
## --------
## 2
## --------
##-> INCORRECT ANSWERS RETRIEVED
##-> a = ((v)**2 - (u)**2)/2*s
## RESOLVED
## a = ((v)**2 - (u)**2)/(2*s)
## --------

import math

# discriminant = math.sqrt((b**2) - (4*(a)*(c)))
# Quadratic_Formula1 = (-1*(b) + discriminant)/(2*(a))
# Quadratic_Formula2 = (-1*(b) - discriminant)/(2*(a))

solutions = []
Formulae = ""
##print ('''
##SyberProjects
##Yousef Zaher
##Version 0.2
##Alpha Stage
##''')
##print ('If Unknown use "?"')
##
##try:
##  s = input('What is the displacement?')
##  if s != "?":
##    float(s)
##except ValueError:
##  print ('Displacement Adjusted to unknown value*')
##  s = "?"
##
##try:
##  u = input('What is the initial velocity?')
##  if u != "?":
##    float (u)
##except ValueError:
##  print ('Initial Velocity Adjusted to unknown value*')
##  u = "?"
##
##try:
##  v = input('What is the final velocity?')
##  if v != "?":
##    float(v)
##except ValueError:
##  print ('Final Velocity Adjusted to unknown value*')
##  v = "?"
##
##try:
##  a = input('What is the acceleration?')
##  if a != "?":
##    float(a)
##except ValueError:
##  print ('Acceleration Adjusted to unknown value*')
##  a = "?"
##
##try:
##  t = input('What is the time')
##  if t != "?":
##    float(t)
##except ValueError:
##  print ('Time Adjusted to unknown value*')
##  t = "?"

def suvat(s,u,v,a,t):
    global solution
    solutions = []
    Formulae = ""
    Run = True

    while Run:
      Solve = False
      solution = ""
      EQ = ""
      if s == "?":
          EQ = EQ + "s"
      if u == "?":
          EQ = EQ + "u"
      if v == "?":
          EQ = EQ + "v"
      if a == "?":
          EQ = EQ + "a"
      if t == "?":
          EQ = EQ + "t"

      poss = 0
      if "s" in EQ:
          poss = poss + 1
          missing = "s"
      if "v" in EQ:
          poss = poss + 1
          missing = "v"
      if "a" in EQ:
          poss = poss + 1
          missing = "a"
      if "t" in EQ:
          poss = poss + 1
          missing = "t"

      if poss == 1:
          Solve = True
          Formula = "s = vt - 1/2at^2   ->    "
          if missing == "s":
            v = float(v)
            a = float(a)
            t = float(t)
            s = v*t - 0.5*a*(t**2) # s = vt - 1/2at^2
            Formulae = Formulae + Formula + "s = vt - 1/2at^2\n"
          elif missing == "v":
            s = float(s)
            a = float(a)
            t = float(t)
            v = (s + 0.5*a*(t**2))/t
            Formulae = Formulae + Formula + "v = (s + 1/2at^2)/t\n"
          elif missing == "a":
            v = float(v)
            s = float(s)
            t = float(t)
            a = (2*v*t -2*s)/(t**2) ####
            Formulae = Formulae + Formula + "(2vt - 2s)/t^2\n"
          elif missing == "t":
            v = float(v)
            a = float(a)
            s = float(s)
            a = -0.5*a
            b = v
            c = -s
            discriminant = (b**2) - (4*(a)*(c))
            discriminant = math.sqrt(discriminant)
            Quadratic_Formula1 = (-1*(b) + discriminant)/(2*(a))
            Quadratic_Formula2 = (-1*(b) - discriminant)/(2*(a))
            Formulae = Formulae + Formula + "Quadratic Factorisation: 1/2at^2 - vt + s = 0 \n"
            if Quadratic_Formula1 > 0:
                Quadratic_Formula1 = '{:.2f}'.format(Quadratic_Formula1)
                solution = solution + 't1 = {}s \n'.format(Quadratic_Formula1)
                solutions.append(Quadratic_Formula1)
            if Quadratic_Formula2 > 0:
                Quadratic_Formula2 = '{:.2f}'.format(Quadratic_Formula2)
                solution = solution + 't2 = {}s'.format(Quadratic_Formula2)
                solutions.append(Quadratic_Formula2)
            t = solutions[0]
            print (t)
            sol = ""
            for i in range(len(t)):
                sol = sol +"t{} = {}s\n".format(i+1, t[i])

      poss = 0

      EQ = ""
      if s == "?":
          EQ = EQ + "s"
      if u == "?":
          EQ = EQ + "u"
      if v == "?":
          EQ = EQ + "v"
      if a == "?":
          EQ = EQ + "a"
      if t == "?":
          EQ = EQ + "t"

      if "s" in EQ:
          poss = poss + 1
          missing = "s"
      if "u" in EQ:
          poss = poss + 1
          missing = "u"
      if "a" in EQ:
          poss = poss + 1
          missing = "a"
      if "t" in EQ:
          poss = poss + 1
          missing = "t"
      
      if poss == 1:
          Solve = True
          Formula = "s = vt + 1/2at^2   ->    "
          if missing == "s":
            u = float(u)
            a = float(a)
            t = float(t)
            s = u*t + 0.5*a*(t**2) # s = ut + 1/2at^2
            Formulae = Formulae + Formula + "s = ut + 1/2at^2 \n"
          elif missing == "u":
            s = float(s)
            a = float(a)
            t = float(t)
            u = (s - 0.5*a*(t**2))/t
            Formulae = Formulae + Formula + "u = (s - 1/2at^2)/t \n"
          elif missing == "a":
            u = float(u)
            s = float(s)
            t = float(t)
            a = (2*s - 2*u*t)/(t**2)
            Formulae = Formulae + Formula + "a = (2s - 2ut)/t^2 \n"
          elif missing == "t":
            u = float(u)
            a = float(a)
            s = float(s)
            a = 0.5*a
            b = u
            c = -s
            discriminant = (b**2) - (4*(a)*(c))
            discriminant = math.sqrt(discriminant)
            Quadratic_Formula1 = (-1*(b) + discriminant)/(2*(a))
            Quadratic_Formula2 = (-1*(b) - discriminant)/(2*(a))
            Formulae = Formulae + Formula + "Quadratic Factorisation: 1/2at^2 + ut - s = 0\n"
            if Quadratic_Formula1 > 0:
                Quadratic_Formula1 = '{:.2f}'.format(Quadratic_Formula1)
                solution = solution + 't1 = {}s \n'.format(Quadratic_Formula1)
                solutions.append(Quadratic_Formula1)
            if Quadratic_Formula2 > 0:
                Quadratic_Formula2 = '{:.2f}'.format(Quadratic_Formula2)
                solution = solution + 't2 = {}s'.format(Quadratic_Formula2)
                solutions.append(Quadratic_Formula2)
            t = solutions
            sol = ""
            for i in range(len(t)):
                sol = sol +"t{} = {}s\n".format(i+1, t[i])

      EQ = ""
      if s == "?":
          EQ = EQ + "s"
      if u == "?":
          EQ = EQ + "u"
      if v == "?":
          EQ = EQ + "v"
      if a == "?":
          EQ = EQ + "a"
      if t == "?":
          EQ = EQ + "t"

      poss = 0

      if "v" in EQ:
          poss = poss + 1
          missing = "v"
      if "u" in EQ:
          poss = poss + 1
          missing = "u"
      if "a" in EQ:
          poss = poss + 1
          missing = "a"
      if "t" in EQ:
          poss = poss + 1
          missing = "t"
      
      if poss == 1:
          Solve = True
          Formula = "v = u + at   ->    "
          if missing == "v":
            u = float(u)
            a = float(a)
            t = float(t)
            v = u + (a*t)
            Formulae = Formulae + Formula + "v = u + at  \n"
          elif missing == "u":
            v = float(v)
            a = float(a)
            t = float(t)
            u = v - (a*t)
            Formulae = Formulae + Formula + "u = v - at\n"
          elif missing == "a":
            v = float(v)
            u = float(u)
            t = float(t)
            a = (v - u)/t
            Formulae = Formulae + Formula + "a = (v - u)/t \n"
          elif missing == "t":
            v = float(v)
            u = float(u)
            a = float(a)
            t = (v - u)/a
            Formulae = Formulae + Formula + "t = (v - u)/a \n"

      EQ = ""
      if s == "?":
          EQ = EQ + "s"
      if u == "?":
          EQ = EQ + "u"
      if v == "?":
          EQ = EQ + "v"
      if a == "?":
          EQ = EQ + "a"
      if t == "?":
          EQ = EQ + "t"

      poss = 0
      if "s" in EQ:
          poss = poss + 1
          missing = "s"
      if "u" in EQ:
          poss = poss + 1
          missing = "u"
      if "v" in EQ:
          poss = poss + 1
          missing = "v"
      if "t" in EQ:
          poss = poss + 1
          missing = "t"
      
      if poss == 1:
          Solve = True
          Formula = "s = 1/2(u + v)t   ->    "
          if missing == "s":
            u = float(u)
            v = float(v)
            t = float(t)
            s = 0.5*t*(u+v)
            Formulae = Formulae + Formula + "s = 1/2(u + v)t \n"
          elif missing == "u":
            v = float(v)
            t = float(t)
            s = float(s)
            u = (2*s - v*t)/t
            Formulae = Formulae + Formula + "u = (2s - vt)/t \n"
          elif missing == "v":
            s = float(s)
            t = float(t)
            u = float(u)
            v = (2*s - u*t)/t
            Formulae = Formulae + Formula + "v = (2s - ut)/t \n"
          elif missing == "t":
            s = float(s)
            u = float(u)
            v = float(v)
            t = 2*s / (u+v)
            Formulae = Formulae + Formula + "t = 2s/(u + v) \n"


      EQ = ""
      if s == "?":
          EQ = EQ + "s"
      if u == "?":
          EQ = EQ + "u"
      if v == "?":
          EQ = EQ + "v"
      if a == "?":
          EQ = EQ + "a"
      if t == "?":
          EQ = EQ + "t"

      poss = 0
      if "v" in EQ:
          poss = poss + 1
          missing = "v"
      if "u" in EQ:
          poss = poss + 1
          missing = "u"
      if "a" in EQ:
          poss = poss + 1
          missing = "a"
      if "s" in EQ:
          poss = poss + 1
          missing = "s"
      
      if poss == 1:
          Solve = True
          Formula = "v^2 = u^2 + 2as   ->    "
          if missing == "v":
            u = float(u)
            a = float(a)
            s = float(s)
            v = math.sqrt((u**2) + 2*a*s)
            Formulae = Formulae + Formula + "v = u + √2as\n"
          elif missing == "u":
            v = float(v)
            a = float(a)
            s = float(s)
            u = math.sqrt((v**2) - 2*a*s)
            Formulae = Formulae + Formula + "u = v -  √2as"
          elif missing == "a":
            v = float(v)
            s = float(s)
            u = float(u)
            a = (((v)**2) - ((u)**2))/(2*s)
            Formulae = Formulae + Formula + "a = (v^2 - u^2)/(2s)"
          
          elif missing == "s":
            v = float(v)
            a = float(a)
            u = float(u)
            s = ((v**2) - (u**2))/(2*a)
            Formulae = Formulae + Formula + "s = (v^2 - u^2)/(2a)"


      Check = 0 
      if s != "?":
          Check = Check + 1
      if u != "?":
          Check = Check + 1
      if v != "?":
          Check = Check + 1
      if a != "?":
          Check = Check + 1
      if t != "?":
          Check = Check + 1
      
      if Check == 5:
          Run = False
      
      if Solve == False:
          print ('Solved to the maximum limit')
          Run = False
      
      if s != "?":
        s = "{:.2f}".format(s)

      if u != "?":
        u = "{:.2f}".format(u)

      if v != "?":
        v = "{:.2f}".format(v)

      if a != "?":
        a = "{:.2f}".format(a)

      if t != "?":
        t = "{:.2f}".format(t)

      if solution == "":
        print ('''
        displacement - {} m
        initial velocity - {} ms^-1
        final velocity - {} ms^-1
        acceleration - {} ms^-2
        time - {} s
        '''.format(s,u,v,a,t))
      else:
        print ('''
        displacement - {} m
        initial velocity - {} ms^-1
        final velocity - {} ms^-1
        acceleration - {} ms^-2
        time - {} s
        '''.format(s,u,v,a,solution))

      print ("\nFormulae Used:\n-------------\n{}".format(Formulae))
      return s,u,v,a,t
      # if u != "?" and a != "?" and t != "?":
      #   s = u*t + 0.5*a*(t**2) # s = ut + 1/2at^2
      #   print (s)

      # if u != "?" and a != "?" and t != "?":
      #   v = u + (a*t) # v = u + at
      #   print (v)

      # if u != "?" and v !+ "?" and t != "?":
      #   s = 0.5*(u+v)*t #s = 1/2 (u + v)t
      #   print (s)

      # if u != "?" and a != "?" and s != "?": 
      #   v = math.sqrt(u**2 + 2*(a)*(s)) #v^2 = u^2 + 2as
      #   print (v)
