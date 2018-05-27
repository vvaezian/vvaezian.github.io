
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



<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // collect value of input field
    $name = htmlspecialchars($_REQUEST['fname']);
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
