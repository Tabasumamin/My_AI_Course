import numpy as np

Assessed_Value,Sale_Amount = np.genfromtxt("Real_Estate_Sales_2001-2022_GL-Short.csv" ,
   delimiter=",",
   usecols=(5,6),
   unpack=True ,
   filling_values=np.nan, 
    invalid_raise=False, 
   skip_header=1)

print(Assessed_Value)
print(Sale_Amount)

#Statistics operations
print('Real_Estate_Sales_2001-2022_GL-Short mean:' , np.mean(Assessed_Value))
print('Real_Estate_Sales_2001-2022_GL-Short median:' , np.median(Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short min:" , np.min(Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short max:", np.max(Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short sum:", np.sum(Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short std:" , np.std(Assessed_Value))

 # Arithmetic operations
addition = Assessed_Value + 4
subtraction = Assessed_Value - 6
multiplication = Assessed_Value * 2
division = Assessed_Value / 4
print("Real_Estate_Sales_2001-2022_GL-Short-Addition:", addition)
print("Real_Estate_Sales_2001-2022_GL-Short-Subtraction:",subtraction)
print("Real_Estate_Sales_2001-2022_GL-Short-multiplication:",multiplication)
print("Real_Estate_Sales_2001-2022_GL-Short-division:" , division)

#Maths operations
print("Real_Estate_Sales_2001-2022_GL-Short Assessed_Value square: " , np.square(Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short Assessed_Value sqrt: " , np.sqrt(Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short Assessed_Value pow: " , np.power(Assessed_Value,Assessed_Value))
print("Real_Estate_Sales_2001-2022_GL-Short Assessed_Value abs: " , np.abs(Assessed_Value))

#Trigonometric Functions
pricePie = (Assessed_Value/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)
print("Real_Estate_Sales_2001-2022_GL-Short_ Sine vlues:" ,sine_values)
print("Real_Estate_Sales_2001-2022_GL-Short_Cosine values:" ,cosine_values)
print("Real_Estate_Sales_2001-2022_GL-Short_Tangent values:" ,tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("Real_Estate_Sales_2001-2022_GL-Short_Natural logarithm values:", log_array)
print("Real_Estate_Sales_2001-2022_GL-Short_Base-10 logarithm values:", log10_array)

# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(Assessed_Value)
print("Real_Estate_Sales_2001-2022_GL_Short_hyperbolic sine:" ,sinh_values)
#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("Real_Estate_Sales_2001-2022_GL_Short_hyperbolic cosine:", cosh_values)

# Calculate the inverse hyperbolic sine of each element

asinh_values = np.arcsinh(pricePie)
print("Real_Estate_Sales_2001-2022_GL_Short_Inverse Hyperbolic Sine values:", asinh_values)


#bed Plus bath - 2 dimentional arrary
D2Assessed_ValueSale_Amount = np.array([Assessed_Value,Sale_Amount
                  ])

print ("Real_Estate_Sales_2001-2022_GL_Short_2 dimentional arrary - " ,D2Assessed_ValueSale_Amount)

# check the dimension of array1
print("Real_Estate_Sales_2001-2022_GL_Short_2 dimentional arrary:" , D2Assessed_ValueSale_Amount.ndim) 


# return total number of elements in array1
print("Real_Estate_Sales_2001-2022_GL_Short_total number of elements:" ,D2Assessed_ValueSale_Amount.size)

# return a tuple that gives size of array in each dimension
print("Real_Estate_Sales_2001-2022_GL_Short_size of array in each dimension" ,D2Assessed_ValueSale_Amount.shape)


# check the data type of array1
print("Real_Estate_Sales_2001-2022_GL_Short_data type:" ,D2Assessed_ValueSale_Amount.dtype) 

# Splicing array
D2Assessed_ValueSale_AmountSlice=  D2Assessed_ValueSale_Amount[:1,:5]
print("Real_Estate_Sales_2001-2022_GL_Short_Splicing array-D2Assessed_ValueSale_Amount[:1,:5]:" , D2Assessed_ValueSale_AmountSlice)
D2Assessed_ValueSale_AmountSlice2=  D2Assessed_ValueSale_Amount[:1, 4:15:4]
print("Real_Estate_Sales_2001-2022_GL_Short_Splicing array-D2Assessed_ValueSale_Amount[:1, 4:15:4]:" , D2Assessed_ValueSale_AmountSlice2)

#Indexing array
D2Assessed_ValueSale_AmountSliceItemOnly= D2Assessed_ValueSale_AmountSlice[0,1]
print("Real_Estate_Sales_2001-2022_GL_Short_Result-D2Assessed_ValueSale_AmountSlice[1,5] :" , D2Assessed_ValueSale_AmountSliceItemOnly)
D2Assessed_ValueSale_AmountSlice2ItemOnly=  D2Assessed_ValueSale_AmountSlice2[0, 2]
print("Real_Estate_Sales_2001-2022_GL_Short_Result_D2Assessed_ValueSale_AmountSlice2[0, 2]: " , D2Assessed_ValueSale_AmountSlice2ItemOnly)









