import pickle 
from flask import Flask, render_template,request
import numpy as np
import pandas as pd

app= Flask(__name__,template_folder="templates")
model=pickle.load(open('model.pkl','rb'))

# load the model

@app.route('/')
def index():
    return render_template('index1.html')


# @app.route('/claim' ,methods='GET')
# def index():
#     return render_template('index.html')


company = {
    'Lexus': 0,
    'Ferrari': 1, 
    'Mecedes': 2,
    'Porche': 3,
    'Jaguar': 4,
    'BMW': 5,            
    'Nisson': 6,
    'Saturn': 7,
    'Mercury':8,
    'Dodge' : 9,
    'Saab' : 10,
    'VW' : 11,
    'Ford': 12,
    'Accura': 13,
    'Chevrolet': 14,
    'Mazda' : 15,
    'Honda' : 16,
    'Toyota' : 17,
    'Pontiac': 18
}

week = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4, 
    'Saturday': 5,
    'Sunday' : 6
}

month = {
    'Jan' : 0,
    'Feb' : 1,
    'Mar' :2,
    'Apr' : 3,
    'May': 4, 
    'Jun': 5,
    'Jul': 6,
    'Aug' : 7,
    'Sep': 8,
    'Oct' : 9,
    'Nov' : 10,
    'Dec' : 11,
    'None' : 12
}

accidentArea = {
    'Urban' : 1,
    'Rural' : 0
}

policyAccident = {
    'none' : 0,
    '1 to 7' : 1,
    '8 to 15' : 2,
    '15 to 30' :3,
    'more than 30' :4
}

policyClaim = {
    '8 to 15' : 0,
    '15 to 30' : 1,
    'more than 30' : 2
}

pastClaims = {
    'none': 0,
    '1': 1,
    '2 to 4': 2,
    'more than 4': 3
}

fault = {
    'Third Party' : 0,
    'Policy Holder' : 1
}

agentType = {
    'External':1 ,
    'Internal':0
}

policyType = {
    'Sport - Liability' : 0,
    'Sport - All Perils' : 1,
    'Utility - Liability' : 2,
    'Utility - Collision' :3,
    'Utility - All Perils' :4,
    'Sport - Collision' : 5,
    'Sedan - All Perils' : 6 ,
    'Sedan - Liability' : 7,
    'Sedan - Collision' : 8
}

vehicleCategory = {
    'Utility' : 0,
    'Sport' : 1, 
    'Sedan' : 2
}
supplements = {
    'none' : 0,
    '1 to 2' : 1,
    '3 to 5' : 2,
    'more than 5' : 3
}

addressChangeClaim = {
    'no change' : 0,
    'under 6 months' : 1,
    '1 year' : 2,
    '2 to 3 years' : 3,
    '4 to 8 years' : 4
}

numberOfCars = {
    '1 vehicle' : 0,
    '2 vehicles' : 1,
    '3 to 4' : 2,
    '5 to 8' : 3,
    'more than 8' : 4
}
basePolicy = {
    'All Perils' : 0, 
    'Liability' : 1,
    'Collision' : 2 
}
age = {
    'new' : 0,
    '2 years' : 1,
    '3 years' : 2,
    '4 years' : 3,
    '5 years' : 4, 
    '6 years' : 5,
    '7 years' : 6,      
    'more than 7' : 7
}
@app.route('/predict' , methods=['POST'])
def predict():
    if request.method =='POST':

        Month=int(request.form.get('month'))  if request.form['month'] is not None else None
        Sex = request.form.get('sex')
        Make = company[request.form.get('CarModel')]
        MaritalStatus = request.form.get('0', '') or request.form.get('1', '') or request.form.get('2', '') or request.form.get('3', '')
        
        Day = request.form.get('DayOfWeekClaimed')
        DayOfWeekClaimed = -1
        if Day is not None:
            DayOfWeekClaimed=week[Day]
        else:
            DayOfWeekClaimed=-1
        
        MonthClaimed = month[(request.form.get('monthClaimed'))]
        DayOfWeek=week[(request.form.get('DayOfWeekClaimed'))]
        Age = age[(request.form.get('Age'))]
        PolicyNumber = (request.form.get('PolicyNum'))
        AccidentArea = accidentArea[request.form.get('accident')]
        AgeOfVehicle = (request.form['AgeOfVehicle'])
        VehiclePrice = (request.form.get('VehiclePrice'))
        Days_Policy_Claim = policyClaim[(request.form.get('daysPolicyClaim'))]
        Days_Policy_Accident = policyAccident[(request.form.get('daysPolicyAccident'))]
        PastNumberOfClaims = pastClaims[(request.form.get('PastNumberOfClaims'))]
        RepNumber = (request.form.get('RepNo'))
        PoliceReportFiled = request.form.get('policeReport') == 'Yes'
        Fault=fault[request.form.get('fault')]
        WitnessPresent= request.form.get('Witness') == 'Yes'
        AgentType=agentType[request.form.get('AgentType')]
        PolicyType=policyType[request.form.get('PolicyType')]
        VehicleCategory=vehicleCategory[request.form.get('VehicleCategory')]
        Deductible=request.form.get('deductible')
        NumberOfSuppliments=supplements[(request.form.get('NumberOfSuppliments'))]
        AddressChange_Claim=addressChangeClaim[(request.form.get('AddressChange_Claim'))]
        NumberOfCars= numberOfCars[(request.form.get('NumberOfCars'))]
        Year=(request.form.get('Year'))
        BasePolicy=basePolicy[request.form.get('BasePolicy')]
    # Process the input data and make a prediction using the ML model
        input_data = [Month,DayOfWeek,Make,AccidentArea,DayOfWeekClaimed,MonthClaimed,Sex,MaritalStatus,Age,Fault,PolicyType,VehicleCategory,VehiclePrice,PolicyNumber,RepNumber,Deductible,Days_Policy_Accident,Days_Policy_Claim,PastNumberOfClaims,AgeOfVehicle,PoliceReportFiled,WitnessPresent,AgentType,NumberOfSuppliments,AddressChange_Claim,NumberOfCars,Year,BasePolicy]
        # input_array=np.array(input_data)
        data_dict = dict(zip(['Month', 'DayOfWeek', 'Make', 'AccidentArea', 'DayOfWeekClaimed', 'MonthClaimed', 'Sex', 'MaritalStatus', 'Age', 'Fault', 'PolicyType', 'VehicleCategory', 'VehiclePrice', 'PolicyNumber', 'RepNumber', 'Deductible', 'Days_Policy_Accident', 'Days_Policy_Claim', 'PastNumberOfClaims', 'AgeOfVehicle', 'PoliceReportFiled', 'WitnessPresent', 'AgentType', 'NumberOfSuppliments', 'AddressChange_Claim', 'NumberOfCars', 'Year', 'BasePolicy'], input_data))
        print(data_dict)
        df=pd.DataFrame.from_dict(data_dict,orient='index').T
        prediction = model.predict(df)
        return render_template('C:\\Users\\HP\\OneDrive\\Desktop\\amex2\\templates\\predict.html', prediction_text = 'your result is ${}'.format(prediction))

if __name__ =='__main__':
    app.run(debug=True)

