 #!/bin/bash
 CP=./classes
 CP=$CP:/home/pi/pi4j/pi4j-distribution/target/distro-contents/lib/pi4j-core.jar
 CP=$CP:./lib/javax.mail_1.1.0.0_1-4-4.jar
 CP=$CP:./lib/json.jar
 #
 java -classpath $CP pi4j.email.LedControllerMain $*
