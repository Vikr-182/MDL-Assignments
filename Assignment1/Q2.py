import numpy as np
import pickle
import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.metrics  import mean_squared_error

#=============================================================================#
# Loading the Data file #
#=============================================================================#
file = open('Q2_data/Fx_test.pkl', 'rb')
test_y = pickle.load(file)
file.close()
file = open('Q2_data/X_test.pkl', 'rb')
test_x = pickle.load(file)
file = open('Q2_data/X_train.pkl', 'rb')
train_x = pickle.load(file)
file = open('Q2_data/Y_train.pkl', 'rb')
train_y = pickle.load(file)
print("Loaded Data Successfully!!!")
#=============================================================================#

#=============================================================================#
# String and other params
string = ""
string += "Model Complexity,"
string += "Bias,"
string += "Variance,"
string += "Total Error"
string += "\n"
file2 = open('./q2.csv','w+')
min_comp = 0
min_val = 1e18
#=============================================================================#


#=============================================================================#
# Resampling Data #
# First randomly Shuffle data into 10 equal parts and then divide them into #
# 10 equal parts. 															#
#=============================================================================#
for x in train_x:
	x = np.asarray(train_x)
train_x = np.asarray(train_x)
print("train_x Shape : ",train_x.shape)

for y in train_y :
	y = np.asarray(train_y)
train_y = np.asarray(train_y)
print("train_y Shape : ", train_y.shape)

test_x = np.reshape(np.asarray(test_x), (80, 1))
print("test_x Shape : ",test_x.shape)

test_y = np.reshape((np.asarray(test_y)), (80, 1))
print("test_y Shape : ", test_y.shape)


#=============================================================================#

#=============================================================================#
# Experiment Page #
#=============================================================================#
# print("train_x Shape : ", train_x.shape)
# print("train_y Shape : ", train_y.shape)
plt.scatter(train_x[5], train_y[5])
plt.savefig('q2scatter.jpg')
plt.show()
#=============================================================================#



#=============================================================================#
# Regression Part !! #
# First loop : Choose Polynomial #
# Second loop : Choose Training set #
#=============================================================================#
err, var, bas,tot = [], [], [],[]
for i in range(1,10) :
	prediction = np.zeros((80, 1))
	pred_array = []
	variance = 0
	mse = []
	for j in range(20) :
		poly = PolynomialFeatures(degree = i)
		subTr_x = np.reshape(train_x[j], (400, 1))

		subTr_y = train_y[j]
		subTr_x = poly.fit_transform(subTr_x)
		# print(subTr_x.shape)
		reg = LinearRegression().fit(subTr_x, subTr_y)
		subTs_x = test_x
		subTs_x = poly.fit_transform(subTs_x)
		pred = np.reshape(reg.predict(subTs_x), (80, 1))
		pred_array.append(pred)
		prediction = prediction + pred
		variance = variance + (pred - test_y)**2
	# if i is 1 or i is 9 or i is 4:
	# 	prediction_ = reg.predict(train_x[:smSize,:i])
	# 	plt.plot(test_x,prediction_,'bo')
	# 	plt.show()
	if i is 1 or i is 3 or i is 9:
		name = "q2fig"
		end = ".jpg"
		plt.scatter(test_x,prediction)
		plt.scatter(test_x,test_y)
		plt.legend(['Prediction','Data'])
		plt.savefig(name+str(i)+end)
		plt.show()

	pred_array = np.asarray(pred_array)
	prediction = prediction/20
	diff = pred_array - prediction
	bias = (np.mean((prediction - test_y)**2))
	variance = np.mean(diff**2)
	# err.append(np.mean(mse))
	var.append(variance)
	bas.append(bias)
	totalerror = bias + variance
	tot.append(totalerror)
	print("Model Complexity : ", i)
	print("Bias : ", bias)
	print("Variance : ", variance)
	print("Total Error: ",totalerror)
	string += str(i)
	string += ","
	string += str(bias)
	string += ","
	string += str(variance)
	string += ","
	string += str(totalerror)
	if totalerror < min_val : 
		min_comp = i
		min_val = totalerror
	if i is not 9:
		string += "\n"
	# smSize = 4500



var = np.array(var)
bas = np.array(bas)
plt.plot(range(1, 10), bas, 'r+-',ms=20)
plt.plot(range(1, 10), var, 'b*-')
plt.plot(range(1, 10), tot, 'g^-')
plt.axvline(x=min_comp,color='grey',linestyle='--',label='Anna')
plt.legend(['Bias^2','Variance','Total Error','Optimal Complexity'])
plt.savefig('q2.jpg')
plt.show()
intercept = 1
intercept = np.asarray(intercept)

#=============================================================================#

#=============================================================================#
# Plotting out of Stuff #
print("XMIN at " + str(min_comp))
file2.write(string)
file2.close()
#=============================================================================#
#=============================================================================#

### Write your observations in the report with respect to underfitting, overfitting and alsocomment on the type of data just by looking at the bias-variance plot.4
### Report should contain details of algorithm implementation, re-sults, tables, plots, observations and answers to the subjectivequestions (if any)