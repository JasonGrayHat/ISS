<?php
require 'common.php';

//Grab all the users from our database
$users = $database->select("users", [
    'id',
    'name',
    'rfid_uid'
]);

?>
<!DOCTYPE html>
<html lang="en">
       <a  href="index.php">Fall 2019 - Reverse Engineerng IoT Systems (ITSC-305-ISA)</a>
                <a href="attendance.php" class="nav-link">View Attendance</a>
                <a href="users.php" class="nav-link active">View Users</a>
	<br>
        <div class="row">
	    <h2>Students</h2>
        </div>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">RFID UID</th>
                </tr>
                <?php
                foreach($users as $user) {
                    echo '<tr>';
                    echo '<td scope="row">' . $user['id'] . '</td>';
                    echo '<td>' . $user['name'] . '</td>';
                    echo '<td>' . $user['rfid_uid'] . '</td>';
                    echo '</tr>';
                }
                ?>
        </div>
</html>
