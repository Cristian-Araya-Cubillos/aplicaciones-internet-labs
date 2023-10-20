<html>
    <head>
        <title>Aplicaciones de Internet</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
            
        <?php
            $id =0;
            if ($_SERVER["REQUEST_METHOD"] == "POST" && (!empty($_POST['nombre']) && !empty($_POST['apellido']))) {
                $nombre = $_POST['nombre'];
                echo "<p>Nombre: $nombre</p>";
                $apellido = $_POST['apellido'];
                echo "<p>Apellido: $apellido</p>";
                $id = $_POST['num'];
                echo "<p>ID: $id</p>";
                $conn = mysqli_connect('db', 'root', 'test', "dbname");
                // Ingresar Consulta
                $query = "INSERT INTO Person (id, name, apellido) VALUES ('$id', '$nombre', '$apellido')";

                
            // Se prepara la consulta
                $stmt = $conn->prepare($query);

                // Mandamos los parametros
                //$stmt->bind_param("iss", $id, $nombre, $apellido);
                /*
                "i": Representa un valor numérico entero.
                "d": Representa un valor numérico de punto flotante (double).
                "s": Representa una cadena de texto (string).
                "b": Representa un valor de tipo blob (binario).
                */
                // Ejecutar la consulta
                if ($stmt->execute()) {
                    echo "Se insertó correctamente";
                } else {
                    echo "No se insertó correctamente";
                }

                $stmt->close();
                mysqli_close($conn);
            } else {
                echo "<p>Ingrese los datos</p>";
            }           
            echo "<h1>Aplicaciones de Internet</h1>";

            $conn = mysqli_connect('db', 'root', 'test', "dbname");

            $query = 'SELECT * From Person';
            $result = mysqli_query($conn, $query);
            $totalPeople = mysqli_num_rows($result);
            $cont =1;
            #echo "<p>Total de personas: $totalPeople</p>";
            echo '<table class="table table-striped">';
            echo '<thead><tr><th></th><th>ID</th><th>Nombre</th><th>Apellido</th></tr></thead>';
            while($value = $result->fetch_array(MYSQLI_ASSOC)){
                echo '<tr>';
                echo '<td><a href="#"><span class="glyphicon glyphicon-search"></span></a></td>';
                foreach($value as $element){
                    echo '<td>' . $element . '</td>';
                    
                }
                echo '</tr>';
                $cont =$cont+1;
                
            }
            echo '</table>';

            $result->close();
            mysqli_close($conn);
        ?>
            
        <div class="container-fluid">
        <form action="" method="post">
            <div class="mb-3">
                <label for="nombreLabel" class="form-label">Nombre</label>
                <input type="text" placeholder="Ingresa Nombre" class="form-control" name = "nombre">
            <div id="emailHelp" class="form-text">Ingrese Nombre</div>
            </div>
            <div class="mb-3">
                <label for="idLabel" class="form-label">Apellido</label>
                <input type="text" placeholder="Ingresa Apellido" class="form-control" id="apellido" name = "apellido">
            </div>
            <input type="hidden" id="num" name="num" value="<?php echo $cont; ?>" >
            <button type="submit" class="btn btn-primary">INSERTAR</button>
        </form>
    </body>

</html>