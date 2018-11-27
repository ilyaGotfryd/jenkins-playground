pipeline{
	agent { docker { image 'python:3.5.1' } }
	stages {
		stage('build') {
			steps {
				sh 'python --version'
				sh 'echo "Hello World"'
				sh '''
					echo "Multiple shell steps work too"
					ls -lah
				'''
			}
		}
		stage('test'){
			steps{
				sh 'py.test'
				sh ' ls -lah'
			}
		}
	}
	post{
		junit 'build/reports/**/*.xml'
	}
}
