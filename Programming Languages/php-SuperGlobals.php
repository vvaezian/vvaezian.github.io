<!-- a showcase of $_REQUEST, $_POST, $_GET and $_COOKIE superglobal variables 
$_REUQEST by default contains the contents of $_GET, $_POST and $_COOKIE. 
$_GET is an array of variables passed to the current script via the URL parameters.
$_GET should be used with non destructive actions (sorting, recording actions, queries)
$_POST is an array of variables passed to the current script via the HTTP POST method.
$_POST should be used with destructive actions (deleting, updating)
$_COOKIE = trivial settings (stylesheet preferences etc)
$_SESSION = non trivial settings (username, logged in?, access levels)  -->

<!DOCTYPE html>
<html>
<head>
<style>
td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
</style>
</head>

<body>


<!-- When a user submits the data by clicking on "Submit", the form data is sent to the file 
specified in the 'action' attribute of the <form> tag. 
In this example, it points to the current file itself. -->
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {  // just an example
    // collect value of input field
    $name = htmlspecialchars($_REQUEST['fname']);  // htmlspecialchars is used to prevent code injection
    if (empty($name)) {
        echo "Name is empty";
    } else {
        echo $name."<br>";

	echo "<br><br>\$_REQUEST<br>";
	echo "<table>";
	  echo "<tr>";
	    echo "<th>Key</th>";
	    echo "<th>Value</th>";
	  echo "</tr>";
  
	    foreach ($_REQUEST as $key => $value) {
	      echo "<tr>";
		echo "<td>$key</td>";
		echo "<td>$value</td>";
	      echo "</tr>";
	    }
	echo "</table>";


	echo "<br><br>\$_POST<br>";
	echo "<table>";
	  echo "<tr>";
	    echo "<th>Key</th>";
	    echo "<th>Value</th>";
	  echo "</tr>";

	    foreach ($_POST as $key => $value) {
	      echo "<tr>";
		echo "<td>$key</td>";
		echo "<td>$value</td>";
	      echo "</tr>";
	    }
	echo "</table>";


	echo "<br><br>\$_GET<br>";
	echo "<table>";
	  echo "<tr>";
	    echo "<th>Key</th>";
	    echo "<th>Value</th>";
	  echo "</tr>";

	    foreach ($_GET as $key => $value) {
	      echo "<tr>";
		echo "<td>$key</td>";
		echo "<td>$value</td>";
	      echo "</tr>";
	    }
	echo "</table>";


	echo "<br><br>\$_COOKIE<br>";
	echo "<table>";
	  echo "<tr>";
	    echo "<th>Key</th>";
	    echo "<th>Value</th>";
	  echo "</tr>";

	    foreach ($_COOKIE as $key => $value) {
	      echo "<tr>";
		echo "<td>$key</td>";
		echo "<td>$value</td>";
	      echo "</tr>";
	    }
	echo "</table>";

} }
?>

</body>
</html>
