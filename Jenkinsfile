pipeline{
	agent { docker { image 'python:3.5.1' } }
	stages {
		stage('Build') {
			steps {
				sh 'python --version'
				sh 'pip install -r requirements.txt'
				sh 'echo "Hello World"'
				sh '''
					echo "Multiple shell steps work too"
					ls -lah
				'''
			}
		}
		stage('Test'){
			steps{
				sh 'py.test'
				sh ' ls -lah'
			}
		}
	}
	post{
		always{
			junit 'build/reports/**/*.xml'
		}
	}
}
