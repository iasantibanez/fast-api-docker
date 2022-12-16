### Implementación de API REST en Fast API + AWS + Docker


 **el codigo se encuentra diseñado bajo el patron de diseño de repositorio, en donde se prima destinar carpetas asociadas a la logica de cada endpoint y desacoplar la logica de todas las operaciones CRUD que se realizan en la Base de datos. Así aislar la capa de datos con el resto de la app**


1. En primer lugar se definio la arquitectura a para resolver el desafio, acá se tomó el uso de recursos cloud, RDS Postgresql y EC2 del ecosistema AWS. Posteriormente en terminos de codigo se desarrollo en python bajo el framework de fastapi Siguiendo documentación y buenas practicas de seguridad.

2. En segundo lugar, se definió el modelo de jobs, deparments y employees que cumpla con las restricciones definidas en el challenge.

3. En tercer lugar, se definierón recursos bases para establecer conexión entre servidores AWS (RDS) (confing.py y sessions.py)

4. En cuarto lugar, se definieron endpoints versionables en el modulo routes. De forma que se desacopla la lógica del endpoint y la lógica de extracción de información.

5. En terminos de seguridad, se definieron variables de entorno para no exponer ni comprometer la seguridad de la información.

6. Por ultimo, se dockerizo la aplicación y se monto en una EC2 basada en linux, se configuró la maquina en mediange SSH copiando el docker-compose-template.yml y reemplazando los valores necesarios.


##### Algo ideal, hubiese sido configurar CI/CD a través del github Actions.



## [Documentación API](http://ec2-50-17-28-57.compute-1.amazonaws.com:8000/docs) 
