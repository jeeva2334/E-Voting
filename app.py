from flask import Flask, render_template, redirect, url_for, request,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from web3 import Web3
from eth_account import Account

app = Flask(__name__)
app.secret_key = "secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'voting'

mysql = MySQL(app)

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

contract_address = "0xe96678E3B9253b2541D8F632315001abC4cCCDBF"
abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "candidate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "canId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "fullname",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "party",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "gender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "voterid",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "aadharno",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "city",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "phoneno",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "voteCount",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllCandidates",
		"outputs": [
			{
				"components": [
					{
						"components": [
							{
								"internalType": "uint256",
								"name": "canId",
								"type": "uint256"
							},
							{
								"internalType": "string",
								"name": "fullname",
								"type": "string"
							},
							{
								"internalType": "uint256",
								"name": "age",
								"type": "uint256"
							},
							{
								"internalType": "string",
								"name": "party",
								"type": "string"
							},
							{
								"internalType": "string",
								"name": "gender",
								"type": "string"
							},
							{
								"internalType": "string",
								"name": "voterid",
								"type": "string"
							},
							{
								"internalType": "uint256",
								"name": "aadharno",
								"type": "uint256"
							},
							{
								"internalType": "string",
								"name": "city",
								"type": "string"
							},
							{
								"internalType": "string",
								"name": "email",
								"type": "string"
							},
							{
								"internalType": "uint256",
								"name": "phoneno",
								"type": "uint256"
							},
							{
								"internalType": "uint256",
								"name": "voteCount",
								"type": "uint256"
							}
						],
						"internalType": "struct Voter.Candidate[]",
						"name": "candidates",
						"type": "tuple[]"
					}
				],
				"internalType": "struct Voter.CandidateList",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getCandidate",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "canId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fullname",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "age",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "party",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "gender",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "voterid",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "aadharno",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "city",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "email",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "phoneno",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "voteCount",
						"type": "uint256"
					}
				],
				"internalType": "struct Voter.Candidate",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_email",
				"type": "string"
			}
		],
		"name": "getVoter",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "fullname",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "age",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "gender",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "voterid",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "aadharno",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "city",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pincode",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "email",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "phoneno",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "isVoted",
						"type": "bool"
					}
				],
				"internalType": "struct Voter.VoterReg",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "isVStarted",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_fullname",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_party",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_gender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_voterid",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_aadharno",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_city",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_phone",
				"type": "uint256"
			}
		],
		"name": "regCandidate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_fullname",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_gender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_voterid",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_aadharno",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_city",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pincode",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_phone",
				"type": "uint256"
			}
		],
		"name": "regVoter",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "result",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "startVoting",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "stop",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "vote",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

contract = web3.eth.contract(address=contract_address, abi=abi)
private_key = "0x72bf3038ede88398cbf2d8d5c9d2181371a6626c3d3d7c6eb718a30f599fc930"
account = Account.from_key(private_key)

# templates Public

@app.route('/')
def index():
    return redirect(url_for('loginpage',msg=""))

@app.route('/Register')
def register():
    return render_template('register.html')

@app.route('/loginpage')
def loginpage():
    msg = request.args.get('msg')
    return render_template('index.html',msg=msg)

@app.route('/voting')
def voting():
    msg = request.args.get('msg')
    user = session['email']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM candidates')
    can = cursor.fetchall()
    started = contract.functions.isVStarted().call()
    print(started)
    print(can)
    return render_template('VotingPage.html',user=user,can=can,res="")

@app.route('/notStarted')
def notStarted():
    user = session['email']
    return render_template('notStarted.html',user=user)

@app.route('/thanks')
def thanks():
    user = session['email']
    return render_template('ThanksPage.html',user=user)

@app.route('/results')
def results():
    user = session['email']
    res = contract.functions.result().call()
    print(int(res[1]))
    winner = contract.functions.getCandidate(int(res[1])).call()
    print(winner)
    return render_template('results.html',user=user,res=winner)

# templates Admin

@app.route('/adminlogin')
def adminlogin():
    msg = request.args.get('msg')
    return render_template('AdminLogin.html',msg=msg)

@app.route('/adminpanel')
def adminpanel():
    msg = request.args.get('msg')
    return render_template('adminpanel.html',msg=msg)

@app.route('/addcandidate')
def addcandidate():
    return render_template('AddCandidate.html')

