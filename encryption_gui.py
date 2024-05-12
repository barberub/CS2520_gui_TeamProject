# Most GUI Parts Created by: PyQt6 UI code generator 6.7.0

# Authors: Ruben Barbero, Marie Philavong, Leonardo Davalos

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import encryptionRSA
from encryptionSimple import caesar_cipher, substitution_cipher, substitution_decrypt, vigenere_encrypt, vigenere_decrypt
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 495)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.inputLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.outputLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 0, 2, 1, 1)
        self.inputField = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.inputField.setObjectName("inputField")
        self.gridLayout.addWidget(self.inputField, 1, 0, 1, 2)
        self.outputField = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.outputField.setObjectName("outputField")
        self.gridLayout.addWidget(self.outputField, 1, 2, 1, 1)
        self.encryptButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.encryptButton.setObjectName("encryptButton")
        self.gridLayout.addWidget(self.encryptButton, 2, 0, 1, 1)
        self.decryptButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decryptButton.setObjectName("decryptButton")
        self.gridLayout.addWidget(self.decryptButton, 2, 1, 1, 1)
        self.moveInputToOutput = QtWidgets.QPushButton(parent=self.centralwidget)
        self.moveInputToOutput.setObjectName("moveInputToOutput")
        self.gridLayout.addWidget(self.moveInputToOutput, 2, 2, 1, 1)
        self.encryptionOptions = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.encryptionOptions.setToolTipDuration(0)
        self.encryptionOptions.setObjectName("encryptionOptions")
        self.rsa = QtWidgets.QWidget()
        self.rsa.setObjectName("rsa")
        self.rsaKeyPairGeneration = QtWidgets.QPushButton(parent=self.rsa)
        self.rsaKeyPairGeneration.setGeometry(QtCore.QRect(20, 30, 111, 24))
        self.rsaKeyPairGeneration.setObjectName("rsaKeyPairGeneration")
        self.publicEncryptionKeyLineEdit_2 = QtWidgets.QLineEdit(parent=self.rsa)
        self.publicEncryptionKeyLineEdit_2.setGeometry(QtCore.QRect(280, 70, 71, 22))
        self.publicEncryptionKeyLineEdit_2.setObjectName("publicEncryptionKeyLineEdit_2")
        self.privateEncryptionKeyLineEdit_2 = QtWidgets.QLineEdit(parent=self.rsa)
        self.privateEncryptionKeyLineEdit_2.setGeometry(QtCore.QRect(280, 100, 71, 22))
        self.privateEncryptionKeyLineEdit_2.setObjectName("privateEncryptionKeyLineEdit_2")
        self.publicEncryptionKeyLabel = QtWidgets.QLabel(parent=self.rsa)
        self.publicEncryptionKeyLabel.setGeometry(QtCore.QRect(21, 71, 121, 16))
        self.publicEncryptionKeyLabel.setObjectName("publicEncryptionKeyLabel")
        self.privateDecryptionKeyLineEdit = QtWidgets.QLineEdit(parent=self.rsa)
        self.privateDecryptionKeyLineEdit.setGeometry(QtCore.QRect(157, 99, 93, 22))
        self.privateDecryptionKeyLineEdit.setObjectName("privateDecryptionKeyLineEdit")
        self.publicEncryptionKeyLineEdit = QtWidgets.QLineEdit(parent=self.rsa)
        self.publicEncryptionKeyLineEdit.setGeometry(QtCore.QRect(157, 71, 93, 22))
        self.publicEncryptionKeyLineEdit.setObjectName("publicEncryptionKeyLineEdit")
        self.privateDecryptionKeyLabel = QtWidgets.QLabel(parent=self.rsa)
        self.privateDecryptionKeyLabel.setGeometry(QtCore.QRect(21, 99, 130, 16))
        self.privateDecryptionKeyLabel.setObjectName("privateDecryptionKeyLabel")
        self.encryptionOptions.addTab(self.rsa, "")
        self.Caesar = QtWidgets.QWidget()
        self.Caesar.setObjectName("Caesar")
        self.caesarKeyLabel = QtWidgets.QLabel(parent=self.Caesar)
        self.caesarKeyLabel.setGeometry(QtCore.QRect(120, 60, 121, 16))
        self.caesarKeyLabel.setObjectName("caesarKeyLabel")
        self.caesarSpinBox = QtWidgets.QSpinBox(parent=self.Caesar)
        self.caesarSpinBox.setGeometry(QtCore.QRect(230, 60, 71, 22))
        self.caesarSpinBox.setMaximum(26)
        self.caesarSpinBox.setObjectName("caesarSpinBox")
        self.encryptionOptions.addTab(self.Caesar, "")
        self.substitution = QtWidgets.QWidget()
        self.substitution.setObjectName("substitution")
        self.substitutionLabel = QtWidgets.QLabel(parent=self.substitution)
        self.substitutionLabel.setGeometry(QtCore.QRect(130, 20, 101, 16))
        self.substitutionLabel.setObjectName("substitutionLabel")
        self.substitutionKeyTextField = QtWidgets.QLineEdit(parent=self.substitution)
        self.substitutionKeyTextField.setGeometry(QtCore.QRect(130, 40, 161, 21))
        self.substitutionKeyTextField.setObjectName("substitutionKeyTextField")
        self.genSubstituteKeyButton = QtWidgets.QPushButton(parent=self.substitution)
        self.genSubstituteKeyButton.setGeometry(QtCore.QRect(130, 80, 161, 24))
        self.genSubstituteKeyButton.setObjectName("genSubstituteKeyButton")
        self.encryptionOptions.addTab(self.substitution, "")
        self.vigenere = QtWidgets.QWidget()
        self.vigenere.setObjectName("vigenere")
        self.substitutionLabel_2 = QtWidgets.QLabel(parent=self.vigenere)
        self.substitutionLabel_2.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.substitutionLabel_2.setObjectName("substitutionLabel_2")
        self.vigenereKeyTextField = QtWidgets.QLineEdit(parent=self.vigenere)
        self.vigenereKeyTextField.setGeometry(QtCore.QRect(50, 40, 321, 21))
        self.vigenereKeyTextField.setObjectName("vigenereKeyTextField")
        self.encryptionOptions.addTab(self.vigenere, "")
        self.gridLayout.addWidget(self.encryptionOptions, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.inputLabel.setBuddy(self.inputField)
        self.outputLabel.setBuddy(self.outputField)
        self.publicEncryptionKeyLabel.setBuddy(self.publicEncryptionKeyLineEdit)
        self.privateDecryptionKeyLabel.setBuddy(self.privateDecryptionKeyLineEdit)

        # Linking button events to functions
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.moveInputToOutput.clicked.connect(self.inputToOutput)
        self.rsaKeyPairGeneration.clicked.connect(self.generateRSAKeys)
        self.genSubstituteKeyButton.clicked.connect(self.generateSubKey)

        # Error Message
        self.errorMessage = QtWidgets.QMessageBox()
        self.errorMessage.setIcon(QMessageBox.Icon.Warning)

        self.retranslateUi(MainWindow)
        self.encryptionOptions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryption GUI"))
        self.rsaKeyPairGeneration.setText(_translate("MainWindow", "Generate Key Pair"))
        self.publicEncryptionKeyLabel.setText(_translate("MainWindow", "Public (Encryption) Key"))
        self.privateDecryptionKeyLabel.setText(_translate("MainWindow", "Private (Decryption) Key:"))
        self.encryptionOptions.setTabText(self.encryptionOptions.indexOf(self.rsa), _translate("MainWindow", "RSA"))
        self.caesarKeyLabel.setText(_translate("MainWindow", "Shift Amount (key): "))
        self.encryptionOptions.setTabText(self.encryptionOptions.indexOf(self.Caesar), _translate("MainWindow", "Caesar"))
        self.substitutionLabel.setText(_translate("MainWindow", "Key:"))
        self.encryptionOptions.setTabText(self.encryptionOptions.indexOf(self.substitution), _translate("MainWindow", "Substitution"))
        self.substitutionLabel_2.setText(_translate("MainWindow", "Key:"))
        self.genSubstituteKeyButton.setText(_translate("MainWindow", "Generate Substitution Key"))
        self.encryptionOptions.setTabText(self.encryptionOptions.indexOf(self.vigenere), _translate("MainWindow", "Vigenère"))
        self.encryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.decryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.moveInputToOutput.setText(_translate("MainWindow", "Move Output to Input"))
        self.inputLabel.setText(_translate("MainWindow", "Input:"))
        self.outputLabel.setText(_translate("MainWindow", "Output:"))


    # Button Methods
    # Encrypt Pressed
    def encrypt(self):
        # Variable to store ciphertext
        cipherText = ""

        # Variable for input text
        inputText = self.inputField.toPlainText()

        ####################################################
        # RSA Encryption is selected
        if self.encryptionOptions.currentIndex() == 0:
            try:
                # Get public key from public key areas.
                publicKey = (int(self.publicEncryptionKeyLineEdit.text()),int(self.publicEncryptionKeyLineEdit_2.text()))

                # Encrypt
                cipherText = encryptionRSA.encrypt(inputText, publicKey).decode('utf-8')
            except ValueError:
                # Error message if there are no keys
                if self.publicEncryptionKeyLineEdit.text() == "" or self.publicEncryptionKeyLineEdit_2.text() == "":
                    self.errorMessage.setText("No Public Key Entered!")
                    self.errorMessage.exec()
                # Error message if no input
                else:
                    self.errorMessage.setText("No Input!")
                    self.errorMessage.exec()
                return
        ####################################################

        ####################################################
        # Caesar Encryption is selected
        elif self.encryptionOptions.currentIndex() == 1:
            cipherText = caesar_cipher(inputText, self.caesarSpinBox.value())
        ####################################################
        
        ####################################################
        # Substitution Encryption is selected
        elif self.encryptionOptions.currentIndex() == 2:
            alphabetSet = set("abcdefghijklmnopqrstuvwxyz")

            # Error message if key does not contain all letters of the alphabet.
            if not (set(self.substitutionKeyTextField.text()) >= alphabetSet):
                self.errorMessage.setText("Key needs to contain every letter in the alphabet once!")
                self.errorMessage.exec()
                return
            
            # Error message if key is not of proper length
            if len(self.substitutionKeyTextField.text()) != 26:
                self.errorMessage.setText("Key not proper length!  Must be 26 letters.")
                self.errorMessage.exec()
                return

            cipherText = substitution_cipher(inputText, self.substitutionKeyTextField.text())
        ####################################################

        ####################################################
        # Vigenere Encryption is selected
        elif self.encryptionOptions.currentIndex() == 3:
            try:
                cipherText = vigenere_encrypt(inputText, self.vigenereKeyTextField.text())
            except IndexError:
                self.errorMessage.setText("No key entered!")
                self.errorMessage.exec()
                return
        ####################################################


        # Set output textfield to ciphertext.
        self.outputField.setPlainText(str(cipherText))
    
    # Decrypt Pressed
    def decrypt(self):
        # Variable to store plaintext
        plainText = ""

        # Variable for input text
        inputText = self.inputField.toPlainText()

        ####################################################
        # RSA Decryption is selected
        if self.encryptionOptions.currentIndex() == 0:
            try:
                # Get private key from private key areas.
                privateKey = (int(self.privateDecryptionKeyLineEdit.text()), int(self.privateEncryptionKeyLineEdit_2.text()))

                # Decrypt
                plainText = encryptionRSA.decrypt(inputText.encode('utf-8'), privateKey)
            except ValueError:
                # Error message if there are no keys
                if self.privateDecryptionKeyLineEdit.text() == "" or self.privateEncryptionKeyLineEdit_2.text() == "":
                    self.errorMessage.setText("Empty Private Key Box!")
                    self.errorMessage.exec()
                    return
                # Error message for improper text to decrypt
                else:
                    self.errorMessage.setText("Input text cannot be decrypted, not in RSA form.")
                    self.errorMessage.exec()
                    return
        ####################################################

        ####################################################
        # Caesar Encryption is selected
        elif self.encryptionOptions.currentIndex() == 1:
            plainText = caesar_cipher(inputText, -self.caesarSpinBox.value())
        ####################################################

        ####################################################
        # Substitution Encryption is selected
        elif self.encryptionOptions.currentIndex() == 2:
            alphabetSet = set("abcdefghijklmnopqrstuvwxyz")

            # Error message if key does not contain all letters of the alphabet.
            if not (set(self.substitutionKeyTextField.text()) >= alphabetSet):
                self.errorMessage.setText("Key needs to contain every letter in the alphabet once!")
                self.errorMessage.exec()
                return
            
            # Error message if key is not of proper length
            if len(self.substitutionKeyTextField.text()) != 26:
                self.errorMessage.setText("Key not proper length!  Must be 26 letters.")
                self.errorMessage.exec()
                return

            plainText = substitution_decrypt(inputText, self.substitutionKeyTextField.text())
        ####################################################

        ####################################################
        # Vigenere Encryption is selected
        elif self.encryptionOptions.currentIndex() == 3:
            try:
                plainText = vigenere_decrypt(inputText, self.vigenereKeyTextField.text())
            except IndexError:
                self.errorMessage.setText("No key entered!")
                self.errorMessage.exec()
                return
        ####################################################

        # Set output to the newly decrypted plaintext
        self.outputField.setPlainText(str(plainText))
    
    # Moves text in output field to input field and clears output field.
    def inputToOutput(self):
        self.inputField.setPlainText(self.outputField.toPlainText())
        self.outputField.setPlainText("")
    
    # Generates RSA Keys, and stores them in the text boxes.
    def generateRSAKeys(self):
        # Generates key pair
        public, private = encryptionRSA.generate_key_pair()
        # store public key pair
        self.publicEncryptionKeyLineEdit.setText(str(public[0]))
        self.publicEncryptionKeyLineEdit_2.setText(str(public[1]))
        # store private key
        self.privateDecryptionKeyLineEdit.setText(str(private[0]))
        self.privateEncryptionKeyLineEdit_2.setText(str(private[1]))
    
    # Generates a random substitution key (a random permutation of the a-z alphabet)
    def generateSubKey(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxyz")
        key = ""

        # Randomly take a letter from the list, add it to the key, and remove it the alphabet list to prevent it from being picked again
        for i in range(26):
            nextIndex = random.randint(0, 25 - i)
            nextChar = alphabetList[nextIndex]
            key += nextChar
            alphabetList.remove(nextChar)
        
        self.substitutionKeyTextField.setText(key)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
