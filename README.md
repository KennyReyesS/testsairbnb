<p align="center">
   <a href="https://github.com/KennyReyesS/AirBnB_clone">[ AirBnB_Clone ]</a>
</p>

<p align = "center">
   <img src="https://i.ibb.co/YNcJjqS/Clone-airbnb.jpg" alt="Clone_airbnb" border="0">
</p>

<p align="center">
        In this project we going to learn how to build a the first part of the project clone AirBnB
</p>

---

Coding Style
-----------
All python files are interpreted and compiled on Ubuntu 20.04 using python3 and PEP 8 style.


---

Usage
-----------
<p>Interactive Mode</p>

```
$./console.py
(hbnb) <command>
```

<p>Non-Interactive Mode</p>

```
$ echo "<command>" | ./console.py
```

---
Examples
-----------

help [command name]:
```
$./console.py
(hbnb) help create
Create a new instance of BaseModel and save in JSON
(hbnb)
```

create command:
```
(hbnb) create BaseModel
4811b20d-715b-4b60-bcfc-be68c9074a0d
(hbnb)
```

all command:
```
(hbnb) all BaseModel
["[BaseModel] (4811b20d-715b-4b60-bcfc-be68c9074a0d) {'id': '4811b20d-715b-4b60-bcfc-be68c9074a0d', 'created_at': datetime.datetime(2021, 7, 1, 0, 59, 53, 378597), 'updated_at': datetime.datetime(2021, 7, 1, 0, 59, 53, 378612)}"]
(hbnb)
```

show command:
```
(hbnb) show BaseModel 4811b20d-715b-4b60-bcfc-be68c9074a0d
[BaseModel] (4811b20d-715b-4b60-bcfc-be68c9074a0d) {'id': '4811b20d-715b-4b60-bcfc-be68c9074a0d', 'created_at': datetime.datetime(2021, 7, 1, 0, 59, 53, 378597), 'updated_at': datetime.datetime(2021, 7, 1, 0, 59, 53, 378612)}
(hbnb)
```

update command:
```
(hbnb) update BaseModel 4811b20d-715b-4b60-bcfc-be68c9074a0d first_name "betty"
(hbnb) show BaseModel 4811b20d-715b-4b60-bcfc-be68c9074a0d
[BaseModel] (4811b20d-715b-4b60-bcfc-be68c9074a0d) {'first_name': 'betty', 'created_at': datetime.datetime(2021, 7, 1, 0, 59, 53, 378597), 'updated_at': datetime.datetime(2021, 7, 1, 0, 59, 53, 378612), 'id': '4811b20d-715b-4b60-bcfc-be68c9074a0d'}
(hbnb)
```

destroy command:
```
(hbnb) destroy BaseModel 4811b20d-715b-4b60-bcfc-be68c9074a0d
(hbnb) show BaseModel 4811b20d-715b-4b60-bcfc-be68c9074a0d
** no instance found **
(hbnb)
```

---
Command
------------

<table style= "width:90%">
	<tr>
		<th>Command</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>help [command name] </td>
		<td>Print a help string containing instructions about the commands</td>
	</tr>
	<tr>
		<td>all [class name] </td>
		<td>Print all string of all instances based on the class name</td>
	</tr>
	<tr>
		<td>show [class name] [id] </td>
                <td>Print the string of instance based in the class name</td>
	</tr>
	<tr>
                <td>create [class name] </td>
                <td>create a new instance/object</td>
        </tr>
	<tr>
                <td>update [class name] [] [] </td>
                <td>Updates an instance based on te class name</td>
        </tr>
	<tr>
                <td>quit</td>
                <td>Exit the program</td>
        </tr>

</table>

---
## [Authors](https://github.com/KennyReyesS/AirBnB_clone/blob/main/AUTHORS)

<ul>
        <li>Kenny Reyes</li>
        <li>Jose Herrera</li>
</ul>

-------

