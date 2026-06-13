import numpy as np

Growth_Rate = np.genfromtxt("startup_growth_investment_data.csv" ,delimiter=",",
    usecols=8,
    unpack=True,
      skip_header=1
      )
print(Growth_Rate)

#Statistics operations
print('startup_growth_investment_data mean:' , np.mean(Growth_Rate))
print('startup_growth_investment_data median:' , np.median(Growth_Rate))
print("startup_growth_investment_data min:" , np.min(Growth_Rate))
print("startup_growth_investment_data max:", np.max(Growth_Rate))
print("startup_growth_investment_data sum:", np.sum(Growth_Rate))
print("startup_growth_investment_data std:" , np.std(Growth_Rate))

#Perform basic arithmetic operations
addition = Growth_Rate + 24
subtraction = Growth_Rate - 4
multiplication = Growth_Rate * 2
division = Growth_Rate / 2
print("startup_growth_investment_data_Addition:", addition)
print("startup_growth_investment_data_Subtraction:",subtraction)
print("startup_growth_investment_data_multiplication:",multiplication)
print("startup_growth_investment_data_division:" , division)

#Maths operations
print("startup_growth_investment_data square: " , np.square(Growth_Rate))
print("startup_growth_investment_data sqrt: " , np.sqrt(Growth_Rate))
print("startup_growth_investment_data pow: " , np.power(Growth_Rate,Growth_Rate))
print("startup_growth_investment_data abs: " , np.abs(Growth_Rate))

# 1. prod value 
prod_value = np.prod(Growth_Rate)
print("Product:", prod_value)

# 2. Variance value

var_value = np.var(Growth_Rate)
print("Variance:", var_value)
 #Trigonometric Functions
sin_val = np.sin(Growth_Rate)
cos_val = np.cos(Growth_Rate)
tan_val = np.tan(Growth_Rate)

print("Sin:", sin_val[:5])
print("Cos:", cos_val[:5])
print("Tan:", tan_val[:5])

#Log values (ln & log10)
ln_val = np.log(Growth_Rate)
log10_val = np.log10(Growth_Rate)

print("Natural Log:", ln_val[:5])
print("Log10:", log10_val[:5])

#Inverse Hyperbolic Sine
arcsinh_val = np.arcsinh(Growth_Rate)
print("Arcsinh:", arcsinh_val[:5])
