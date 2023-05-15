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
