<!DOCTYPE html>
<html>

<head>
  <title>Shell Scripting</title>
  <link rel="shortcut icon" href="/vvaezian.github.io/Pic/terminal.ico">
  <link rel="stylesheet" href="/vvaezian.github.io/styles.css"/>
  <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>
</head>

<body>
<img src="/vvaezian.github.io/Pic/shell-scripting.png" alt="Logo" height="128">     

<em>"Graphical user interfaces make easy tasks easier, while command line interfaces make difficult tasks possible."</em>  
    
<em>* Most of the material is taken from <a href="https://www.amazon.com/Linux-Shell-Scripting-Bash-Burtch/dp/0672326426">this</a> book.</em>
    

<h2>Shell Scripting</h2>

A Simple Shell Script
	
  ``` class="prettyprint">#!/bin/bash
clear
echo "Hello world!"
```  
The first line tells the operating system what shell to use to interpret the script and the location of the shell.  
We need the following command to make the file <a href="http://en.wikipedia.org/wiki/File_system_permissions#Numeric_notation">executable</a>: `$ chmod 755 script_name` (or `$ chmod +x script_name`).  
We can then run the script by `$ ./script_name`.  
Alternatively, we could use `$ bash script_name`. In This method we don't need to make the file executable.  
  
All shell commands and scripts generate a return value upon finishing execution; the value can be set with the exit statement (default 0). The return value is always stored in the `$?` variable.

<details class="details">
	<summary>Variables</summary>

		<ul>
			<li>Variables can be created and assigned text using an equals sign. 
			Surround the text with double quotes (although it is not necessary unless there is space in the name):  
			```$ FILENAME="info.txt"  
			$ printf “%s\n” “$FILENAME”  
			info.txt```  
			<li>The `declare` command, in addition to creation of variable and assigning values, can add attributes to variables as well 
			(using + instead of - turns of the attribute).  
			<samp>declare -r x=5</samp>  
			(`-r` option makes the variable read-only)  
			  
			The <samp>declare</samp> command without any options list all pre-defined variables of system.  
			<li>The results of a command can be assigned to a variable using backquotes.  
			```$ Date=`date`  
			$ printf "%s\n" "$Date"  
			Thu Apr 13 08:02:19 UTC 2017 ```  
			<li>Double quotes do not prevent Bash from interpreting the special characters $, ‘, and \,
			but single quotes leave all characters unchanged.
			<li>Variable names can be enclosed in curly braces to make it clear where the variable’s name begins and ends.  
			<smap>$ TAX_MESSAGE="The tax is ${TAX}%"</samp>
			<li>Shell variables exist in the script or interactive sessions only, where they were
			declared. In order to make shell variables available outside of their place of origin, they have to be declared as exportable with `-x` option.  
			Although Linux has provisions for exporting environment variables, there is no way to assign any attributes to them.  
			The variables shared with a new program are copies of the original. If a script
			declares an exported variable and runs a second script, any changes made to the variable by the second script are invisible to the first.There is no way for a second script to assign a new value to a variable that the first script will see. Unlike other programming languages, exporting shell variables is a one-way street.  
			The only way to return a value to the calling program is to write it to a file (or standard output) and have the calling program read (or assign) the value back into a variable.
			<li>Before a command is executed, Bash searches the command for all dollar signs and inserts the value of variables before the command is carried out. Bash performs this substitution once. `eval` command do this another time:  
			```#!/bin/bash  
				VAR1=25  
				VAR2='$VAR1'  
				VAR3='$VAR2'  
				echo "$VAR3"  
				eval echo "$VAR3"  
				eval eval echo "$VAR3"
			```  
			Output of the script above:  
			```$VAR2  
				$VAR1  
				25```
		</ul>
		<table class="EveryOtherOne">
					<tr>
						<td><samp>$RANDOM</samp>
						<td>Generates a random integer number (0 - 32767)
					</tr>
		</table>
	</div>
</details>



<details class="details">
	<summary>Reading Keyboard Input</summary>

		  ``` class="prettyprint">read -p "Please enter your name: " USER_NAME```  
		With <samp>-p</samp> option we can provide a message before the user input.  
		<samp>read -t 5 FILENAME # wait up to 5 seconds to read a filename </samp>  
		<samp>-n 10 FILENAME # read no more than 10 characters</samp>  
		The <samp>-r</samp> (raw input) option disables the backslash escaping of special characters. 
	</div>
</details>



<details class="details">
	<summary>printf</summary>

		`printf` is very similar to the C standard I/O <samp>printf()</samp> function, but they are not
		identical. In particular, single- and double-quoted strings are treated differently in shell scripts than in C programs.  
		The first parameter is a format string describing how the items being printed will be represented. 
		For example, the special formatting code “%d” represents an integer number, and the code “%f” represents a floating-point number:  
		```$ printf "%d and %f\n" 5 5
		5 and 5.000000```  
	</div>
</details>



