from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

# Create the linear solver with the GLOP backend.
solver = pywraplp.Solver.CreateSolver('GLOP')

# Create the variables x and y.
S1 = solver.NumVar(0, solver.infinity(), 'S1')
S2 = solver.NumVar(0, solver.infinity(), 'S2')
S3 = solver.NumVar(0, solver.infinity(), 'S3')
S4 = solver.NumVar(0, solver.infinity(), 'S4')
S5 = solver.NumVar(0, solver.infinity(), 'S5')
S6 = solver.NumVar(0, solver.infinity(), 'S6')

print('Number of variables =', solver.NumVariables())

# Create a linear constraint, 0 <= x + y <= 2.
solver.Add((62*S1)+(50*S2)+(59*S3)+(50*S4)+(59*S5) >=S6)
solver.Add((65*S1)+(65*S2)+(68*S3)+(59*S4)+(68*S5)>=S6)
solver.Add((59*S1)+(50*S2)+(65*S3)+(50*S4)+(62*S5)>=S6)
solver.Add((68*S1)+(65*S2)+(68*S3)+(65*S4)+(68*S5)>=S6)
solver.Add((56*S1)+(56*S2)+(65*S3)+(40*S4)+(68*S5)>=S6)
solver.Add(S1+S2+S3+S4+S5==1)
# ct1.SetCoefficient(s6, -1)

print('Number of constraints =', solver.NumConstraints())

# Create the objective function, 3 * x + y.
solver.Maximize(1*S6)



status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('S6 =', S6.solution_value())
    print('S5 =', S5.solution_value())
    print('S4 =', S4.solution_value())
    print('S3 =', S3.solution_value())
    print('S2 =', S2.solution_value())
    print('S1 =', S1.solution_value())
else:
    print('The problem does not have an optimal solution.')
