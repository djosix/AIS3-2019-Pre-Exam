<h2>Directory Lister</h2>
<p>Let's hack my stupid webpage for d1v1n6 d33p3r</p>

<form>
    <input type="text" name="dir" value="./">
    <input type="submit" value="List!">
</form>

<?php if ($dir = @$_GET['dir']): ?>
    <pre>Output:
<?= shell_exec("ls -al '$dir'") ?>
</pre>
<?php endif; exit; ?>
AIS3{y0u_4r3_4bl3_70_d1v3_d33p3r_n3x7_71m3}
