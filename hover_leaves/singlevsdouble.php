<?php

    $fname = "David";

    // Single quotes
    echo 'My name is $fname.'; // My name is $fname.

    // Double quotes
    echo "My name is $fname."; // My name is David.

    // Curly braces to isolate the name of the variable
    echo "My name is {$fname}."; // My name is David.

    // Example of heredoc
    echo $foo = <<<abc
    My name is {$fname}
    abc;

        // Example of nowdoc
        echo <<< 'abc'
        My name is "$name".
        Now, I am printing some
    abc;

?>
