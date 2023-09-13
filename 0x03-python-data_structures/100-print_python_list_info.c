#include <object.h>
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
	int i = 0;
	long int size = PyList_Size(p);
	PyListObject *element = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", element->allocated);

	for (; i < size; i++)
		printf("Element %i: %s\n", i,
		Py_TYPE(element->ob_item[i])->tp_name);
}
