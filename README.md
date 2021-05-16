# CRUD_Interfaz_SQL
## Aplicación gráfica tipo CRUD conectada a una base de datos

### Función de la interfaz

Esta aplicación gráfica se conecta a una base de datos donde se pueden realizar operaciones de Insertar, Leer, Actualizar y Borrar registros. 

Para crear la interfaz fue utilizada la librería tkinter. Se crearon cuadros de texto y labels para permitir la interacción adecuada con el usuario. Incluso se creó un cuadro de desplazamiento en el cuadro de Comentario para en caso de extenderse no sea un problema. 

En cada módulo puede identificarse por su nombre qué clase de función tiene en la interfaz. En cada uno de estos existen comandos SQL para hacer el proceso de Creación, Lectura, Actualización y Eliminación de datos. Para ello fue utilizada la librería de SQL Lite. 

A continuación una imágen de la aplicación gráfica:

![image](https://user-images.githubusercontent.com/43154438/118383267-f8a7e380-b5c1-11eb-9542-48924256746b.png)

Hay ventanas desplegables en cada uno de los botones de esta interfaz donde se pueden realizar diferentes funciones. Como la de salir y conectar en la primera pestaña desplegable. Si se le da en conectar, se crea automáticamente una base de datos:

![image](https://user-images.githubusercontent.com/43154438/118383464-81734f00-b5c3-11eb-8657-5ccd2627bf5e.png)

En cambio, si se le da en salir, sale una ventana emergente donde se pregunta si realmente se quiere salir de la aplicación y así evitar inconveniencias con el usuario:

![image](https://user-images.githubusercontent.com/43154438/118383502-e9299a00-b5c3-11eb-8728-b728f82d2d9a.png)

En cambio, si la base de datos ya existem saldrá una ventana emergente indicando esto.

Mediante la aplicación del DBBrowser es posible ver la estructura de la base de datos creada:

![image](https://user-images.githubusercontent.com/43154438/118385567-85a86800-b5d5-11eb-8c3c-d23fa2905a28.png)

Como se puede observar existen 6 campos: ID, NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCIÓN Y COMENTARIOS. 

Existe también la opción de borrar campos, la cual sirve para eliminar datos individuales en caso de arrepentirse de agregar uno,

![image](https://user-images.githubusercontent.com/43154438/118383664-a10b7700-b5c5-11eb-9460-f60d2bdc8d59.png)

Es en la pestaña que dice "CRUD" donde se tienen las opciones de Crear, LEer, Actualizar o Borrar un registro. 

![image](https://user-images.githubusercontent.com/43154438/118383735-47f01300-b5c6-11eb-9d2d-3f15e0cb6bc1.png)

A medida que se van creando los datos así se va modificando la base de datos. 

![image](https://user-images.githubusercontent.com/43154438/118385578-af618f00-b5d5-11eb-9531-dae06a4a3e28.png)

Del mismo modo en que se crea el dato, puede leerse poniendo meramente el ID del usuario en el recuadro de ID, dandole click en "Leer" en la pestaña desplegable de CRUD y los datos aparecerán en los cuadros de texto. 

También se pueden actualizar haciendolo en el siguiente orden: ingresar un ID, luego escribir los nuevos datos, y dandole en Actualizar en la pestaña desplegable CRUD, así se reemplazan datos ya existentes por otros.

Y pueden borrarse poniendo el ID y dándole click al botón Borrar de la pestaña desplegable CRUD.

### Conclusiones y resultados obtenidos

Aparte de las Queries que pueden hacerse mediante el uso de comandos SQL las cuales consisten en el proceso de consultas y lecturas de los datos, también se pueden crear y actualizar datos, lo cuál está evidenciado en este proyecto. 

Esto combinado con la creación de un ejecutable, podría ser de gran utilidad para alguna empresa que necesite hacer su proceso de registro de datos en la cual una interfaz tipo CRUD sea de utilidad.
