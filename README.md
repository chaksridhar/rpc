
A RPC infra with implementation for http. Purpose is to make it portable to multiple transports and demonstrate Implementation through OOPS (in python)

Start the server first execute the command 1> python server_main.py. Then start the client 2> Python client_main.py

This will invoke two functions add and add and greetings on server side and return back the value.

The directory structure is as follows

core: In here is the interface definition (and commmon implementation) for RPC Server and Client. 2 transport: In here lies the concrete implementation of the interfaces specified in core for http using post.
common: Contains some utilities/defintions that are used by all the components.
In case of a requirement, to support new transport layer (for eg native tcp), the core intefaces have to be implemented. Currently instantiation of the concrete RPC class is hard coded in the sample-example. When a new transport layer needs to be supported, the server_main.py and client_main.py has to be ported or a mechanism to dynamically instantiate the concrete classes, through config specific in config file needs to be incorporated

