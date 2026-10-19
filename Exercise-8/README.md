# Exercise 8 – Creating a "Hello World" Jenkins Job

## Objective

To create a simple shell script, store it in a GitHub repository, and configure a Jenkins Freestyle project to execute the script automatically.

The Jenkins job prints:

```text
Hello, Jenkins!
1. Create the Hello World Script

The script was created as hello-world.sh.

Script
#!/bin/bash
echo "Hello, Jenkins!"

The script was made executable using:

chmod +x hello-world.sh

The script was tested locally using:

./hello-world.sh
Output
Hello, Jenkins!
2. Git Repository

The script is maintained as part of the DEVOPS GitHub repository:

https://github.com/Rajatha-AN/DEVOPS

The Exercise 8 directory contains:

Exercise-8/
├── hello-world.sh
└── README.md
3. Jenkins

Jenkins was already installed and running from the previous exercises.

Jenkins can be accessed at:

http://localhost:8080

The existing Jenkins installation was reused for this exercise.

4. Create a New Jenkins Job
Open Jenkins at http://localhost:8080.
Click New Item.
Enter the job name:
HelloWorld
Select Freestyle project.
Click OK.
5. Configure Source Code Management

Under Source Code Management:

Select Git.
Enter the repository URL:
https://github.com/Rajatha-AN/DEVOPS.git
Configure the required Git credentials if prompted.
Select the appropriate branch:
*/main
6. Configure Build Step

Under Build Steps:

Click Add build step.
Select Execute shell.
Enter:
cd Exercise-8
sh hello-world.sh

This changes to the Exercise-8 directory and executes the shell script.

7. Build the Jenkins Job

After saving the job:

Open the HelloWorld Jenkins job.
Click Build Now.
A new build will appear under Build History.
8. View Console Output

Open the build number and select Console Output.

The expected output is:

Started by user
Building in workspace /var/jenkins_home/workspace/HelloWorld
[HelloWorld] $ /bin/sh -xe ...
+ cd Exercise-8
+ sh hello-world.sh
+ echo 'Hello, Jenkins!'
Hello, Jenkins!
Finished: SUCCESS
9. Result

The Jenkins Freestyle project successfully executes the hello-world.sh script from the GitHub repository.

The expected message:

Hello, Jenkins!

is displayed in the Jenkins Console Output, and the build finishes with:

Finished: SUCCESS
