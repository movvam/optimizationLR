from numpy import *

def compute_error_for_line_given_points(b,m,points):
   totalError = 0

   for i in range(len(points)):
      x = points[i,0]
      y = points[i,1]
      totalError += (y - (m*x+b)) ** 2

   return totalError/float(len(points))

def step_gradient(b_current,m_current, points,learningRate):
   #gradient descent
   b_gradient = 0
   m_gradient = 0
   N = float(len(points))
   
   for i in range(len(points)):
      x = points[i,0]
      y = points[i,1]
      b_gradient += -(2/N) * (y - (m_current*x) + b_current)
      m_gradient += -(2/N) * (x * (y - (m_current*x) + b_current))
   new_b = b_current - (learningRate * b_gradient)
   new_m = m_current - (learningRate * m_gradient)

   return [new_b,new_m]


def gradient_descent_runner(points,starting_b, starting_m, learning_rate, num_iterations):
   b = starting_b
   m = starting_m

   for i in range(num_iterations):
      b, m = step_gradient(b,m,array(points), learning_rate) # points is an array of tuples

   return [b,m]

def run():
   input_var = input("Enter a float: ")
   
   
   points = genfromtxt('data.csv',delimiter=',')
   #hyperparameters
   learning_rate = float(input_var)#0.0001
   #y = mx+b
   initial_b = 0
   initial_m = 0
   num_iterations = 1000
   
   initial_error = compute_error_for_line_given_points(initial_b, initial_m, points)

   print "Starting gradient descent at b = {0}, m = {1}, error = {2}\n".format(initial_b, initial_m, initial_error)
   print "Running...\n"
   [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
   
   new_error = compute_error_for_line_given_points(b, m, points)
   print "After {0} iterations b = {1}, m = {2}, error = {3}\n".format(num_iterations, b, m, new_error)

   f=open("errorOutput.txt", "a+")
   f.write("The new error is %f" %(new_error) )
   f.write("   The difference in error is %f\n" %(initial_error - new_error))
   f.close()




if __name__ == '__main__':
   run()