<details class="details">
	<summary><samp>if</samp> command</summary>

		```
			if test Condition; then  
			&emsp; Expression1  
			else  
			&emsp; Expression2  
			fi  
		```  
		We can use square brackets instead of <samp>test</samp>:   
		```
			if [ Condition ]; then  
			&emsp; ...  
			fi  
		```  
		We can use carriage return instead of semi-colon <samp>(;)</samp> :  
		```
			if [ Condition ]  
			then  
			&emsp; Expression1  
			else  
			&emsp; Expression2  
			fi  
		```  
		Make richer Conditions by using `-a` <samp>(and)</samp>, `-o` <samp>(or)</samp>, `!` <samp>(not)</samp>.  
		Unlike most programming languages, in BASH the "not" operator doesn't take precedence over "and" and "or". So use parenthesis if needed.  
		```
			if [ \( ! -f "$TMP1" \) -a -f "$TMP2" ]  
		```  
		Alternatively we can use <samp>&&, ||</samp> for 'and', 'or'.  
		```
			if [ \( ! -f "$TMP1" \) ] && [ -f "$TMP2" ]  
		```  
		* `help test` gives useful options.  
		Writing <samp>if</samp> commands in terminal:  
		```if [ condition ]; then &ltrest of code&gt ; fi
		```  
		Alternatively,  
		```$ if [ condition ]; then  
			> &ltrest of code&gt   
			> fi  
		```
	</div>
</details>




<details class="details">
	<summary>Arrays</summary>

		<ul><li>Array is like a variable. So it is created using declare, with `-a` option or just direct assignment:  
		<samp>$ declare -a ARRAY0$</samp>  
		<samp>$ ARRAY1=(0 1 2)</samp>  
		<samp>$ ARRAY2=([3]='cat' [5]='dog' [12]='cow')</samp> #indicating indeces
		<li>Bash arrays differ from arrays in other computer languages in that they are open-ended. Arrays can be any length and are initially filled with empty strings for items.
		<li>Use curly braces to supercede the shell's pathname matching process:  
			<samp>$ echo "${ MYARRAY [2] }"</samp>
		<li>If no index is given, index zero is assumed:  
			<samp>$ echo "$ARRAY1"</samp>  
			2  
			<samp>$ ARRAY1 = "a"</samp>  
			['a', 1, 2]
		<li>Accessing all elements of an array can be done using index `*` or `@`. The difference (for `printf` not `echo`) is that `*` puts an space (actually the first character of IFS variable) in between elements but `@` doesn't:  
		<samp>$ echo "${ARRAY1[*]}"</samp>  
		a 1 2
		<li>Individual array values can be removed with the command. Erasing a value by `unset` assigning the array position an empty string doesn’t destroy it:The empty string is still treated as an array item whenever the items are counted.
		<li>The `read` command can read a list into an array using an `-a` switch. When this switch is used, each item on the line of input is read into a separate array position.
	</div>
</details>



<details class="details">
	<summary>Command History</summary>

		<p>The easiest way to browse the command history is with the Up and Down arrow
		keys. The history can also be searched with an exclamation mark (`!`). This denotes the
		start of a command name to be completed by Bash. Bash executes the most recent command
		that matches. For example,  
		```
			$ !d  
			date  
			Thu Apr 13 08:24:51 UTC 2017  
		```  
		`!!`repeats the last command. A negative number indicates the relative line number. That is, it indicates the number
		of commands to move back in the history to find the one to execute. `!!` is the same as `!-1`.  
		  
		The `!#` repeats the content of the current command line. (Don’t confuse this with `#!`) 
		Use this to run a set of commands twice.  
		  
		`history n` lists the last n commands.
		</p>

		<ul>
		<li>Running `stty` shows the common command keys as well as other information about your session. (has -a option)
		<li> Use `\` for using the next line in long commands
		<li> Two commands separated by a semicolon (`;`), are executed consecutively, one after another. 
		Two commands separated by `&&`, are executed until one of them fails or until all the commands are executed. Similarly for `||`.
		<li> `sleep n` makes a n second delay.
		<li> Using the minus sign (–) with `cd`, you can switch between the current directory and the last directory. 
		(~ and - are features of Bash and only work with Bash and Bash scripts.)
		</ul>
	</div>
</details>


<details class="details">
	<summary>Looping Constructs</summary>

```
for i in list
do
	something
done```
  ``` class="prettyprint">
sum=0
for i in 1 2 3 4
do
	sum=$(($sum+$i))
done
echo "The sum of $i numbers is: $sum"
```  
		```
			while condition is true  
			do  
				&emsp; something  
			done
		```  
		```
			until condition is false  
			do  
			    &emsp; something  
			done
		```  
	</div>
</details>




<details class="details">
	<summary>Security</summary>

        Create random and unpredictable filenames for temporary storage with the `mktemp` utility:  
        ```
        	TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)  # To create a temporary file  
			TEMPDIR=$(mktemp -d /tmp/tempdir.XXXXXXXX)  # To create a temporary directory
		```  
		The <samp>XXXXXXXX</samp> is replaced with random characters by the <samp>mktemp</samp> utility.
	</div>
</details>




<details class="details">
	<summary>Misc.</summary>

		<details class="details">
			<summary>Debugging</summary>

				We can run a script in debug mode by `bash –x ./script_file`.  
				Inside a sccript we can do it by  
				```
					set -x    # turns on debugging  
					...  
					set +x    # turns off debugging  
				```
			</div>
		</details>	
    
		<details class="details">
			<summary>Quick Refference Table</summary>

				<table class="EveryOtherOne">
					<tr>
						<td><samp>${#str}</samp>
						<td>Length of the string <samp>str</samp>
					</tr>
					<tr> 
						<td> <samp>${str:i:j}</samp>
						<td> String Slicing. i: start, j: length
					</tr>
					<tr> 
						<td> <samp>${str#*i}</samp>
						<td> String Slicing. The part of <samp>str</samp> after character i.
					</tr>
					<tr> 
						<td> <samp>$n</samp>
						<td> Referring to the nth argument that is given alongside the command
					</tr>
				</table>
			</div>
		</details>
    
	</div>
</details>


</body>
</html>
