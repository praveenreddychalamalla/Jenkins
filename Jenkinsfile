pipeline{
	agent any
	stages{
		stage('Clone Git'){
			steps{
				git'https://github.com/praveenreddychalamalla/Jenkins.git'
			}
		}
		stage('Build Code'){
			steps{
				sh "chmod u+x Program1.py"
				sh "./Program1.py"
			}
		}
		stage('Test Code'){
			steps{
				sh "chmod u+x Test.py"
				sh "./Test.py"
			}
		}
	}
}