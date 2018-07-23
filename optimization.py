import demo 

if __name__ == '__main__':
   
   #min_learning_rate = 0.0001
   demo.run(0.0001)
   
   for i in range(55, 100):
      demo.run(float(i)/1000000)
   #new_err = (demo.run(0.0001)
   #if (float(new_err) < float(min_err)):
      #min_err = new_err
      #min_learning_rate = i 

   #print(min_err)
   #print(min_learning_rate)

   """finding the min here is difficult due to float limitations. 
      Python Decimals may be too slow."""
