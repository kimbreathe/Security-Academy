<?php
include "./config.php";
$con = con();
$id = isset($_GET['id']) ? $_GET['id'] : '';
$password = isset($_GET['password']) ? $_GET['password'] : '';

if (!empty($id) && !empty($password)) {
    $sql = "SELECT id FROM users WHERE id='$id' AND password='$password'";
    echo "<h1>Query : <strong>{$sql}</strong></h1><br><br><br>";
    $result = @mysqli_fetch_array(mysqli_query($con, $sql));
    if ($result['id'] == 'admin')
    {
        echo "<h1>admin check!</h1><br><br><br>";
    }
}
highlight_file(__FILE__);
?>
