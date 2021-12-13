<!doctype html>
<html lang="en">
  <head>
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>MYHome</title>
  </head>
  <body class="p-3">
    <h2>MYHome</h2>
    <br>

        <?php
        set_time_limit(500);

        if(array_key_exists('tambah', $_POST)) {
            tambah();
        }
        else if(array_key_exists('train', $_POST)) {
            train();
        }
        else if(array_key_exists('test', $_POST)) {
            test();
        }

        function tambah() {
            shell_exec('python dataset.py');

        }
        function train() {
            shell_exec('python test.py');

        }
        function test() {
            shell_exec('python test.py');
        }
        ?>

        <form method="post">
            <input type="submit" class="btn btn-primary btn-lg" name="tambah" value="Tambah data">
            <input type="submit" class="btn btn-warning btn-lg text-light" name="train" value="Training data">
            <input type="submit" class="btn btn-success btn-lg" name="test" value="Testing">
        </form>
        
    </body>
</html>
