from write_environment import Environment
import write_environment

help(write_environment)
Environment().clear()
Environment().add("test","100")
Environment().add("test","100")
print(Environment("test").value)
