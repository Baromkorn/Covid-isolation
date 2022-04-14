from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Covid Isolation')
my_win.resize( 500 , 500 )
button = QPushButton('Confirm')
secret = QLabel("It's a miracle")
name = QLineEdit('')
name.setPlaceholderText('Enter you name')
score = 0
q1 = QLabel("Q1:Symptoms")
q2 = QLabel("Q2:Places you visit")
q3 = QLabel("Q3:From Q2, who did you go with?")
q4 = QLabel("Q4:Types of mask")
q5 = QLabel("Q5:Types of vaccines")
q6 = QLabel("Q6:From Q5, How many doses?")
q7 = QLabel("Q7:Hand sanitizer usage")
q8 = QLabel("Q8:Are you close to a covid-19 patient recently(4 days):")
finalresult = QLabel("")
radiobutton11 = QCheckBox( 'cough' )
radiobutton12 = QCheckBox( 'fever' )
radiobutton13 = QCheckBox( 'aches and pains' )
radiobutton14 = QCheckBox( "can't taste" )
radiobutton15 = QCheckBox( 'none' )
radiobutton21 = QCheckBox( 'market' )
radiobutton22 = QCheckBox( 'stadium' )
radiobutton23 = QCheckBox( 'airport' )
radiobutton24 = QCheckBox( 'none' )
radiobutton31 = QCheckBox( 'family' )
radiobutton32 = QCheckBox( 'friends' )
radiobutton33 = QCheckBox( 'others' )
radiobutton34 = QCheckBox( 'alone' )
radiobutton35 = QCheckBox( "didn't go" )
radiobutton41 = QCheckBox( 'n95' )
radiobutton42 = QCheckBox( 'fabric' )
radiobutton43 = QCheckBox( 'surgical' )
radiobutton44 = QCheckBox( 'KF94/KN95' )
radiobutton45 = QCheckBox( 'none' )
radiobutton51 = QCheckBox( 'Pfizer' )
radiobutton52 = QCheckBox( 'Astrazeneca' )
radiobutton53 = QCheckBox( 'Moderna' )
radiobutton54 = QCheckBox( 'Sinovac' )
radiobutton55 = QCheckBox( 'Sinofarm' )
radiobutton56 = QCheckBox( 'none' )
radiobutton61 = QCheckBox( '1' )
radiobutton62 = QCheckBox( '2' )
radiobutton63 = QCheckBox( '3' )
radiobutton64 = QCheckBox( '4' )
radiobutton71 = QCheckBox( 'Always' )
radiobutton72 = QCheckBox( 'Sometimes' )
radiobutton73 = QCheckBox( 'Never' )
radiobutton81 = QCheckBox( 'Yes' )
radiobutton82 = QCheckBox( 'No' )
submit = QPushButton("Submit")
reset = QPushButton("Reset")
# button_group1 = QButtonGroup()
# button_group2 = QButtonGroup()
# button_group3 = QButtonGroup()
# button_group4 = QButtonGroup()
# button_group5 = QButtonGroup()
# button_group6 = QButtonGroup()
# button_group7 = QButtonGroup()
# button_group8 = QButtonGroup()
# button_group1.addButton(radiobutton1, id = 1)
# button_group1.addButton(radiobutton2, id = 2)
# button_group1.addButton(radiobutton3, id = 3)
# button_group1.addButton(radiobutton4, id = 4)
v_line = QVBoxLayout()
v_line.addWidget(name)
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
h4_line = QHBoxLayout()
h5_line = QHBoxLayout()
h6_line = QHBoxLayout()
h7_line = QHBoxLayout()
h8_line = QHBoxLayout()
h9_line = QHBoxLayout()
h10_line = QHBoxLayout()
h11_line = QHBoxLayout()
h12_line = QHBoxLayout()
h13_line = QHBoxLayout()
h14_line = QHBoxLayout()
h15_line = QHBoxLayout()
h16_line = QHBoxLayout()
h17_line = QHBoxLayout()
g1 = QGroupBox(q1.text())
g1.setLayout(h2_line)
g2 = QGroupBox(q2.text())
g2.setLayout(h4_line)
g3 = QGroupBox(q3.text())
g3.setLayout(h6_line)
g4 = QGroupBox(q4.text())
g4.setLayout(h8_line)
g5 = QGroupBox(q5.text())
g5.setLayout(h10_line)
g6 = QGroupBox(q6.text())
g6.setLayout(h12_line)
g7 = QGroupBox(q7.text())
g7.setLayout(h14_line)
g8 = QGroupBox(q8.text())
g8.setLayout(h16_line)
v_line .addLayout(h1_line)
#v_line .addLayout(h2_line)
v_line .addLayout(h3_line)
#v_line .addLayout(h4_line)
v_line .addLayout(h5_line)
#v_line .addLayout(h6_line)
v_line .addLayout(h7_line)
#v_line .addLayout(h8_line)
v_line .addLayout(h9_line)
#v_line .addLayout(h10_line)
v_line .addLayout(h11_line)
#v_line .addLayout(h12_line)
v_line .addLayout(h13_line)
#v_line .addLayout(h14_line)
v_line .addLayout(h15_line)
#v_line .addLayout(h16_line)
v_line .addLayout(h17_line)
h1_line .addWidget(g1, alignment = Qt.AlignLeft)
h2_line .addWidget(radiobutton11, alignment = Qt.AlignCenter)
h2_line .addWidget(radiobutton12, alignment = Qt.AlignCenter)
h2_line .addWidget(radiobutton13, alignment = Qt.AlignCenter)
h2_line .addWidget(radiobutton14, alignment = Qt.AlignCenter)
h2_line .addWidget(radiobutton15, alignment = Qt.AlignCenter)
h3_line .addWidget(g2, alignment = Qt.AlignLeft)
h4_line .addWidget(radiobutton21, alignment = Qt.AlignCenter)
h4_line .addWidget(radiobutton22, alignment = Qt.AlignCenter)
h4_line .addWidget(radiobutton23, alignment = Qt.AlignCenter)
h4_line .addWidget(radiobutton24, alignment = Qt.AlignCenter)
h5_line .addWidget(g3, alignment = Qt.AlignLeft)
h6_line .addWidget(radiobutton31, alignment = Qt.AlignCenter)
h6_line .addWidget(radiobutton32, alignment = Qt.AlignCenter)
h6_line .addWidget(radiobutton33, alignment = Qt.AlignCenter)
h6_line .addWidget(radiobutton34, alignment = Qt.AlignCenter)
h6_line .addWidget(radiobutton35, alignment = Qt.AlignCenter)
h7_line .addWidget(g4, alignment = Qt.AlignLeft)
h8_line .addWidget(radiobutton41, alignment = Qt.AlignCenter)
h8_line .addWidget(radiobutton42, alignment = Qt.AlignCenter)
h8_line .addWidget(radiobutton43, alignment = Qt.AlignCenter)
h8_line .addWidget(radiobutton44, alignment = Qt.AlignCenter)
h8_line .addWidget(radiobutton45, alignment = Qt.AlignCenter)
h9_line .addWidget(g5, alignment = Qt.AlignLeft)
h10_line .addWidget(radiobutton51, alignment = Qt.AlignCenter)
h10_line .addWidget(radiobutton52, alignment = Qt.AlignCenter)
h10_line .addWidget(radiobutton53, alignment = Qt.AlignCenter)
h10_line .addWidget(radiobutton54, alignment = Qt.AlignCenter)
h10_line .addWidget(radiobutton55, alignment = Qt.AlignCenter)
h10_line .addWidget(radiobutton56, alignment = Qt.AlignCenter)
h11_line .addWidget(g6, alignment = Qt.AlignLeft)
h12_line .addWidget(radiobutton61, alignment = Qt.AlignCenter)
h12_line .addWidget(radiobutton62, alignment = Qt.AlignCenter)
h12_line .addWidget(radiobutton63, alignment = Qt.AlignCenter)
h12_line .addWidget(radiobutton64, alignment = Qt.AlignCenter)
h13_line .addWidget(g7, alignment = Qt.AlignLeft)
h14_line .addWidget(radiobutton71, alignment = Qt.AlignCenter)
h14_line .addWidget(radiobutton72, alignment = Qt.AlignCenter)
h14_line .addWidget(radiobutton73, alignment = Qt.AlignCenter)
h15_line .addWidget(g8, alignment = Qt.AlignLeft)
h16_line .addWidget(radiobutton81, alignment = Qt.AlignCenter)
h16_line .addWidget(radiobutton82, alignment = Qt.AlignCenter)
h17_line .addWidget(finalresult, alignment = Qt.AlignCenter)
v_line . addWidget(submit,alignment = Qt.AlignCenter)
v_line . addWidget(reset, alignment = Qt.AlignCenter)
# h5_line .addWidget(button, alignment = Qt.AlignLeft)
def result():
    global score
    if radiobutton11.isChecked():
        score+=1
    if radiobutton12.isChecked():
        score+=1
    if radiobutton13.isChecked():
        score+=1
    if radiobutton14.isChecked():
        score+=2
    if radiobutton21.isChecked():
        score+=1
    if radiobutton22.isChecked():
        score+=1
    if radiobutton23.isChecked():
        score+=1
    if radiobutton31.isChecked():
        score+=2
    if radiobutton32.isChecked():
        score+=2
    if radiobutton33.isChecked():
        score+=2
    if radiobutton34.isChecked():
        score+=1
    if radiobutton42.isChecked():
        score+=2
    if radiobutton43.isChecked():
        score+=1
    if radiobutton44.isChecked():
        score+=1
    if radiobutton56.isChecked():
        score+=3
    if radiobutton61.isChecked():
        score+=2
    if radiobutton62.isChecked():
        score+=1
    if radiobutton72.isChecked():
        score+=2
    if radiobutton73.isChecked():
        score+=4
    if radiobutton81.isChecked():
        score+=4
    tempname = name.text()
    if(score>=0 and score<=5):
        finalresult.setText(tempname+" ,you are safe")
    elif(score<=10):
        finalresult.setText(tempname+" ,you are unsafe")
    elif(score>10):
        finalresult.setText(tempname+" ,you are dangerous")
    score =0
