import numpy as np
import pickle
import random
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics  import mean_squared_error


#=============================================================================#
# Loading the Data file #
#=============================================================================#
file = open('Q1_data/data.pkl', 'rb')
data = pickle.load(file)
print("Loaded Data Successfully!!!")
#=============================================================================#


#=============================================================================#
# Resampling Data #
# First randomly Shuffle data into 10 equal parts and then divide them into #
# 10 equal parts. 															#
#=============================================================================#
np.random.shuffle(data)

test = data[:len(data)//10]
train = data[len(data)//10:]

print("Test Data Size  : ", len(test))
print("Train Data Size : ", len(train))

random.shuffle(train)
train_y = np.asarray([[i[1]] for i in train])
test_y  = np.asarray([[i[1]] for i in test])
#=============================================================================#

#=============================================================================#
# Experiment Page #
#=============================================================================#
train_x = np.asarray([np.asarray([i[0]**j for j in range(1, 10)]) for i in train])
test_x = np.asarray([np.asarray([i[0]**j for j in range(1, 10)]) for i in test])

print("train_x Shape : ", train_x.shape)
print("train_y Shape : ", train_y.shape)
print("Shape : ", train_x[1*len(train_x)//10:(1+1)*len(train_x)//10, :5].shape)
#=============================================================================#


#=============================================================================#
# Plotting Stuff out#
#=============================================================================#
# plt.scatter(test_x[:, :1], test_y)
# plt.show()
#=============================================================================#

#=============================================================================#
# String 
string = ""
string += "Model Complexity,"
string += "Bias,"
string += "Variance,"
string += "Total Error"
string += "\n"
file2 = open('./q1.csv','w+')
min_comp = 0
min_val = 1e18
#=============================================================================#


#=============================================================================#
# Regression Part !! #
#=============================================================================#
coef = []			# Coefficient Obtained by Regression #
intercept = []		# Intercept Obtained by Regression   #
err, var, bas,nos,tot = [], [], [],[],[]
for j in range(1,10):
	prediction = np.zeros((len(test_x), 1))
	pred_array = []
	variance = 0
	mse = []
	for i in range(10) :
		if j == 1 :
			fit_intercept = False
		else :
			fit_intercept = True
		reg = LinearRegression(fit_intercept=fit_intercept, normalize = True).fit(train_x[i*len(train_x)//10:(i+1)*len(train_x)//10, :j],
								train_y[i*len(train_x)//10:(i+1)*len(train_x)//10])
		coef.append(reg.coef_)
		if fit_intercept == True :
			intercept.append(reg.intercept_)
		pred = reg.predict(test_x[:,:j])
		pred_array.append(pred)
		prediction = prediction + pred
		
	if j is 1 or j is 9 or j is 4:
		name = "q1fig"
		end = ".jpg"
		# plt.scatter(test_x,prediction)
		# plt.scatter(test_x,test_y)
		predic = reg.predict(train_x[:4500,:j])
		plt.plot(train_x[:4500,:1],predic,'bo')
		plt.plot(train_x[:4500,:1],train_y[:4500],'ro')
		plt.legend(['Prediction','Data'])
		# plt.savefig(name+str(j)+end)
		plt.show()

	pred_array = np.asarray(pred_array)
	prediction = prediction/10
	diff = pred_array - prediction
	bias = (np.mean((prediction - test_y))**2)
	variance = np.mean(diff**2)
	totalerror = bias + variance
	tot.append(totalerror)
	# err.append(np.mean(mse))
	var.append(variance)
	bas.append(bias)
	print("Model Complexity : ", j)
	print("Bias : ", bias)
	print("Variance : ", variance)
	print("Total Error : ",totalerror)
	string += str(j)
	string += ","
	string += str(bias)
	string += ","
	string += str(variance)
	string += ","
	string += str(totalerror)
	if totalerror < min_val : 
		min_comp = j
		min_val = totalerror

	if j is not 9:
		string += "\n"
		
	
var = np.array(var)
err = np.array(err)
bas = np.array(bas)
# plt.semilogy([x for x in range(1, 10)], bas*((np.max(err)-np.min(err))/(np.max(bas)-np.min(bas))), 'r+-',ms=20)
# plt.semilogy([x for x in range(1, 10)], var*((np.max(err)-np.min(err))/(np.max(var)-np.min(var))), 'b*-')
# plt.semilogy([x for x in range(1, 10)], err, 'yo-')
# plt.xlabel('Model Complexity')
plt.plot(range(1-1, 10-1), bas, 'r+-',ms=20)
plt.plot(range(1-1, 10-1), var, 'b*-')
plt.plot(range(1-1, 10-1), tot, 'g^-')
plt.axvline(x=min_comp,color='grey',linestyle='--')
# plt.s
plt.legend(['Bias^2','Variance','Total Error','Optimal Complexity'])
# plt.savefig('q1.jpg')
plt.show()
# coef = np.asarray(coef)
intercept = np.asarray(intercept)
#=============================================================================#


#=============================================================================#
# Plotting some stuff #
#=============================================================================#
test_x
file2.write(string)
file.close()
file2.close()
print("XMIN at " + str(min_comp))
#=============================================================================#

#### R Tabulate the values of bias and variance and also write a detailed report explaining how bias and variance changes as you vary your function classes.
#### Report should contain details of algorithm implementation, re-sults, tables, plots, observations and answers to the subjective questions (if any)