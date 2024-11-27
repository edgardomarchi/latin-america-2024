import m5
from m5.debug import flags
from m5.objects.Root import Root
from m5.objects.HelloSimObject import HelloSimObject, GoodByeSimObject

root = Root(full_system=False)
root.hello = HelloSimObject(num_hellos=5)
root.hello.goodbye_object = GoodByeSimObject()

m5.instantiate()

flags["HelloExampleFlag"].enable()

exit_event = m5.simulate()

print(f"Exited simulation because: {exit_event.getCause()}.")
