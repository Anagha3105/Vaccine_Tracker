from  flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def home():
	return render_template('index.html')


@app.route('/submit', methods =['GET', 'POST'])
def compute():
	if request.method == 'POST':
		print ("hello")
		name = request.form.get("name")
		age = request.form.get("age")
		if age is None:
			age=0
		gender = request.form.get('gender')
		health = request.form.get('health')
		essential = request.form.get('essential')
		comorb = request.form.get('comorb')
		activity = request.form.get('activity')
		hot = request.form.get('hot')
		wfh = request.form.get('wfh')
		antibody = request.form.get('antibody')

		a=0
		if health=="yes":
			time= "January 2021"
			a=a+30
		elif essential=="yes":
			time= "February 2021"
			a=a+20
		
		if int(age)>=60:
			a=a+20
		elif int(age)>=50:
			a+a+10
		if comorb=="yes":
			a=a+10
		if activity=="sed":
			a=a+20
		elif activity=="act":
			a=a+10
		if hot=="yes":
			a=a+10
		if wfh=="no":
			a=a+10
		if antibody=="no":
			a=a+10
			
		
		riskf =(a/110)*100
		if health=="yes":
			time= "January 2021"
			risk="high risk"
		elif essential=="yes":
			time= "February 2021"
			risk="high risk"
		elif a<30:
			risk="low risk"
			time="June 2021"
		elif a>=30 and a<70:
			risk="moderate risk"
			time="April to May 2021"
		else:
			risk="high risk"
			time= "March 2021"
			
		return render_template('output.html', riskf=riskf, risk=risk, time=time)
		
	else:
		return render_template('index.html')



if __name__=="__main__":
	app.run(debug=True)








	