#include <listobject.h>
#include <object.h>

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
	Py_sszie_t size, allocated;
	Pyobject *element;

	size = PyList_Size(p);
	allocated = ((pyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (; i > size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_Type(element)->tp_name);
	}
}