def res():
    global score
    radiobutton11.setChecked(False)
    radiobutton12.setChecked(False)
    radiobutton13.setChecked(False)
    radiobutton14.setChecked(False)
    radiobutton15.setChecked(False)
    radiobutton21.setChecked(False)
    radiobutton22.setChecked(False)
    radiobutton23.setChecked(False)
    radiobutton24.setChecked(False)
    radiobutton31.setChecked(False)
    radiobutton32.setChecked(False)
    radiobutton33.setChecked(False)
    radiobutton34.setChecked(False)
    radiobutton35.setChecked(False)
    radiobutton41.setChecked(False)
    radiobutton42.setChecked(False)
    radiobutton43.setChecked(False)
    radiobutton44.setChecked(False)
    radiobutton45.setChecked(False)
    radiobutton51.setChecked(False)
    radiobutton52.setChecked(False)
    radiobutton53.setChecked(False)
    radiobutton54.setChecked(False)
    radiobutton55.setChecked(False)
    radiobutton56.setChecked(False)
    radiobutton61.setChecked(False)
    radiobutton62.setChecked(False)
    radiobutton63.setChecked(False)
    radiobutton64.setChecked(False)
    radiobutton71.setChecked(False)
    radiobutton72.setChecked(False)
    radiobutton73.setChecked(False)
    radiobutton81.setChecked(False)
    radiobutton82.setChecked(False)
    score = 0
    finalresult.setText("")
    # label.setText("The button selected was number" + str(button_group1.checkedId()))
    # v_line .addWidget(label, alignment = Qt.AlignCenter)
submit.clicked.connect(result)
reset.clicked.connect(res)
my_win.setLayout( v_line )
my_win.show()
app.exec_()