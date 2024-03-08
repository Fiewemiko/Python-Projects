
import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirlte","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])

table.align = "l"
print(table)


