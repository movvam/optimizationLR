import demo 

if __name__ == '__main__':
   
   #min_learning_rate = 0.0001
   #min_err = demo.run(0.0001)
   
   for i in range(0.0001, 0.000098, -0.000001):
      demo.run(i)
   #new_err = (demo.run(0.0001)
   #if (float(new_err) < float(min_err)):
      #min_err = new_err
      #min_learning_rate = i 

   #print(min_err)
   #print(min_learning_rate)

   """finding the min here is difficult due to float limitations. 
      Python Decimals may be too slow."""
