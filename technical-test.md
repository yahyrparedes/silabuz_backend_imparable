## Reto técnico Django - Backend Imparable 

### INTRODUCCIÓN

El siguiente reto es una prueba para poder evaluar tus habilidades.

### ¿Qué evaluaremos?

Principalmente los siguientes aspectos:

- Creatividad para resolver los requerimientos a nivel de servicios.
- Calidad del código entregado (estructura y buenas prácticas).
- Eficiencia de los algoritmos entregados.
- Organización de la estructura de folders y archivos.

### Objetivo

Crear una aplicación que ayude a obtener una lista de álbumes, canciones y sus artistas (clone de Deezer).

Puedes tomar como referencia la [API Rest de Deezer](https://developers.deezer.com/api). (Es necesario que te registres para acceder a la documentación) Así mismo, debe tener un sistema de autentificación API Rest Desarrollado con Django.

Lista de end-points que debes trabajar

<table>
<thead>
<tr>
<th>#</th>
<th>Nombre</th>
<th>Método: endpoint</th>
<th>Ejemplo</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Albums</td>
<td>GET : /album/{id}</td>
<td><a href="https://api.deezer.com/album/302127">https://api.deezer.com/album/302127</a></td>
</tr>
<tr>
<td>2</td>
<td>Artists</td>
<td>GET : /artist/{id}</td>
<td><a href="https://api.deezer.com/artist/27">https://api.deezer.com/artist/27</a></td>
</tr>
<tr>
<td>3</td>
<td>Search songs</td>
<td>GET : /search?q=keyword</td>
<td><a href="https://api.deezer.com/search?q=eminem">https://api.deezer.com/search?q=eminem</a></td>
</tr>
<tr>
<td>4</td>
<td>Auth</td>
<td>POST: /login</td>
<td>request:  <pre>data : {   email: <a href="mailto:hola@silabuz.com">hola@silabuz.com</a>,   password: 12345678 } response:  data : {   token: ASdx$3de3e2dd…, }</pre></td>
</tr>
<tr>
<td>5</td>
<td>Register</td>
<td>POST: /register</td>
<td>request:  <pre>data : {   email: <a href="mailto:hola@silabuz.com">hola@silabuz.com</a>,   name: Freddy Silabuz,   password: 12345678,   confirm: 12345678,   country: Perú }</pre> response:  <pre>data : {   user: {Object...}   token: ASdx$3de3e2dd…, }</pre></td>
</tr>
<tr>
<td>6</td>
<td>Logout</td>
<td>POST: /logout</td>
<td>request:  <pre>data : {} (Empty) response:  data : {   message: ‘Successful logout’ }</pre></td>
</tr>
</tbody>
</table>

## IMPORTANTE

Ten en cuenta los siguientes consideraciones:

1. Las rutas (end-points) deben estar protegidas, esto quiere decir que es necesaria la autenticación para acceder a ellas.
2. La API deberá estar documentada, recuerda que las rutas que pondrás a disposición deben ser consumidas desde front-end. Por lo tanto, estas deben estar detalladas claramente por ello debes documentar la API siguiendo estándares. Te recomendamos utilizar herramientas tales como : Postman Tools https://www.postman.com/api-documentation-tool/ o Swagger https://swagger.io/
3. Opcional: Es bueno adoptar la práctica de desarrollo Test Driven Development (TDD) con el fin de evaluar la calidad del código implementado en relación a los requerimientos.
4. Opcional: Las rutas (end-points) /artist , /albums ,etc. Son consideradas rutas de lectura (only-GET), sin embargo puedes añadir las rutas complementarias a un CRUD (Create, Update & Delete), esto se considerará como bonus en tu calificación.
5. Para el desarrollo de este reto tienes un tiempo máximo de 48 horas.
6. Al finalizar, subirlo a un repositorio en github y compártenos el enlace en el siguiente formulario