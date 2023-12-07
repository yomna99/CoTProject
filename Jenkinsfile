pipeline {
    agent any
    
    environment {
        WILDFLY_HOME = '/opt/wildfly'
        M3_HOME = '/opt/maven'
        PROJECT_DIR = 'code/api'
    }
    
    stages {
        stage('Build') {
            steps {
                dir(PROJECT_DIR) {
                    script {
                        sh "$M3_HOME/bin/mvn clean install"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                dir(PROJECT_DIR) {
                    script {
                        sh "$M3_HOME/bin/mvn test"
                    }
                }
            }
        }
        stage('Deploy to WildFly') {
            steps {
                dir(PROJECT_DIR) {
                    script {
                        sh "echo P | $WILDFLY_HOME/bin/jboss-cli.sh --connect -u=\"admin\" -p=\"admin\"  --command=\"deploy --force target/jakartaee-hello-world.war\""
                      
                    }
                }
            }
        }
    }
}
