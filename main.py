import pickle 
from flask import Flask, render_template,request
import numpy as np
import pandas as pd

app= Flask(__name__,template_folder="templates")
model=pickle.load(open('model.pkl','rb'))

# load the model

@app.route('/')
def index():
    return render_template('index.html')

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
        
        MonthClaimed = (request.form.get('MonthClaimed'))
        DayOfWeek=(request.form.get('DayOfWeek'))
        Age = (request.form.get('Age'))
        PolicyNumber = (request.form.get('PolicyNum'))
        AccidentArea = request.form.get('accident')
        AgeOfVehicle = (request.form['AgeOfVehicle'])
        VehiclePrice = (request.form.get('VehiclePrice'))
        Days_Policy_Claim = (request.form.get('daysPolicyClaim'))
        Days_Policy_Accident = (request.form.get('daysPolicyAccident'))
        PastNumberOfClaims = (request.form.get('PastNumberOfClaims'))
        RepNumber = (request.form.get('RepNo'))
        PoliceReportFiled = request.form.get('policeReport') == 'Yes'
        Fault=request.form.get('fault')
        WitnessPresent= request.form.get('Witness') == 'Yes'
        AgentType=request.form.get('AgentType')
        PolicyType=request.form.get('PolicyType')
        VehicleCategory=request.form.get('VehicleCategory')
        Deductible=request.form.get('deductible')
        NumberOfSuppliments=(request.form.get('NumberOfSuppliments'))
        AddressChange_Claim=(request.form.get('AddressChange_Claim'))
        NumberOfCars= (request.form.get('NumberOfCars'))
        Year=(request.form.get('Year'))
        BasePolicy=request.form.get('BasePolicy')
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

