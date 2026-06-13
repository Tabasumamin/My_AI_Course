import numpy as np

latitude,longitude = np.genfromtxt('FastFoodRestaurants.csv',
                                                
 delimiter=',',
 usecols=(4,5),
 unpack=True,
 filling_values=np.nan, 
 invalid_raise=False,  
 skip_header=1,
)
latitude[np.isnan(latitude)] = np.nanmean(latitude)
longitude[np.isnan(longitude)] = np.nanmean(longitude)
print(latitude)
print(longitude)
#Statistics Operations
print("FastFoodResturants mean:" , np.mean(longitude))
print("FastFoodResturants median:" , np.median(longitude))
print("FastFoodResturants min:" , np.min(longitude))
print("FastFoodResturants max:", np.max(longitude))
print("FastFoodResturants sum:", np.sum(longitude))
print("FastFoodResturants std:" , np.std(longitude))


#Perform basic Arithmetic operations
addition = longitude + latitude
subtraction = longitude - latitude
multiplication = longitude * latitude
division = longitude / latitude

print("FastFoodResturants longitude-latitude-Addition:", addition)
print("FastFoodResturants longitude-latitude-Subtraction:",subtraction)
print("FastFoodResturants longitude-latitude-multiplication:",multiplication)
print("FastFoodResturants longitude-latitude-division:" , division)
#Maths operations
print("FastFoodResturants latitude square: " , np.square(latitude))
print("FastFoodResturants latitude sqrt: " , np.sqrt(latitude))
print("FastFoodResturants latitude pow: " , np.power(latitude,2))
print("FastFoodResturants latitude abs: " , np.abs(latitude))
#Trigonometric Functions
latitudePie = (latitude/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(latitudePie)
cosine_values = np.cos(latitudePie)
tangent_values = np.tan(latitudePie)
print("FastFoodResturants latitude - div - pie - Sine vlues:" ,sine_values)
print("FastFoodResturants latitude - div - pie - Cosine values:" ,cosine_values)
print("FastFoodResturants latitude - div - pie - Tangent values:" ,tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(latitudePie)
log10_array = np.log10(latitudePie)

print("FastFoodResturants longitude - div - pie -   Natural logarithm values:", log_array)
print("FastFoodResturants longitude - div - pie -  Base-10 logarithm values:", log10_array)
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(latitude)
print("FastFoodResturants latitude - div - pie - hyperbolic sine:" ,sinh_values)
#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(latitudePie)

print("FastFoodResturants longitude - div - pie - hyperbolic cosine:", cosh_values)
# Calculate the inverse hyperbolic sine of each element

asinh_values = np.arcsinh(latitudePie)
print("FastFoodResturants Inverse Hyperbolic Sine values:", asinh_values)

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(latitudePie)
print("FastFoodResturants-Inverse Hyperbolic Sine values:", asinh_values)

#longitude Plus latitude - 2 dimentional arrary
D2longitudelatitude = np.array([longitude,latitude]
                  )

print ("FastFoodResturants-longitude-plus-latitude -2 dimentional arrary - " ,D2longitudelatitude)

# check the dimension of array1
print("FastFoodResturants-2 dimentional arrary:" , D2longitudelatitude.ndim) 


# return total number of elements in array1
print("FastFoodResturants-total number of elements:" ,D2longitudelatitude.size)

# return a tuple that gives size of array in each dimension
print("FastFoodResturants-size of array in each dimension" ,D2longitudelatitude.shape)


# check the data type of array1
print("FastFoodResturants-data type:" ,D2longitudelatitude.dtype) 

# Splicing array
D2longitudelatitudeSlice=  D2longitudelatitude[:1,:5]
print("FastFoodResturants-Splicing array-D2longitudelatitude[:1,:5]:" , D2longitudelatitudeSlice)
D2longitudelatitudeSlice2=  D2longitudelatitude[:1, 4:15:4]
print("FastFoodResturants-Splicing array-D2longitudelatitude[:1, 4:15:4]:" , D2longitudelatitudeSlice2)

#Indexing array
D2longitudelatitudeSliceItemOnly= D2longitudelatitudeSlice[0,1]
print("FastFoodResturants-Result-D2longitudelatitudeSlice[1,5] :" , D2longitudelatitudeSliceItemOnly)
D2longitudelatitudeSlice2ItemOnly=  D2longitudelatitudeSlice2[0, 2]
print("FastFoodResturants-Result - D2longitudelatitudeSlice2[0, 2]: " , D2longitudelatitudeSlice2ItemOnly)

