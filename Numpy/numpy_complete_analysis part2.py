import numpy as np

price, bed , bath,house_size = np.genfromtxt(
    'RealEstate-USA.csv',
    delimiter=",",
    usecols=(2,3,4,10),
    unpack=True,
    filling_values=np.nan,
      skip_header=1
    )
bed[np.isnan(bed)] = np.nanmean(bed)
bath[np.isnan(bath)] = np.nanmean(bath)
house_size[np.isnan(house_size)] = np.nanmean(house_size)

print(price)
print(bed)
print(bath)
print(house_size)
 #Statistics operations
print('RealEstate-USA mean:' , np.mean(price))
print('RealEstate-USA median:' , np.median(price))
print("RealEstate-USA min:" , np.min(price))
print("RealEstate-USA max:", np.max(price))
print("RealEstate-USA sum:", np.sum(price))
print("RealEstate-USA std:" , np.std(price))

 #Perform basic arithmetic operations
addition = bed + bath
subtraction = bed - bath
multiplication = bed * bath
division = bed / bath
print("RealEstate-USA bed-bath-Addition:", addition)
print("RealEstate-USA bed-bath-Subtraction:",subtraction)
print("RealEstate-USA bed-bath-multiplication:",multiplication)
print("RealEstate-USA bed-bath-division:" , division)

# price  - maths operations
print("RealEstate-USA price square: " , np.square(price))
print("RealEstate-USA Price sqrt: " , np.sqrt(price))
print("RealEstate-USA Price pow: " , np.power(price,price))
print("RealEstae-USA Price abs: " , np.abs(price))
#Trigonometric Functions
pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)
print("RealEstate-USA price - div - pie - Sine vlues:" ,sine_values)
print("RealEstate-USA price - div - pie - Cosine values:" ,cosine_values)
print("RealEstate-USA price - div - pie - Tangent values:" ,tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("RealEstate-USA price - div - pie -   Natural logarithm values:", log_array)
print("RealEstate-USA price - div - pie -  Base-10 logarithm values:", log10_array)
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(price)
print("RealEstate-USA price - div - pie - hyperbolic sine:" ,sinh_values)
#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)

print("RealEstate-USA price - div - pie - hyperbolic cosine:", cosh_values)
# Calculate the inverse hyperbolic sine of each element

asinh_values = np.arcsinh(pricePie)
print("RealEstate-USA Inverse Hyperbolic Sine values:", asinh_values)

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("RealEstate-USA-Inverse Hyperbolic Sine values:", asinh_values)

#bed Plus bath - 2 dimentional arrary
D2bedbath = np.array([bed,
                  bath])

print ("RealEstate-USA-bed-plus-bath - 2 dimentional arrary - " ,D2bedbath)

# check the dimension of array1
print("RealEstate-USA-2 dimentional arrary:" , D2bedbath.ndim) 


# return total number of elements in array1
print("RealEstate-USA-total number of elements:" ,D2bedbath.size)

# return a tuple that gives size of array in each dimension
print("RealEstate-USA-size of array in each dimension" ,D2bedbath.shape)


# check the data type of array1
print("RealEstate-USA-data type:" ,D2bedbath.dtype) 

# Splicing array
D2bedbathSlice=  D2bedbath[:1,:5]
print("RealEstate-USA-Splicing array-D2bedbath[:1,:5]:" , D2bedbathSlice)
D2bedbathSlice2=  D2bedbath[:1, 4:15:4]
print("RealEstate-USA-Splicing array-D2bedbath[:1, 4:15:4]:" , D2bedbathSlice2)

#Indexing array
D2bedbathSliceItemOnly= D2bedbathSlice[0,1]
print("RealEstate-USA-Result-D2bedbathSlice[1,5] :" , D2bedbathSliceItemOnly)
D2bedbathSlice2ItemOnly=  D2bedbathSlice2[0, 2]
print("RealEstate-USA-Result - D2bedbathSlice2[0, 2]: " , D2bedbathSlice2ItemOnly)

