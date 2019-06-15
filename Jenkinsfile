def app = 'Unknown'
pipeline {
    agent any
    stages {
        stage('build'){
            steps{
                script{
                    app = docker.build("purvaudai/facebook-archive")
                    docker.withRegistry('', 'dockerhub'){
                        app.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
    }  
}