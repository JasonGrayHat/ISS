<?php
require 'common.php';

$users = $database->select("users", [
    'id',
    'name',
]);

if (isset($_GET['year'])) {
    $current_year = int($_GET['year']);
} else {
    $current_year = date('Y');
}

if (isset($_GET['month'])) {
    $current_month = $_GET['month'];
} else {
    $current_month = date('n');
}

$num_days = cal_days_in_month(CAL_GREGORIAN, $current_month, $current_year);

?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Attendance System</title>
    </head>
    <body>

        <a href="index.php">Fall 2019 - Reverse Engineerng IoT Systems (ITSC-305-ISA)</a>
                <a href="attendance.php">View Attendance</a>
                <a href="users.php">View Users</a>
    <br>
            <h2>Attendance</h2>
                <tr>
                    <th scope="col">Name</th>
                    <?php
                        //Generate headers for all the available days in this month
                        for ( $iter = 1; $iter <= $num_days; $iter++) {
                            echo '<th scope="col" style="min-width:200px;max-width:300px;">' . $iter . '</th>';
                        }
                    ?>
                </tr>
                <?php
                    //Loop through all our available users
                    foreach($users as $user) {
                        echo '<tr>';
                        echo '<td scope="row">' . $user['name'] . '</td>';

                        //Iterate through all available days for this month
                        for ( $iter = 1; $iter <= $num_days; $iter++) {
                            
                            //For each pass grab any attendance that this particular user might of had for that day
                            $attendance = $database->select("attendance", [
                                'clock_in'
                            ], [
                                'user_id' => $user['id'],
                                'clock_in[<>]' => [
                                    date('Y-m-d', mktime(0, 0, 0, $current_month, $iter, $current_year)),
                                    date('Y-m-d', mktime(24, 60, 60, $current_month, $iter, $current_year))
                                ]
                            ]);

                            //Check if our database call actually found anything
                            if(!empty($attendance)) {
                                //If we have found some data we loop through that adding it to the tables cell
                                echo '<td class="table-success">';
                                foreach($attendance as $attendance_data) {
                                    echo $attendance_data['clock_in'] . '</br>';
                                }
                                echo '</td>';
                            } else {
                                //If there was nothing in the database notify the user of this.
                                echo '<td class="table-secondary">No Data Available</td>';
                            }
                        }
                        echo '</tr>';
                    }
                ?>
</html>