@app.route('/viewcandidate')
def viewcandidate():
	return render_template('viewcandidate.html',res="")

@app.route('/viewvoter')
def viewvoter():
    res=""
    return render_template('viewvoter.html',res=res)
# methods

@app.route('/Login', methods =['GET', 'POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM votersLogin WHERE email = % s AND password = % s', (email, password, ))
    account = cursor.fetchone()
    print(account)
    if account:
        session['isloggedin'] = True
        session['id'] = account['id']
        session['email'] = account['email']
        started = contract.functions.isVStarted().call()
        if started == True:
            return redirect(url_for('voting',msg='Logged in successfully !'))
        else:
            return redirect(url_for('notStarted'))
    else:
        return redirect(url_for('loginpage',msg='Incorrect email / password !'))
    
file = ""
    
@app.route('/RegUser', methods =['POST'])
def reguser():
    fullname = request.form['fullname']
    age = request.form['age']
    gender = request.form.get('gender')
    voterid = request.form['voterid']
    aadharno = request.form.get('aadharno')
    city = request.form['city']
    pincode = request.form['pincode']
    email = request.form['email']
    phone = request.form.get('phone')
    password = request.form['password']
    res  = contract.functions.regVoter(fullname,int(age),gender,voterid,int(aadharno),city,pincode,email,int(phone)).transact({'from': account.address})
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO votersLogin(email,password) VALUES (% s, % s)', (email, password))
    mysql.connection.commit()
    return redirect(url_for('loginpage', msg='Registered successfully !'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('loginpage',msg=""))

@app.route('/vote')
def vote():
    email = request.args.get('email')
    id = request.args.get('id')
    print(email,id)
    res = contract.functions.vote(email,int(id)).transact({'from': account.address})
    return redirect(url_for('thanks'))

# Admin methods

@app.route('/Admin', methods =['GET', 'POST'])
def admin():
    email = request.form['email']
    password = request.form['password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM admin WHERE email = % s AND password = % s', (email, password, ))
    account = cursor.fetchone()
    if account:
        session['loggedin'] = True
        session['id'] = account['id']
        session['email'] = account['email']
        
        return redirect(url_for('adminpanel'))
    else:
        return redirect(url_for('adminlogin',msg='Incorrect email / password !'))
    
@app.route('/AddCandidateS', methods =['POST'])
def addcandidates():
    fullname = request.form['fullname']
    age = request.form['age']
    party = request.form['party']
    gender = request.form.get('gender')
    voterid = request.form['voterid']
    aadharno = request.form.get('aadharno')
    city = request.form['city']
    email = request.form['email']
    phone = request.form.get('phone')
    password = request.form['password']
    res  = contract.functions.regCandidate(fullname,int(age),party,gender,voterid,int(aadharno),city,email,int(phone)).transact({'from': account.address})
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO votersLogin(email,password) VALUES (% s, % s)', (email, password))
    cursor.execute('INSERT INTO candidates (fullname, age, party, gender, voterid, aadharno, city, email, phoneno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',(fullname,age,party,gender,voterid,aadharno,city,email,phone))
    mysql.connection.commit()
    return redirect(url_for('adminpanel', msg='Registered successfully !'))

@app.route('/ViewCandidateS', methods =['GET', 'POST'])
def viewcandidates():
    id = request.form['id']
    print(id)
    res = contract.functions.getCandidate(int(id)).call()
    print(res)
    return render_template('viewcandidate.html',res=res)

@app.route('/ViewVoterS', methods =['GET', 'POST'])
def viewvoters():
    email = request.form['email']
    res = contract.functions.getVoter(email).call()
    print(res)
    return render_template('viewvoter.html',res=res)

@app.route('/startVoting')
def startvoting():
    res = contract.functions.startVoting(7200).transact({'from': account.address})
    return redirect(url_for('adminpanel', msg='Voting Started !'))

@app.route('/endVoting')
def endvoting():
    res = contract.functions.stop().transact({'from': account.address})
    return redirect(url_for('adminpanel', msg='Voting Ended !'))

@app.route('/result')
def result():
    res = contract.functions.result().call()
    print(res)
    return redirect(url_for('results', msg=""))

@app.route('/test')
def test():
    msg = request.args.get('msg')
    res = contract.functions.getAllCandidates().call()
    return render_template('test.html',msg=msg)

    

if __name__ == '__main__':
    app.run(debug=True)