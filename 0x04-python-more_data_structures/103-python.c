#include <stdio.h>
#include "Python.h"

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *list_object;

	list_object = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", list_object->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list_object->allocated);

	while (i < list_object->ob_base.ob_size)
	{
		printf("Element %d: %s\n", i, list_object->ob_item[i]->ob_type->tp_name);
		i++;
	}
}

void print_python_bytes(PyObject *p)
{
	int i;
	PyBytesObject *byte_object;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object");
		return;
	}
	byte_object = (PyBytesObject *)p;
	printf("[.] bytes object info");
	printf("size: %lu\n", PyBytes_Size(byte_object));
	printf("trying string: %s\n", PyBytes_AsString(byte_object));
	printf("first %lu bytes: ", PyBytes_Size(byte_object) + 1);
	if (PyBytes_Size(byte_object) >= 10)
	{
		i = 0;
		while (i < 10)
		{
			printf("%x ", PyBytes_AsString(byte_object));
			i++;
		}
	}
	else
	{
		i = 0;
		while (i < PyBytes_Size(byte_object))
		{
			printf("%x ", PyBytes_AsString(byte_object));
			i++;
		}

	}
	printf("\n");
}
