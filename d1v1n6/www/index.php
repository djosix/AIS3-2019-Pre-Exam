<?php

    if ($_SERVER['REMOTE_ADDR'] == '127.0.0.1') {

        // show path of the flag
        die($_ENV['FLAG_HINT']);
    }


    if ($path = @$_GET['path']) {
        $path = trim($path);

        if (preg_match('/https?:\/\/([^\/]+)/i', $path, $g)) {
            // resolve ip address
            $ip = gethostbyname($g[1]);

            // no local request
            if ($ip == '127.0.0.1' || $ip == '0.0.0.0')
                die('Do not request to localhost!');
        }

        // no flag in path
        $path = preg_replace('/flag/i', '', $path);

        if ($content = @file_get_contents($path, FALSE, NULL, 0, 1000)) {

            // no flag in content
            if (preg_match('/flag/i', $content)) {
                die('Detected "flag" in content. Not showing!');
            }

            die($content);
        }

        die('No content or failed to get content.');
    }

?>
<h2>d1v1n6</h2>
<a href="?path=hint.txt">Hint</a>
