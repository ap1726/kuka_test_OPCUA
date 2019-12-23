
from opcua import Client
from opcua import ua


if __name__ == "__main__":

    client = Client("opc.tcp://OpcUaObserver@192.168.123.5:4840")
    client.set_password("kuka")
    try:
        client.connect()
        client.load_type_definitions()  # load definition of server specific structures/extension objects

        root = client.get_root_node()
        print(root)
        # objects = client.get_objects_node()
        # print(objects)
        # print(root.get_children())
        # print(root.get_children()[0].get_children())
        # print(root.get_children()[1].get_children())
        # print(root.get_children()[0].get_children()[0].get_children())
        # print( root.get_children()[0].get_children()[1].get_children())
        print("-------------------------------------------------------------------------------------------")
        print(root.get_children()[0].get_children()[1].get_children()[0].get_children()[4].get_children()[1].get_children()[4].get_children()[2].get_children())
        artsignals = root.get_children()[0].get_children()[1].get_children()[0].get_children()[4].get_children()[1].get_children()[4].get_children()[2].get_children()[1].get_children()
        for i in artsignals:
            # print(i, "=", i.get_data_value())
            print(i, "=", i.get_value())
        #varprint("Children of root are: ", root.get_children()) = client.get_node("ns=3;i=2002")
        #var.get_data_value() # get value of node as a DataValue object
        #var.get_value() # get value of node as a python builtin
        # myvar = root.get_child(["0:Objects", "{}:MyObject".format(idx), "{}:MyVariable".format(idx)])
        # obj = root.get_child(["0:Objects", "{}:MyObject".format(idx)])

    finally:
        client.disconnect()
