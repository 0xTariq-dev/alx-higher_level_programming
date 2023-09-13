#include <stdlib.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints list size, allocated elements and types
 *	of the elements.
 * @p: A pointer to python object.
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p);

void print_python_list_info(PyObject *p)
{
	int i = 0, size, allocated;
	PyObject *element;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
